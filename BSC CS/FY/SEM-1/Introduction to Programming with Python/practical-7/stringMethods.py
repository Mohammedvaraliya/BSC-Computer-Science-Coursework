# WAP to implement all the methods of class str1 (str1ing Methods )

def string_methods():
    str1 = "python language"
    str2 = "5454"
    print("The str1ing is : ", str1)

    # Implementation for str1
    #Capitalize
    print("Capitalize():\n",str1.capitalize())
    #Casefold
    print("Casefold(): \n",str1.casefold())
    #Center
    print("Center(): \n",str1.center(50,"-"))
    #Count
    print("Count(): \n",str1.count("Hello"))
    #Encode
    print("Encode(): \n",str1.encode())
    #Endswith
    print("Endswith(): \n",str1.endswith("n"))
    #Expand Tabs
    print("Expand Tabs(): \n","Hello \t world".expandtabs(10))
    #Find
    print("Find(): \n",str1.find("world"))
    #Format
    print("Format(): \n","This is how {x} {y}".format(x="formatting",y="works."))
    #Starts with
    print("Starts with(): \n",str1.startswith("python"))
    #is ASCII
    print("Is ASCII(): \n",str1.isascii())

    # Implementation for str2
    # isnumeric
    print("isnumeric(): \n",str2.isnumeric())
    # islower
    print("islower(): \n",str2.islower())
    # isspace
    print("isspace(): \n",str2.isspace())
    # isprintable
    print("isprintable(): \n",str2.isprintable())
    # istitle
    print("istitle(): \n",str2.istitle())
    # isupper
    print("isupper(): \n",str2.isupper())


  
if __name__ == "__main__":
    string_methods()