Aim : Design a program for creating a machine which count number of 1’s and 0’s in a given string.

    The states dictionary represents the state transition table for the finite state machine (FSM) that we will use to count the 
    number of 1's and 0's in a given string. In this case, there is only one state A, and it transitions to itself on both 0 and 1 inputs.

    The initial_state variable stores the starting state of the FSM, which is A in this case.

    The count_string function takes a string as input and returns a formatted string that contains the number of 1's and 0's in the input string.

    The current_state variable is initially set to the starting state of the FSM, which is A.

    The no_of_zeros and no_of_one variables are used to keep track of the number of 0 and 1 characters seen so far in the input string.

    The for loop iterates through each character in the input string.

    For each character s, the FSM transitions to the next state based on the current state and the input character. 
    In this case, the transition is simply to the same state, regardless of the input character. 
    At the same time, the function updates the counts of 0 and 1 characters.

    After processing all characters in the input string, the function returns a formatted string that contains the counts of 0 and 1 characters.

    Finally, the main block of code prompts the user to input a string, calls the count_string function with the user input, 
    and prints the output string.