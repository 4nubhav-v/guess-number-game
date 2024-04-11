#guessing the game
import random
import sys
print('I am thinking of number between 1 and 20')
secretNum = random.randint(1,20)
guess = 0
while (True):
    guess = guess+1
    print('Take guess')
    guessNum = int(input())
    if (guessNum == secretNum):
        print('Good job! You guessed my number in '+ str(guess)+' guesses')
        sys.exit()
    elif (guessNum > secretNum):
        print('Your guess is too high')
        continue
    else:
        print('You guess is too low')
        continue
