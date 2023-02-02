Aim : Design a program for accepting decimal number divisible by 2.

    Design a program for accepting decimal number divisible by 2.
    This code is implementing a program that checks if a decimal number is divisible by 2 or not. 
    
    It does so by converting the decimal number to its binary representation and then checking if the last digit of the binary representation is 0 or not.

    The program defines a states dictionary that has two states, "A" and "B". 
    
    The "A" state represents a number that is divisible by 2, 
    and the "B" state represents a number that is not divisible by 2. 
    
    The program then uses a transition function to move from one state to another based on the binary digit of
    the number being processed. 
    
    If the state reaches "A" after processing all the binary digits, it means the number is divisible by 2, 
    and the program returns True.