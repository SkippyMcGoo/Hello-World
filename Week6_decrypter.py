message = input("Enter the encrypted message: ")
distanceVal = int(input("Please enter the distance value: "))
result = ""

for i in message:
    result += chr(ord(i)-distanceVal)
print(result)
