file1=input("Enter the payroll file name :")

fn1 = open(file1,'r')

content = fn1.readlines()

for i in range(0, len(content)):
    row = content[i].split()
    lastName = row[0]
    wages = float(row[1])
    hours = float(row[2])
    pay = wages * hours
    print("{: <10}{: <10.2f}{: <10.2f}{: <10.2f}".format(lastName,hours,wages, pay))

fn1.close()
