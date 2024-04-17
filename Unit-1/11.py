x = [1, 2, 3, 4, 5, 6]


# map(function, collection)
# filter(function, collection)

def functionForMap(i):
    return (i, i*2)


mappedList = map(functionForMap, x)
print(list(mappedList))

def functionForFilter(x):
    if x % 2 != 0:
        return True
    else:
        return False

filteredList = dict(filter(functionForFilter, x))
print(filteredList)

