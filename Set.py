print("-----------")
print("Set:-")
s = set([22,33,44,55])
print(type(s))
print(s)

#Set doesnt append existing values
s.add(11)
s.remove(11)
s.add(11)
print(s)
print(min(s))
s1= set([11,22])
print(s.union({11,22, 44}))
print(len(s))