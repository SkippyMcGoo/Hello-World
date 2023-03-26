fileName = input("Enter the name of the file: ")
f = open(fileName, 'r')
lines = []
for line in f:
    lines.append(line)
LinePrint = int(input("Enter the line number you would like to view: "))
actVal = LinePrint - 1
print(lines[actVal])
