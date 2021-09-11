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
