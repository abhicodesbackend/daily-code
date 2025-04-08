#import necessary modules
from tkinter import *
from tkinter import simpledialog
import random

# user defined function run the guessing game driver code
def guessNumber():
    # generate a random number in range 0 - 9
    randomNum = random.randint(0,9)
    # get a number input from user
    print('You get 3 chances to guess the number...')
    #userInput = int(input('Guess the number in 0-9 (incusive): '))
    userInput = simpledialog.askinteger('Guess the number...', 'Guess the number in 0-9 (incusive): ')
    # 3 trials for guessing the number 
    for _ in range(2):
        # coditions to check the user input number with the random number
        if (userInput < randomNum):
            #userInput = int(input(('Didn\'t match, guess big...:')))
            userInput = simpledialog.askinteger('Guess the number...', 'Didn\'t match, guess big...:')
        elif(userInput > randomNum): 
            #userInput = int(input(('Didn\'t match, guess small...:')))
            userInput = simpledialog.askinteger('Guess the number...', 'Didn\'t match, guess small...:')
        elif (userInput == randomNum):
            #print('You win...! \nThanks for playing...')
            l1 = Label(root, text='You win...! Thanks for playing...', font='Times 15 bold')
            l1.grid(row=4, column=1)
            break
        else:
            #print('This machine wins...! \nSorry, thanks for playing...')
            l2 = Label(root, text='This machine wins...! Sorry, thanks for playing...', font='Times 15 bold')
            l2.grid(row=4, column=1)
            break
    # else clause if user fails to guess the number in 3 chances
    else:
        if (userInput == randomNum):
            #print('You win...! \nThanks for playing...')
            l1 = Label(root, text='You win...! Thanks for playing...', font='Times 15 bold')
            l1.grid(row=4, column=1)
        else:
            #print('This machine wins...! \nSorry, thanks for playing...')
            l2 = Label(root, text='This machine wins...! Sorry, thanks for playing...', font='Times 15 bold')
            l2.grid(row=4, column=1)
    #root.quit()

# creating GUI home window
root = Tk()
# add title to home window
root.title('Guess the number...')
# adjust it's geometry
#root.geometry('300x150')
# add buttons
b1 = Button(root, text='Play!', command=guessNumber, font='Times 16 bold', borderwidth=2, relief='groove', activebackground='grey')
b1.grid(row=2, column=1)
b2 = Button(root, text='Close', command=root.quit, font='Times 16 bold', borderwidth=2, relief='groove', activebackground='grey')
b2.grid(row=2, column=2)

root.mainloop()