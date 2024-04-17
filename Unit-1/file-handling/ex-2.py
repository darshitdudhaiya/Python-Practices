f1 = open("a.txt", "r")
data = f1.readlines()
for x in data:
    print(x)
f1.close()
