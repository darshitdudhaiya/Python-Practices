lst = [1, 5, 15, 23, 45, 60, 75, 79, 83, 87, 95]
searchItem = int(input("Enter search number :"))

startPoint = 0
endPoint = len(lst) - 1

def binarySearch(startPoint, endPoint, searchItem, lst):
    if startPoint <= endPoint:
        midPoint = (startPoint + endPoint) // 2 
        if lst[midPoint] == searchItem:
            print(f"{searchItem} found on {midPoint + 1} position")
        elif lst[midPoint] > searchItem:
            endPoint = midPoint - 1
            binarySearch(startPoint, endPoint, searchItem, lst)
        else:
            startPoint = midPoint + 1
            binarySearch(startPoint, endPoint, searchItem, lst)
    else:
        print(f"{searchItem} not found")

binarySearch(startPoint, endPoint, searchItem, lst)
