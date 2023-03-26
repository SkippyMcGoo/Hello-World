def printAll(seq, counter):
    if seq:
        print("Index", counter, seq[0])
        counter += 1
        printAll(seq[1:], counter)


newList = [1, 2, 3, 5, 6, 7]
printAll(newList, 0)

#While this program works as intended, printing out the given list in a sequence; 
#Recursive algorithms can be constly, and for a program like this, a for loop would do the job far more efficiently.  

