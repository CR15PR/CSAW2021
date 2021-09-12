The goal of this challenge is to call the print_flag function which opens the flag.txt file on the remote server. In order to call the print_flag function you have to answer two questions correctly to get to the vulnerable `gets` function in `final_question`.
While the first and second questions do not have b0f vulnerable functions they have poor implementations of rand() that enable you to bypass the checks.

