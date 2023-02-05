Aim : Design a Program for creating machine that accepts three consecutive one.

    This code defines a program that accepts a string and returns True if there are three consecutive 1's 
    in the string and False otherwise.

    It uses two approaches to solve this problem: an iterative approach and a recursive approach.

    The iterative approach uses a finite state machine represented by the states dictionary. 
    
    The finite state machine has four states: A, B, C, and D. 
    
    When the machine is in state A and it encounters a 0, it remains in state A. 
    
    When it encounters a 1, it transitions to state B. 
    
    When it is in state B and it encounters a 0, it transitions back to state A, but when it encounters a 1, 
    it transitions to state C. 
    
    Similarly, when it is in state C and it encounters a 0, it transitions back to state A, but when it encounters a 1, 
    it transitions to state D. 
    
    When it is in state D, it remains in state D regardless of the input. 
    
    The count variable keeps track of the number of consecutive 1's encountered so far, 
    and consecutive_one keeps track of whether three consecutive 1's have been encountered.

    The recursive approach works similarly, but instead of a loop, it uses recursion to transition from one state to the next. 
    
    The three_consecutive_one_recursive function takes the input string, the current state, a count of the number of consecutive 1's,
    and a flag indicating whether three consecutive 1's have been encountered. 
    
    If the input string is empty, the function returns True if three consecutive 1's have been encountered, and False otherwise. 
    
    If the current character in the string is 1, the next state is updated to the next state in the finite state machine, 
    the count is incremented, and the consecutive_one flag is set to 3 if the count is equal to 3. 
    
    If the current character in the string is 0, the next state is updated to the next state in the finite state machine and the count is reset to 0. 
    
    The function then makes a recursive call with the rest of the string and the updated values for the current state, 
    count, and consecutive_one.