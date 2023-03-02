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
    no_of_zeros = 0
    no_of_one = 0

    for s in string:
        # Transition to next state
        if s == "0":
            no_of_zeros += 1
        if s == "1":
            no_of_one += 1 
        current_state = states[current_state][s]

    return f"The Number of 1's is {no_of_one} and number of 0's is {no_of_zeros}"




if __name__ == "__main__":

    user_input = input("Enter the string : ")

    X = count_string(user_input)
    print(X)

