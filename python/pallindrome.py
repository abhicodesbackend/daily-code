def checkPallindrome(string):
	for i in range(len(string)//2):
		if (string[i] != string[len(string)-i-1]):
			return 'not pallindrome...'
	else:
		return 'pallindrome...'

word = input()
print(checkPallindrome(word))