# List implementation in python
# Creating a List

def create_list():
    List = []
    return List


def check_empty(List):
    return len(List) == 0


def insert(List, i, item):
    List.insert(i, item)
    print("Insert element: " , item)


def remove(List, item):
    if (check_empty(List)):
        return "List is empty"
    print("Removing element : ", item)
    return List.remove(item)


List = create_list()
insert(List, 0, 1)
insert(List, 1, 2)
insert(List, 2, 3)
insert(List, 3, 4)
remove(List, 2)
print("List after removing an element: " , List)