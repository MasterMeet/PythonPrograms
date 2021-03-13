print("-----------")
#Tupple (Immutable- Not Changeable)
print("Tupple:-")
tup = (1,22,33,"Hello")
print(tup)
#tup[1]= 40 does not supported in Tupple
print(tup[1])
print("-----------")

#List
print("List:-")
list = [10,30,5]
print(list)
list[2]= 25
print(list)
list.reverse()
print(list)
#list.append(50)
#list.sort()
list.insert(3,"Heey")
print(list)
print(list[0:3])
print(list.pop(0))
print(list[::-1])


