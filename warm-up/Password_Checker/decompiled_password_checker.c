void password_checker(void)

{
  undefined8 local_a8;
  undefined local_a0;
  char local_78 [48];
  char local_48 [60];
  int local_c;
  
  printf("Enter the password to get in: \n>");
  gets(local_48);
  strcpy(local_78,local_48);
  local_a8 = 0x64726f7773736170;
  local_a0 = 0;
  local_c = strcmp(local_78,(char *)&local_a8);
  if (local_c == 0) {
    printf("You got in!!!!");
  }
  else {
    printf("This is not the password");
  }
  return;
}
