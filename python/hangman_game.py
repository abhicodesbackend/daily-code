# import random module for picking random words from the list
import random

# save some words for the hangman game before hand
words = ['computer', 'electronics', 'cycle', 'python', 'java', 'ruby', 'linux', 'programming', 'coding']

# pick a random word from the given list
word = random.choice(words)

print('Guess the characters: ')

# a variable to store all the user guessed characters
guesses = ''

# this could be anything, since the longest word here is of 11 characters. I took the guess turns to be 12
turns = 12

# while loop to run till the number of turns
while turns > 0:

	# a variable to check if user is guessing correct
	failed = 0

	# for loop to print the characters of the word guessed with blank underlined spaces, at every guess
	for char in word:

		# if guessed character is present in the random word, it prints it
		if char in guesses:
			print(char, end=' ')

		# if not it prints a underscore denoting the character is to be guessed
		else:
			print('_', end=' ')

		# at every wrong guess, this variable increments its value 
			failed += 1

	# just to put an extra blank line after every printing of the word sequence
	print()
	print()

	# if this variable checks if all the guesses are made right at the end of the word 
	if failed == 0:

		# prints the underlying statements
		print('You Win...!!')
		print(f'The word is...{word}')
		break

	# user input for each character
	guess = input('Guess a character: ')

	# every guessed character is appended into another variable
	guesses += guess

	# condition to check if guessed char is in the random word
	if guess not in word:

		# if char not in word, turns get reduced
		turns -= 1

		print('Wrong')

		print(f'You have {turns} left to guess the word')

		# when user runs out of all the turns, this prints
		if turns == 0:
			print('You Loose...')