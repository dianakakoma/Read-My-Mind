#Build a game that asks the user to think of a number and then gets the compute to get that number. 
#import the random module
import random
#write a function that accepts the high limit for guesses as a parameter
def readMyMind(x):
#declare the variables
    low = 1
    high = x
    compGuess = 0
#ask the user for number within a certain range
    userNum = int(input(f"Enter a number between{low} and {high} "))
#ask the computer to guess the users
    compGuess = random.randint(low,x)
#tell the computer if their guess is too high, too low or correct and then adjust the range of possibilities accordingly.

#call the function
readMyMind(100)
