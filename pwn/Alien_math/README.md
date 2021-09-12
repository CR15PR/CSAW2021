The goal of this challenge is to call the print_flag function which opens the flag.txt file on the remote server. In order to call the print_flag function you have to answer two questions correctly to get to the vulnerable `gets` function in `final_question`.
While the first and second questions do not have b0f vulnerable functions they have poor implementations of rand() that enable you to bypass the checks in order to get to the vulnerable function.

Main takes user input from `__isoc99_scanf` and string formats it to a decimal number. Then `rand()` is called with a default seed and compared against the user input. This is not a secure function and can is easily predicted. This funciton will always return the same result on the first iteration based on your version of libc if given a default seed. Since we have to bypass this check we have two options; to either have python generate the value or pull it from memory. I chose to pull the value from GDB.

`b *main+103` to stop at ` 0x00000000004015f5 <+103>:	cmp    QWORD PTR [rbp-0x8],rax`

`$rax` is compared to `$rbp-0x8` so we examine this offset on the stack: `x/gx $rbp-0x8` and we get `0x7fffffffdcf8:	0x000000006b8b4567` or 1804289383 in decimal.

![pic](https://github.com/CR15PR/CSAW2021/blob/main/pwn/Alien_math/alien-math-main.png)

After this `__isoc99_scanf` is called again and our input is formated to a max of 24 characters as a string. Our input is then put passed into the `second_question` function

Next some funky values are placed on the stack and our input is sent through a convulated transformation. 
![pic](https://github.com/CR15PR/CSAW2021/blob/main/pwn/Alien_math/alien-math-second-question-transformation.png)

The transformation is compared against a static value of 7759406485255323229225. We can pull this value from memory:

`b *second_question+358` then give some input and continue and `x/gx $rdi` which yields 7759406485255323229225.

Again we have two options; we can either model the function in python and use Microsoft's z3 utilities to create the acceptable input or brute force the key character by character since the same input will always produce the same output.

User input is stored in `$rsi` so using this breakpoint you can character by character observe the changes to yield the correct result:

  ``` 7 - 7
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
      7856445899213065428791 - 7759406485255323229225```


