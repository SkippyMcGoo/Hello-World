mainFile=input("Enter the name of the first file: ")
copyFile=input("Enter the name of the second file: ")
 
f1 = open(mainFile, 'r') 


f2 = open(copyFile, 'w') 


cont = f1.readlines() 

for i in range(0, len(cont)):
    f2.write(cont[i]) 


f2.close() 
print("The file has been copied")

