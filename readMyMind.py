#Build a game that asks the user to think of a number and then gets the compute to get that number. 
#import the random module
import random
#write a function that accepts the high limit for guesses as a parameter
def readMyMind(x):
#declare the variables
    low = 1
    high = x
    feedback = ""
#ask the user for number within a certain range
    userNum = int(input(f"Enter a number between {low} and {high}. "))
#ask the computer to guess the users
    
    while feedback != "c":
        compGuess = random.randint(low,high)
    #tell the computer if their guess is too high, too low or correct and then adjust the range of possibilities accordingly.
        feedback = input(f"Is {compGuess}, too high(h), too low(l) or correct(c)?")
        if feedback == "l":
            low = compGuess + 1
            print(f"Computer, {compGuess} too low. Guess again.")
        elif feedback == "h":
            high = compGuess - 1
            print(f"Computer, {compGuess} is too high. Guess again.")
    print("f{compGuess} is correct!")
#call the function
readMyMind(100)
