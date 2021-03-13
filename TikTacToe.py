t = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}
i = 1

print("Available Choices:\n O\n X")
c = input("Enter Your Choice:-")
c = c.capitalize()

while i <= 9:
    print("---------------------------")
    print("|1|2|3|\n|4|5|6|\n|7|8|9|")

    print("Enter a Location for Input:-")
    n = int(input())
    t[n] = c

    print("---------------------------")
    print(f"|{t[1]}|{t[2]}|{t[3]}|\n"
          f"|{t[4]}|{t[5]}|{t[6]}|\n"
          f"|{t[7]}|{t[8]}|{t[9]}|")

    # Checking Conditions
    if (t[1] == t[2] == t[3] == c) or (t[1] == t[5] == t[9] == c) or (t[1] == t[4] == t[7] == c):
        print("You Won!")
        break

    elif t[2] == t[5] == t[8] == c:
        print("You Won!")
        break

    elif (t[3] == t[6] == t[9] == c) or (t[3] == t[5] == t[7] == c):
        print("You Won!")
        break

    elif t[4] == t[5] == t[6] == c:
        print("You Won!")
        break

    elif t[7] == t[8] == t[9] == c:
        print("You Won!")
        break

    else:
        pass

    i += 1
