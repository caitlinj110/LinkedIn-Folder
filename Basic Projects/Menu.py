
#varibles 
balance=0 # set to zero 
numbers=[] #set list to empty

#while tool allow you to repeat the loop
#TRUE help the control the flow of the the loop which determine if it need to repeat or stop
while True:

    print()
    print("Option 1: Deposit")
    print("Option 2: Withdraw")
    print("Option 3: Current balance")
    print("Option 4: Process a Transaction")
    print("Option 5: Print Transactions")

    choice=str(input("Choose a option:"))

    if(choice=="1"):
        user_option=int(input("Enter the amount:"))
        balance+=user_option

    elif(choice=="2"):
        user_option=int(input("Enter the amount:"))
        balance-=user_option

    elif(choice=="3"):
        txt=f"${balance}"
        print(txt)

    elif(choice=="4"):
        numbers.append(balance)
        print("Process Completed")

    elif(choice=="5"):
        print(numbers)


