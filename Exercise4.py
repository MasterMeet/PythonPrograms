# Pattern Printing
print("Enter Your Choice: ")
print("1-Forward\n2-Backward")
choice = int(input())

print("Enter The No of Row:- ")
n = int(input())

if choice == 1:
    for i in range(0, n):
        while j < n:
            print("*", end=" ")
            j += 1
        print(" ")

elif choice == 2:
    for i in range(0, n):
        j = 0

        while j <= i:
            print("*", end=" ")
            j += 1
        print(" ")

else:
    print("Invalid Choice!")