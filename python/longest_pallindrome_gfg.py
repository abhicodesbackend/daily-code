def longestPallindrome(string):

	dup = {}

	if string == string[::-1]:
		return True

	for i in string: # to check the occurances of all the letters

		if i in dup:
			dup[i] += 1
		else:
			dup[i] = 1

	pallindrome = []
	max = 0
	ele = 0
	
	for key in dup:  # for maximum odd occurance insertion

		if (dup[key]%2 != 0 and max < dup[key]):

			max = dup[key]
			ele = key

	pallindrome.insert(len(pallindrome)//2, ele*max)

	for key in dup: # for all the even occurances insertion

		if (dup[key]%2 == 0):
			
			pallindrome.append(key*(dup[key]//2))
			pallindrome.insert(0, key*(dup[key]//2))

	return ''.join(pallindrome)  # convert list iterables into string

string = 'abcdedcba' # this is not a pallindrome

print(longestPallindrome(string.lower())) # convert all the letters to lower case