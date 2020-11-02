# dice code
import random
import sys

def roll(min, max):
    while True:
        print(random.randint(min, max))
        print(random.randint(min, max))
    sys.exit()
roll(1, 6)
