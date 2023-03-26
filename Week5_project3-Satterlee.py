import random
import math
lowerBound = int(input("Please enter the lower bound of guesses: "))
upperBound = int(input("Please enter the upper bound of guesses: "))
correctNum = int(input("Pleae enter a number for the computer to guess: "))
maxGuess = math.log(upperBound - lowerBound + 1)
maxGuess = round(maxGuess)
guessNum = 0
correctGuess = False
while (guessNum < maxGuess):
    guessNum += 1
    playerTrust = False
    computerGuess = random.randint(lowerBound, upperBound)
    print("I guess the number is", computerGuess)

    while playerTrust == False:
        winCheck = int(input("Please enter 1 if my guess is correct\n 2 if the correct number is lower than my guess\n and 3 if the correct number is higher than my guess: "))

        if winCheck == 1:
            if computerGuess == correctNum:
                print("ha ha, I guessed the correct number in", guessNum, "guess(es)")
                playerTrust = True
                correctGuess = True
            else:
                print("Don't lie, tell me the truth! ")
        if winCheck == 2:
            if correctNum < computerGuess:
                upperBound = computerGuess - 1
                playerTrust = True
            else:
                playerTrust = False
                print("Don't lie, tell me the truth! ")
        if winCheck == 3:
            if correctNum > computerGuess:
                playerTrust = True
                lowerBound = computerGuess + 1
            else:
                playerTrust = False
                print("Don't lie, tell me the truth! ")
            
    if correctGuess == True:
        break

if correctGuess == False:
    print("You win.... this time")
        
print("End")

    
