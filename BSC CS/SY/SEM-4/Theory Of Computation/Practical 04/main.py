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


def check_string(string: str):
    current_state = initial_state  # By defaul initial state
    count = 0
    print(string)

    for s in string:
        # Transition to next state
        if (s == "1"):
            current_state = states[current_state][s]
            count += 1
            print(count)
        else:
            current_state = states[current_state][s]
            count = 0
            print(count)


    return True if count >= 3 else False


# If len == 1

# [1:]

# def check_string_recursive(string: str, current_state: str):
#     # print(string, current_state)
#     if len(string) == 1:
#         return True if states[current_state][string[0]] == final_state else False

#     return check_string_recursive(string[1:], states[current_state][string[0]])



if __name__ == "__main__":

    # 0110 is the binary of decimal 6

    user_input = input("Enter the string : ")

    X = check_string(user_input)
    print("Accepted" if X else "Not accepted")

    # Y = check_string_recursive(user_input, initial_state)
    # print("Accepted" if Y else "Not accepted")
