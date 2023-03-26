import math

def newtons(userInput):
    tolerance = 0.000001
    estimate = 1.0

    while True:
        estimate = (estimate + userInput /estimate ) / 2
        difference = abs(userInput - estimate ** 2)
        if difference <= tolerance:
            break
    return(estimate)

while True:
    i = (input("Enter a positive number: "))
    if not i:
        print("Have a nice day: ")
        break
    else:
        newVar = float(i)
        EstimateResult = newtons(newVar)
        PythonApprox = math.sqrt(newVar)
        print("Program approximation: ", EstimateResult)
        print("Python Approx: ", PythonApprox)

