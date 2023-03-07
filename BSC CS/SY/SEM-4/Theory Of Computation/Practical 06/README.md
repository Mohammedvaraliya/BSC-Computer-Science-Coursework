Aim : Design a program for creating a machine which accepts string having equal no. of 1’s and 0’s.

    states dictionary: This defines the transition function for the DFA. Each state is a key in the dictionary, 
    and its value is another dictionary that maps input symbols to the next state. 
    For example, if the current state is "A" and the input symbol is "0", the next state would be "B".

    initial_state variable: This is the initial state of the DFA. In this case, it is set to "A".

    final_state set: This is a set of all final states of the DFA. In this case, it contains the states "A".

    check_string function: This function takes a string as input and returns a boolean indicating whether the input 
    string is accepted by the DFA. The function uses the transition function defined in the states dictionary to 
    transition between states for each input symbol in the string. 
    
    It also keeps track of the count of 0's and 1's in the string, and checks whether the final state is in 
    the set of final states and the counts are equal.

    user_input variable: This takes user input to get the string to be checked.

    X variable: This is assigned the return value of the check_string function.

    The program then prints "Accepted" if the value of X is True, and "Not accepted" otherwise.
