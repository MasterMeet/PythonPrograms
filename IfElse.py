print("-----------")
#MAximum No using ifelse
print("Maximum among 3 Numbers")
num1 = int(input("Enter a No:"))
num2 = int(input("Enter a No:"))
num3 = int(input("Enter a No:"))

if(num1>num2):
    if(num1>num3):
        print(num1,"is Greatest")
    else:
        print(num3,"is Greatest")
else:
    if(num2>num3):
        print(num2,"is Greatest")
    else:
        print(num3,"is Greatest")
print("-----------")


#Short Hand If Else
print("Short Hand If Else")
print("Num1 is Greater") if(num1>num2) else print("Num2 is Greater")
print("-----------")

#Availability in List
print("Number is Available in List or Not")
list = []
list.append(num1)
list.append(num2)
list.append(num3)

if 33 in list:
    print("Available!")
else:
    print("Not Available!")
print("-----------")

#Voting Crieteria
print("Cheching if Your are eligible for voting or not")
age = int(input("Enter Your Age:"))
if age>1 and age<100:
    if age>18:
        print("You are Eligible for Voting!")
    else:
        print("You are not eligible.")
else:
    print("Sorry You cant")
print("-----------")
