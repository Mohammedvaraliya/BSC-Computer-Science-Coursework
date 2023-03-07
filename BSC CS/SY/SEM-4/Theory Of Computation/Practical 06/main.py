# Design a program for creating a machine which accepts string having equal no. of 1’s and 0’s.

states = {
    "A": {
        "0": "B",
        "1": "B"
    },
    "B": {
        "0": "A",
        "1": "A"
    }
}

initial_state = "A"
final_state = {"A"}


def check_string(string:str):
    current_state = initial_state # By defaul initial state
    count_0 = 0
    count_1 = 0

    for s in string:
        # Transition to next state
        if s == "0":
            count_0 += 1
        if s == "1":
            count_1 += 1 
        current_state = states[current_state][s]

    if current_state in final_state and count_0 == count_1:
        return True

    return False



# If len == 1

# [1:]

def check_string_recursive(string:str, current_state:str, count_0 = 0, count_1 = 0):
    # print(string, current_state)
    if len(string) == 0:
        return True if current_state in final_state and count_0 == count_1 else False
    
    if string[0] == "0":
        count_0 += 1
    if string[0] == "1":
        count_1 += 1 

    return check_string_recursive(string[1:], states[current_state][string[0]], count_0, count_1)



if __name__ == "__main__":

    user_input = input("Enter the string : ")

    X = check_string(user_input)
    print("Accepted" if X else "Not accepted")

    Y = check_string_recursive(user_input, initial_state)
    print("Accepted" if Y else "Not accepted")

