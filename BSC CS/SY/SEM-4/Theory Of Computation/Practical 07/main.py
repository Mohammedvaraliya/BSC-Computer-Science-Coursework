# Design a program for creating a machine which count number of 1's and 0's in a given string.

states = {
    "A": {
        "0": "A",
        "1": "A"
    }
}

initial_state = "A"

def count_string(string:str):
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

    return f"The Number of 1's is {count_1} and number of 0's is {count_0}"


def check_string_recursive(string:str, current_state:str, count_0 = 0, count_1 = 0):
    # print(string, current_state)
    if len(string) == 0:
        return f"The Number of 1's is {count_1} and number of 0's is {count_0}"
    
    if string[0] == "0":
        count_0 += 1
    if string[0] == "1":
        count_1 += 1 

    return check_string_recursive(string[1:], states[current_state][string[0]], count_0, count_1)




if __name__ == "__main__":

    user_input = input("Enter the string : ")

    X = count_string(user_input)
    print(X)

    Y = check_string_recursive(user_input, initial_state)
    print(Y)

