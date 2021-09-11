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
