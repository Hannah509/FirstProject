import random
import sys
print ("minimum:0")
print ("maximum:50")
x = random.randint(1,50)
   # taking guessing number as input
guess = int(input("Guess a number:- ")) 
     
    # Condition testing
if x == guess:  
       print("Congratulations you did it in ")
       # Once guessed, loop will break 
elif x > guess:
       print("You guessed too small!")
elif x < guess:
       print("You Guessed too high!")