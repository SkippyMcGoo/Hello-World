import math

def EstimateSquareRoot(userInput, estimate = 1.0):
    tolerance = 0.000001

    estimate = (estimate + userInput /estimate ) / 2
    difference = abs(userInput - estimate ** 2)

    if difference <= tolerance:
        return estimate

    return EstimateSquareRoot(userInput, estimate)

while True:
    i = (input("Enter a positive number: "))
    if not i:
        print("Have a nice day: ")
        break
    else:
        newVar = float(i)
        RecursiveEstimate = EstimateSquareRoot(newVar)
        PythonApprox = math.sqrt(newVar)

        print("Recursive approximation: ", RecursiveEstimate)
        print("Python Approx: ", PythonApprox)
