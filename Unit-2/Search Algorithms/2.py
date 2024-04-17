lst = [1, 5, 15, 23, 45, 60, 75, 79, 83, 87, 95]
searchItem = int(input("Enter search number :"))

startPoint = 0
endPoint = len(lst) - 1
flag = True

while(startPoint <= endPoint):
    midPoint = (startPoint + endPoint) // 2
    if lst[midPoint] == searchItem:
        flag = False
        print(f"{searchItem} found on {midPoint + 1} position")
        break
    elif lst[midPoint] > searchItem:
        endPoint = midPoint - 1
    else:
        startPoint = midPoint + 1

if flag == True:
    print(f"{searchItem} not found")
