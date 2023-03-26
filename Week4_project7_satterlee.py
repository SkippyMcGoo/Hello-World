salary = int(input('Enter the starting salary: $'))
annualIncrease = (float(input('Enter the annual % increase: ')) / 100)
years = int(input('Enter the number of years: '))
print('Year\tSalary')
print('--------------')
for year in range(1, years + 1):
    print(year,'\t',round(salary, 2))
    salary = salary + salary * annualIncrease


