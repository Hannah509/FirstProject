# dice code
import random
import sys

def roll(min, max):
    while True:
        print(random.randint(1, 6))
        print(random.randint(1, 6))
        sys.exit()

roll(1, 6)