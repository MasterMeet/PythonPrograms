#Assignment Operator
print("Assignment Operator")
num1 = 85
num2 = 40
num1 += 15 # num1=num1 + 15
print(num1)

#Arithmetic Operator
print("-----------")
print("Arithmetic Operator")
print(f"{num1} + {num2} = {num1+num2}") # same as print(num1,"+",num2,"=",num1+num2)
print(f"{num1} - {num2} = {num1-num2}")
print(f"{num1} * {num2} = {num1*num2}")
print(f"{num1} / {num2} = {num1/num2}")
print(f"{num1} // {num2} = {num1//num2}")
print(f"{num1} % {num2} = {num1%num2}")

#Comparison Operator
print("-----------")
print("Comparison Operator")
print(f"{num1} == {num2} :- {num1==num2}")
print(f"{num1} != {num2} :- {num1!=num2}")
print(f"{num1} >= {num2} :- {num1>=num2}")
print(f"{num1} > {num2} :- {num1>num2}")
print(f"{num1} <= {num2} :- {num1<=num2}")
print(f"{num1} < {num2} :- {num1<num2}")

#Logical Operator
print("-----------")
print("Logical Operator")
print("And:-",num1>50 and num2>50)
print("Or:-",num1<50 or num1>30)
print("Not:-",not (num1==num2))

#Bitwise Operator
print("-----------")
print("Bitwise Operator")
print(0 & 1)
print(11 | 110)

#identity Operator
print("-----------")
print("Identity Operator")
print(num1 is num2)
print(num1 is not num2)

#membership Operator
print("-----------")
print("Membership Operator")
list = [10,20,3,55,34]
num = 20
print(f"{num} is available in List:- {20 in list}")