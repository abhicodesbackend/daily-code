def firstNonOccurance(s):
	
	for i in s:
		if s.count(i) == 1:
			return i

	return None


s = 'this is a string which contains some alphabets'

print(firstNonOccurance(s))

# Time Complexity: O(k), where k is the position of first non occurance alphabet
# Space Complexity: O(1)
