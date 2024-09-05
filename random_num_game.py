import random as ra

#variables
num = ra.randint(0, 10)
guess = None
attempts = 1

print("I'm thinking of a number between 0 and 10. Try to guess what it is!")
while guess != num :
    guess = int(input())
    if guess == num:
        print('correct! It took you ' + str(attempts) + ' attempts!')
    elif guess > num:
        print('lower!')
        attempts = attempts + 1
    else:
        print('higher!')
        attempts = attempts + 1