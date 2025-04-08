# importing random module
import random
# generate a random number in range 0 - 9
randomNum = random.randint(0,3)
# get a number input from user
print('You get 3 chances to guess the number...')
userInput = int(input('Guess the number in 0-9 (incusive): '))
# 3 trials for guessing the number 
for _ in range(2):
    # coditions to check the user input number with the random number
    if (userInput < randomNum):
        userInput = int(input(('Didn\'t match, guess big...:')))
    elif(userInput > randomNum): 
        userInput = int(input(('Didn\'t match, guess small...:')))
    elif (userInput == randomNum):
        print('You win...!')
        break
    else:
        print('This machine wins...!')
        break
# else clause if user fails to guess the number in 3 chances
else:
    if (userInput == randomNum):
        print('You win...!')
    else:
        print('This machine wins...!')
