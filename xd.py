def dividingChocolate(n, chocolates):
    for i in range (1,10000):
        if (i % 2 == 1):
            m = i
            print(m)

    
    if n == m:
        return False
    else:
        return True

def main():
    t = int(input().strip())

    for i in range(t):
        n = int(input().strip())
        chocolates = list(map(int,input().strip().split(' ')))
        dividable = dividingChocolate(n, chocolates)

        if dividable:
            print("Yes")
        else:
            print("No")

if __name__ ==" __main__":
    main()
