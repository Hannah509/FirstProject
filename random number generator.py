import random
print ("minimum:0")
print ("maximum:50")
x = random.randint(1,50)
guess=x + 1

while guess != x:
    # taking guessing number as input
    guess = int(input("Guess a number:- "))  
        # Condition testing
    if x == guess:  
        print("Congratulations you did it!")
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You guessed too high!")
