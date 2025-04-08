'''
two words are said to be ANAGRAM, if both the words share same number of occurances
regardless their occurances
'''

def isAnagram(word1, word2):

	dict1, dict2 = {}, {}

	for key1 in word1:

		if key1 in dict1:
			dict1[key1] += 1
		else:
			dict1[key1] = 1

	for key2 in word2:
		if key2 in dict2:
			dict2[key2] += 1
		else:
			dict2[key2] = 1

	return dict1 == dict2


word1 = input()
word2 = input()

print(isAnagram(word1, word2))