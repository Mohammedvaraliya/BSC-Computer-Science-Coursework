# Design a program for Turing machine that’s accepts the even number of 1's.

states = {
    'A': {
        '0': ('A', '0', 'R'), 
        '1': ('B', '0', 'R'), 
        '_': ('D', '_', 'L')
    },
    'B': {
        '0': ('B', '0', 'R'), 
        '1': ('A', '0', 'R'), 
        '_': ('C', '_', 'L')
    },
    'C': {
        '0': ('C', '0', 'L'), 
        '1': ('C', '1', 'L'), 
        '_': ('A', '_', 'R')
    },
    'D': {
        '0': ('D', '0', 'L'), 
        '1': ('D', '1', 'L'), 
        '_': ('E', '_', 'R')
    },
    'E': {
        '0': ('D', '0', 'R'), 
        '1': ('D', '1', 'R'), 
        '_': ('F', '_', 'L')
    },
    'F': {
        '0': ('F', '0', 'L'), 
        '1': ('F', '1', 'L'), 
        '_': ('A', '_', 'R')
    }
}

initial_state = "A"
final_state = {"A"}

def turing_machine(input_str):
    current_state = initial_state
    tape = list(input_str)
    i_head = 0

    while True:
        if tape[i_head] not in states[current_state]:
            return False

        new_state, write_value, move_dir = states[current_state][tape[i_head]]
        tape[i_head] = write_value

        if move_dir == 'R':
            i_head += 1
        elif move_dir == 'L':
            i_head -= 1

        current_state = new_state

        if current_state in final_state and i_head >= len(tape):
            return True
        elif current_state not in states or i_head >= len(tape) or i_head < 0:
            return False



print(turing_machine('011'))  # True
print(turing_machine('01111'))  # True
print(turing_machine('010101111'))  # True
print(turing_machine('01'))  # False
print(turing_machine('1101'))  # False
print(turing_machine('1101101'))  # False
print(turing_machine('110110111'))  # False
