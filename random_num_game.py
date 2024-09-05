import random as ra

#variables
num = ra.randint(0, 100)
guess = None
attempts = 1
diff = None

print('Welcome to the super fun number guessing extravaganza!')
print('to begin, please choose your difficulty: easy, medium, hard')
diff = input()

if diff == 'easy':
    num = ra.randint(0, 10)
elif diff == 'medium':
    num = ra.randint(0, 50)
else:
    num = ra.randint(0, 100)

print("I'm thinking of a number. Try to guess what it is!")
while guess != num:
    guess = int(input())
    if guess == num:
        print('correct! It took you ' + str(attempts) + ' attempts!')
    elif guess > (num + 10):
        print('much lower!')
        attempts = attempts + 1
    elif guess > num:
        print('a little lower')
        attempts = attempts + 1
    elif guess < (num - 10):
        print('much higher!')
        attempts = attempts + 1
    else:
        print('a little higher!')
        attempts = attempts + 1
