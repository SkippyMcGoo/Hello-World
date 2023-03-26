def average(lst):
    avg = sum(lst) / len(lst)
    return avg


fileName = input("Please enter a filename: ")

f = open(fileName, "r")

data = f.read()

stringList = data.split("\n")
intList = [eval(i) for i in stringList]

average(intList)
print("The average of the values in the file is:", average(intList))
f.close()


