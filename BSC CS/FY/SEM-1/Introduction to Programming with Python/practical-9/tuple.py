# WAP to create Tuple, Access items in tuple through slicing, implement all the methods of tuples.

def printTuple():
    tuple = ()
    print(tuple)

    # Tuple having integers
    tuple = (1, 2, 3)
    print(tuple)

    # tuple with mixed datatypes
    tuple = (1, "Hello", 3.4)
    print(tuple)

    # nested tuple
    tuple = ("mouse", [8, 4, 6], (1, 2, 3))
    print(tuple)

    # tuple having no parenthesis
    tuple = 3, 4.6, "Animal"
    print(tuple)

    # tuple unpacking is also possible
    a, b, c = tuple
    print(a) #3
    print(b) #4.6
    print(c) #Animal

    # Types of tuples
    tuple = ("Varaliya")
    print(type(tuple))

    tuple = (1, 2 ,3)
    print(type(tuple))

    tuple = ("varaliya", 2, 4, 6)
    print(type(tuple))

    # Accessing tuple elements using indexing
    tuple = ("v", "a", "r", "a", "l", "i", "y", "a")
    print(tuple[0]) # v
    print(tuple[1]) # a
    print(tuple[2]) # r
    print(tuple[3]) # a
    print(tuple[4]) # l
    print(tuple[5]) # i
    print(tuple[6]) # y
    print(tuple[7]) # a

    # nested tuple
    tuple = ("varaliya", [8, 4, 6], (1, 2, 3))
    print(tuple[0][6]) # from 0th index to 6 alphabet
    print(tuple[1][2]) # from 1th index means [] to 2nd element

    # Negative indexing for accessing tuple elements
    tuple = ('p', 'e', 'r', 'm', 'i', 't')
    print(tuple[-1]) # t
    print(tuple[-6]) # p

    # Accessing tuple elements using slicing
    tuple = ("v", "a", "r", "a", "l", "i", "y", "a")
    print(tuple[0:8])
    print(tuple[0:]) # from 0 to end
    print(tuple[:8]) # from 8 to start
    print(tuple[:]) # from 0 to end
    print(tuple[:-1]) # from lats 1 to start

    # Iterating Through a Tuple
    # Using a for loop to iterate through a tuple
    for name in ('varaliya', 'unknown'):
        print("Hello", name)

if __name__ == "__main__":
    printTuple()