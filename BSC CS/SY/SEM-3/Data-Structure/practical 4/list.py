# List implementation in python
# Creating a List

def create_list():
    List = []
    return List


# Creating an empty List
def check_empty(List):
    return len(List) == 0


# Adding items into the List
def insert(List, i, item):
    List.insert(i, item)
    print("Insert item: " , item)


# Removing an element from the List
def remove(List, item):
    if (check_empty(List)):
        return "List is empty"

    return List.remove(item)


List = create_list()
insert(List, 0, 1)
insert(List, 1, 2)
insert(List, 2, 3)
insert(List, 3, 4)
print("Removing element ")
remove(List, 2)
print("List after removing an element: " , List)