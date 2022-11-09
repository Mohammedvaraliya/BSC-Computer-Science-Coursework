# WAP to handle multiple exceptions.

# ArithmeticError
try:
    print(5/0)
except ArithmeticError:
    print("Arithmetic Error encountered")    
    
# AttributeError
try:
    print.something()
except AttributeError:
    print("Attribute Error encountered")

# ImportError
try:
    import some_random_module
except ImportError:
    print("Import Error encountered")

# IndexError
try:
    nums = [1,2,3]
    print(nums[5])
except IndexError:
    print("Index error is encountered")

# KeyError
try:
    dict = {"foo":"bar"}
    print(dict["baz"])
except KeyError:
    print("Key error is encountered")

# NameError
try:
    cars = ["Aston Martin", "BMW", "Kia"]
    print(carrs)
except NameError:
    print("Name error encountered")
# OSError
# SyntaxError
# TypeError
try:
    a = 'Hello'
    b = 5
    print(a + b)
except TypeError:
    print("Type error encountered")
# ValueError
try:
    myNum = 7
    myList = []
    myList.remove(myNum)
except:
    print("Value error encountered")
# ZeroDivisionError
try:
    print(5/0)
except:
    print("zero division error encountered")