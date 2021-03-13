numbers = ["10","20","30","40","50"]

# for i in range(len(numbers)):
#     numbers[i]= int(numbers[i])
# numbers[3]+= 40
# print(numbers[3])

#Mapping Using Function
# def nint(a):
#     return int(a)
#
# num = list(map(nint,numbers))
# print(num)

#Mapping Using Lamda
num = list(map(lambda n:int(n),numbers))
print(num)