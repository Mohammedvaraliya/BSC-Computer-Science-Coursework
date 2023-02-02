Aim : Design a Program for creating machine that accepts the string always ending with 101.

    Design a Program for creating machine that accepts the string always ending with 101.
    Certainly! This code defines a deterministic finite automaton (DFA) that accepts strings 
    that end with the substring "101". The DFA is modeled using a set of states and state transitions.

    Here's what the code is doing:

    states is a dictionary that defines the state transitions of the DFA. For example, if the DFA is in state 
    "A" and the next character in the input string is "0", it will transition to state "A".

    initial_state is a string that represents the starting state of the DFA, which is set to "A".

    final_state is a string that represents the final or accepting state of the DFA, which is set to "D".

    check_string is a function that takes a string as input and returns a 
    boolean value indicating whether the string is accepted by the DFA. 
    
    The function starts at the initial_state and then uses the states dictionary to transition to the next state 
    for each character in the input string. 
    
    If the final state of the DFA is equal to final_state, the function returns True, indicating that the string is accepted.

    check_string_recursive is a function that takes a string and the current state of the DFA as input, and
    returns a boolean value indicating whether the string is accepted by the DFA. 
