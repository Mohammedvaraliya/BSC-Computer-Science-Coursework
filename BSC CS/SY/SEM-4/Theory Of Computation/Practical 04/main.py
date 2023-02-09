# Design a Program for creating machine that accepts three consecutive one.

states = {
    "A": {
        "0": "A",
        "1": "B"
    },
    "B": {
        "0": "A",
        "1": "C"
    },
    "C": {
        "0": "A",
        "1": "D"
    },
    "D": {
        "0": "F",
        "1": "E"
    },
    "E": {
        "0": "E",
        "1": "E"
    },
    "F": {
        "0": "F",
        "1": "G"
    },
    "G": {
        "0": "F",
        "1": "H"
    },
    "H": {
        "0": "F",
        "1": "D"
    }
}

initial_state = "A"
final_states = ["D", "F", "G", "H"]


def three_consecutive_one(string: str):
    current_state = initial_state  # By defaul initial state

    for s in string:
        # Transition to next state
        current_state = states[current_state][s]

    if current_state in final_states:
        return True

    return False


def three_consecutive_one_recursive(string:str, current_state:str):
    # print(string, current_state)
    if len(string) == 1:
        return True if states[current_state][string[0]] in final_states else False

    return three_consecutive_one_recursive(string[1:], states[current_state][string[0]])



if __name__ == "__main__":

    # 0110 is the binary of decimal 6

    user_input = input("Enter the string : ")

    X = three_consecutive_one(user_input)
    print("Accepted" if X else "Not accepted")

    Y = three_consecutive_one_recursive(user_input, initial_state)
    print("Accepted" if Y else "Not accepted")
