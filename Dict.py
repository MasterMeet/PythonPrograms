#dictionary
dict = {1:"JAva",4:"Python",7:"Android","c":"programming with c"}
print(dict[7])

#add item in dictonary
dict[5] = "C++"
print(dict)
dict.update({2:"PhP"})
print(dict)

w = "c"
print(dict[w])

del dict[7]
print(dict)