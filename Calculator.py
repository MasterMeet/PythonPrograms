#Calculator accept two number as input and one operator  

def calculator():
    num1 = int(input("Enter a No:- "))
    op = input("Enter The Operator: ")
    num2 = int(input("Enter a No:- "))

    print("-----------")
    print(f"{num1} {op} {num2} =",end=" ") #end=" " prevent cursor from moving to next line

    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    elif op == "%":
        print(num1 % num2)
    elif op == "//":
        print(num1 // num2) 
    else:
        print("Invalid Operator!")

calculator()
