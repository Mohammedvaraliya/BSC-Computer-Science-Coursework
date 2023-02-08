Aim : Design a Program for creating machine that accepts three consecutive one.

    This code defines a finite state machine that accepts a string of 0s and 1s as input 
    and returns Accepted or Not accepted based on whether the string contains three consecutive 1s.

    The state machine is defined by the states dictionary. 
    It maps a current state to a dictionary that maps the next input (0 or 1) to the next state. 
    For example, if the current state is "A" and the next input is 1, the next state will be "B".

    The initial state is "A" and the final states are ["D", "F", "G", "H"]. 
    The machine will accept a string if it reaches any of the final states.

    The three_consecutive_one function takes a string as input and returns True or False 
    based on whether the string is accepted by the state machine. 
    
    It starts from the initial state and uses the states dictionary to transition from one state to the next based on the next input.
    If the current state after processing the whole string is in the final states, the function returns True. 
    Otherwise, it returns False.

    The three_consecutive_one_recursive function is a recursive implementation of the same machine. 
    It takes a string and a current state as inputs and returns True or False based on whether the 
    string is accepted by the machine starting from the current state. 
    
    If the length of the string is 1, it returns True if the next state after processing the input is in the final states. 
    Otherwise, it returns False. 
    
    If the length of the string is more than 1, it processes the first input, updates the current state, 
    and calls itself with the rest of the string and the updated current state.
