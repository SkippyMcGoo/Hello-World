def isSorted(lst): 
    sortedList = lst[:]
    sortedList.sort()

    if (lst == sortedList):
        return True
    else:
        return False

newList = [1, 2, 5, 4, 5]
print(isSorted(newList))
