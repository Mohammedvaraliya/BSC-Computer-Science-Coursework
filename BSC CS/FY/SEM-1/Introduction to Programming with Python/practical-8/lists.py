# WAP to implement all the list methods

def printLists():
    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    stack = [2,4,5,6,7,8]
    squares = []
    print(fruits)

    # Counting the elements in the list
    print(fruits.count('apple'))
    print(fruits.count('kiwi'))
    print(fruits.count('banana'))

    # Finding the element index number
    print(fruits.index('banana'))
    print(fruits.index('apple'))
    print(fruits.index('kiwi'))
    print(fruits.index('banana', 4)) # Find next banana starting a position 4
    print(fruits.index('pear'))

    # Using Lists as Stacks
    stack.append(10)
    print(stack)

    stack.pop() # it will remove the last element in the list
    print(stack)

    # Using list comprehension
    for x in range(10):
        squares.append(x**2) # exponent of will return the square of all number in range 10
    
    print(squares)

if __name__ == "__main__":
    printLists()