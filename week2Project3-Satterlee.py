newies = int(input("Please enter the number of new releases you would like to rent: "))
newiesTotal = newies * 3.00
oldies = int(input("Please enter the number of old releases you would like to rent: "))
oldieTotal = oldies * 2.00
rentalTotal = round(oldieTotal + newiesTotal)
print("your total rental price will be:", rentalTotal)
