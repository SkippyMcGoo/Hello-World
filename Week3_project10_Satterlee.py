hourlyWage = float(input("Enter the hourly wage: "))
regHours = float(input("Enter regular hours: "))
over = float(input("Enter overtime hours: "))
regPay = hourlyWage * regHours
overtimePay = over * (1.5 * hourlyWage)
weeklyPay = round(overtimePay + regPay, 2)
print("The weekly pay is $" + str(weeklyPay))
