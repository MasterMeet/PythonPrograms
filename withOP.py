
with open("file.txt","r+") as f:
    print(f.readlines())
    f.write("GP Rajkot")
    print(f.read())