# WAP to check whether the input age is eligible to vote.
def ageToVote():
    age = int(input("Enter your age :"))
    if age >= 18:
        print("Your age is ", age, ",you can vote ")
    else:
        print("Your age is ", age, ",you cannot vote ") 

ageToVote()
