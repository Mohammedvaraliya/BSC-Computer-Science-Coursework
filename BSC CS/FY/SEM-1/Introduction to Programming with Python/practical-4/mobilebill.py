'''WAP to calculate the mobile bill. The user enters a name, a total number of calls, and messages. The basic rental is Rs. 300. 50 calls and 100 messages are free. after free calls and messages charges are @ Rs. 2 per call and rs. 1 per message. GST @18% is charged on the total bill. Calculate the mobile bill and display the bill with all the break-ups.'''

def mobileBill():
    name = input("Enter Cunsumer Name : ")
    totCalls = int(input("Enter total numbers of calls : "))
    totMsg = int(input("Enter total numbers of messages : "))

    basicRental = 300
    callCost = 0
    msgCost = 0
    if totCalls <= 50 and totMsg <= 100:
        callCost = 0
        msgCost = 0
    if totCalls > 50:
        callCost = (totCalls - 50)*2
    if totMsg > 100:
        msgCost = (totMsg - 100)*1

    basicBill = basicRental + callCost + msgCost
    gstAmt = basicBill * 0.18
    totBill = basicBill + gstAmt
    print("--"*40)
    print("--"*10, "INVOICE", "--"*10)
    print("Cunsumer Name : ", name)
    print("Total calls : ", totCalls)
    print("Total messges : ", totMsg)
    print("Call charges @ Rs.2 : ", callCost)
    print("Message charges @ Rs.1 : ", msgCost)
    print("Bill Amount : Rs.", basicBill)
    print("GST @18% : Rs.", gstAmt)
    print("Total Bill : Rs.", totBill)
    print("--"*40)

mobileBill()