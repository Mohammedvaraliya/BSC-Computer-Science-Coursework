# WAP to implement all implement all the methods of dictionary

def printDictionary():
    dict = {
        "brand": "Alpina",
        "model": "BMW",
        "year": "7 March 1916"
    }
    print(dict)

    print(dict["brand"])

    dict = {
        "brand": "Alpina",
        "model": "BMW",
        "year": "7 March 1916",
        "colors": ["white", "Golden", "Blue"]
    }
    print(dict)

    print(len(dict))
    print(type(dict))

    # Accessing the item
    x = dict["model"]
    print(x)

    x = dict.keys()
    print(x)

    x = dict.values()
    print(x)

    x = dict.items()
    print(x)

    if "model" in dict:
        print("Yes, 'model' is one of the keys in the thisdict dictionary")

    # Changing the item from the dictionary
    x = dict["year"] = "7 March 1976" # it will change the original dictionary
    print(x)
    print(dict)

    # clear the dictionary
    x = dict.clear()
    print(dict)

    # loop in dictionary
    dict = {
        "brand": "Alpina",
        "model": "BMW",
        "year": "7 March 1916",
        "colors": ["white", "Golden", "Blue"]
    }
    for x in dict:
        print(dict[x])

    # One more to get values
    for x in dict.values():
        print(x)

    # One more to get keys
    for x in dict.keys():
        print(x)

    # To get both keys and values
    for x,y in dict.items():
        print(f"{x}:{y}")
        

if __name__ == "__main__":
    printDictionary()
