# Create a program that implements 

states = {
    "A": {
        "0": "A",
        "1": "B"
    },
    "B": {
        "0": "A",
        "1": "B"
    }
}

initial_state = "A"
final_state = "A"


def check_string(string: str):
    current_state = "A"  # By defaul initial state

    for s in string:
        # Transition to next state
        current_state = states[current_state][s]

    if current_state == final_state:
        return True

    return False


# If len == 1

# [1:]

def check_string_recursive(string: str, current_state: str):
    print(string, current_state)
    if len(string) == 1:
        return True if states[current_state][string[0]] == final_state else False

    return check_string_recursive(string[1:], states[current_state][string[0]])


print("Accepted" if check_string_recursive(
    "101", initial_state) else "Not accepted")
