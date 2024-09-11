import random as ra

#variables
num = ra.randint(0, 100)
guess = None
attempts = 1
diff = None
range = None


print('Welcome to the super fun number guessing extravaganza!')


while True:
    diff = input('To begin, please choose your difficulty: easy, medium, hard \n')
    if diff == 'easy':
        num = ra.randint(0, 10)
        range = '0 and 10'
        break
    elif diff == 'medium':
        num = ra.randint(0, 50)
        range = '0 and 50'
        break
    elif diff == 'hard':
        num = ra.randint(0, 100)
        range = '0 and 100'
        break
    else:
        print("That is not an acceptable response.\n")

while True:
    print("I'm thinking of a number between " + range +". Try to guess what it is!")
    try:
        guess = int(input())
        if guess == num:
            print('correct! It took you ' + str(attempts) + ' attempts!')
            break
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
    except:
            print("This input only accepts integers.")