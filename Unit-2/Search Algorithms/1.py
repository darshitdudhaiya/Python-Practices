lst = [1, 5, 15, 23, 45, 60, 75, 79, 83, 87, 95]

searchItem = int(input("Enter seartch number :"))

count = 1
flag = True
for x in lst:
    if searchItem == x:
        print(f"{searchItem} is found on {count} position")
        flag = False
        break
    count += 1

if flag == True:
    print(f"{searchItem} not found")

