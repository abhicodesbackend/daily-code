# def isPangram(text):

# 	pan = {}

# 	for letter in text:

# 		if letter not in pan and letter.isalpha():

# 			pan[letter] = 1

# 	return len(pan) == 26

# p = isPangram('abcdefghijklmnopqrstuvwxyz'.lower())
# print(p)

# # Time Complexity: O(n) need to check for punctuation marks, special characters and symbols
# # Space Complexity: O(26)

#  OPTIMAL SOLUTION

def isPangram(text):

	for i in range(97, 97+26):

		if text.find(chr(i)) == -1:
			return False

	else:
		return True

p = isPangram('abcdefghijklmnopqrstuvwxyz'.lower())
print(p)

# Time Complexity: O(26) need not bother about the special charcters or symbols
# Space Complexity: O(1)