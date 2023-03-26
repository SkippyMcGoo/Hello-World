iteration = int(input("Enter the number of iterations: "))
initSum = 0
div = 1
isPos = True
for i in range(iteration):
    initSum = initSum + 1 / div if isPos else initSum - 1 / div
    div += 2
    isPos = not isPos
result = initSum * 4
print(result)
        
