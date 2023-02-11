# Create a program that implements a machine that accepts strings ending with '101'

states = {
    "A": {
        "0": "A",
        "1": "B"
    },
    "B": {
        "0": "C",
        "1": "B"
    },
    "C": {
        "0": "A",
        "1": "D"
    },
    "D": {
        "0": "C",
        "1": "B"
    }
}

initial_state = "A"
final_state = "D"


def check_string(string:str):
    current_state = initial_state # By defaul initial state

    for s in string:
        # Transition to next state
        current_state = states[current_state][s]

    if current_state == final_state:
        return True

    return False



# If len == 1

# [1:]

def check_string_recursive(string:str, current_state:str):
    # print(string, current_state)
    if len(string) == 1:
        return True if states[current_state][string[0]] == final_state else False

    return check_string_recursive(string[1:], states[current_state][string[0]])



if __name__ == "__main__":

    user_input = input("Enter the string : ")

    X = check_string(user_input)
    print("Accepted" if X else "Not accepted")

    Y = check_string_recursive(user_input, initial_state)
    print("Accepted" if Y else "Not accepted")
