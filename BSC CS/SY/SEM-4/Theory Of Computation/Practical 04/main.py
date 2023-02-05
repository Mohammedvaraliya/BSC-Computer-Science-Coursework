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
        "0": "D",
        "1": "D"
    }
}

initial_state = "A"


def three_consecutive_one(string: str):
    current_state = initial_state  # By defaul initial state
    count = 0
    consecutive_one = 0
    print(string)

    for s in string:
        # Transition to next state
        if (s == "1"):
            current_state = states[current_state][s]
            count += 1
            if count == 3:
                consecutive_one = 3
        else:
            current_state = states[current_state][s]
            count = 0


    return True if consecutive_one == 3 else False


def three_consecutive_one_recursive(string: str, current_state: str, count: int = 0, consecutive_one: int = 0):

    if len(string) == 0:
        return True if consecutive_one == 3 else False
    
    if string[0] == "1":
        next_state = states[current_state][string[0]]
        count += 1
        if count == 3:
            consecutive_one = 3 
    else:
        next_state = states[current_state][string[0]]
        count = 0

    return three_consecutive_one_recursive(string[1:], next_state, count, consecutive_one)



if __name__ == "__main__":

    # 0110 is the binary of decimal 6

    user_input = input("Enter the string : ")

    X = three_consecutive_one(user_input)
    print("Accepted" if X else "Not accepted")

    Y = three_consecutive_one_recursive(user_input, initial_state)
    print("Accepted" if Y else "Not accepted")
