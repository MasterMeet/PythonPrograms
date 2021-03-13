#Banking Service
chance = 3
Account_Holder = {"Meet":3352,"Preet":9732,"Jeet":9536}

print("Welcome to City Bank")
accountName = input("Enter Account Name:- ")

while chance>0:
    if accountName in Account_Holder:
        pin = int(input("Enter Your pin:- "))
        if pin == Account_Holder[accountName]:
            print("Account Found") 
            break
        else:
            print("Invalid Pin!")
            print("Chances left:- ",chance-1)
    else:
        print("Account Not Found!")
        break
    chance-=1
