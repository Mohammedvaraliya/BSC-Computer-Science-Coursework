# WAP for simple Mobile and Laptop Store using functions. (use mainof  and if-else statement is compulsory )
def mobile():
    print(" ~~~~~ iPhone Mobile @ Rs. 80000 ~~~~")
    pname = "iPhone Mobile"
    price = 80000
    quantity = int(input("Quantity : "))
    BasicAmt = quantity*price
    gstAmt = BasicAmt*0.18
    TotalAmt = BasicAmt + gstAmt
    bill(pname,price,quantity,BasicAmt,gstAmt,TotalAmt)
    

def laptop():
    print(" ~~~~~ Macbook @ Rs. 200000 ~~~~")
    pname = "Macbook"
    price = 200000
    quantity = int(input("Quantity : "))
    BasicAmt = quantity*price
    gstAmt = BasicAmt*0.18
    TotalAmt = BasicAmt + gstAmt
    bill(pname,price,quantity,BasicAmt,gstAmt,TotalAmt)

def bill(pname,price,quantity,BasicAmt,gstAmt,TotalAmt) :
    print("~~~~~~~~~~ INVOICE ~~~~~~~~~~~~~")
    print("Product : ",pname)
    print("Price : ",price)
    print("Quantity : ",quantity)
    print("Basic Amount : Rs.",BasicAmt)
    print("GST @18% : Rs.",gstAmt)
    print("Total Bill : Rs.",TotalAmt)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

if __name__ == "__main__":
    while(True):
        print("~~~ Mobile and Laptop Store ~~~~")
        print("1 - iPhone Mobile @ Rs. 80000")
        print("2 - Macbook  @ Rs. 200000")
        print("2 - Exit")
        choice = int(input("Enter your choice : "))
        if choice == 1 :
            mobile()
        elif choice == 2 :
            laptop()
        elif choice == 3 :
            break
        else :
            print("Wrong Input !")
    print("~~~ Thank you ~~~~")
