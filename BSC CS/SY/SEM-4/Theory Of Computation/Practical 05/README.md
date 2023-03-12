Aim : Design a Turing machine that’s accepts the even number of 1's.

    This program is implementing a Turing machine that accepts strings with an even number of 1's. 
    A Turing machine is a theoretical model of computation that consists of an infinite tape divided into discrete cells, 
    a read/write head that can read or write to a cell on the tape, and a finite set of states that the machine can be in. 
    The Turing machine operates by moving its read/write head left or right on the tape, writing new symbols on the tape, 
    and changing its state according to a set of rules or transitions.

    In this program, the Turing machine is defined using a dictionary of states. Each state is represented by a key in the dictionary, 
    and the value is another dictionary that specifies the transitions for that state. Each transition is represented as a tuple of three 
    values: the next state, the symbol to write to the tape, and the direction to move the read/write head 
    (either 'R' for right or 'L' for left).

    The initial state of the Turing machine is 'A', and the input string is passed to the function as an argument. The input string is
    represented as a list of characters, and the read/write head of the Turing machine is initially positioned at the leftmost 
    cell of the tape (index 0).

        1. The main loop of the program iterates over the transitions of the current state and performs the following steps:

        2. If the symbol at the current position of the tape is not a valid input for the current state, the function returns False.

        3. The transition for the current symbol is retrieved from the dictionary of transitions for the current state.

        4. The symbol on the tape is updated to the value specified by the transition.

        5. The read/write head is moved left or right depending on the direction specified by the transition.

        6. The current state is updated to the next state specified by the transition.

    If the current state is 'A' and the read/write head has reached the end of the input string, or if the current state is 'D' and the read/
    write head has moved off the left end of the tape, the function returns True, indicating that the input string has 
    been accepted by the Turing machine.

    If the current state is not a valid state or the read/write head has moved off the right end of the tape or the left end of the tape, 
    the function returns False, indicating that the input string has been rejected by the Turing machine.

    Finally, the program calls the turing_machine function with two example input strings ('011' and '1101') and prints the output, 
    which should be True for the first input string and False for the second input string, 
    
    since the first input string contains an even number of 1's and the second input string contains an odd number of 1's.
