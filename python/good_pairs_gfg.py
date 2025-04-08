def goodPairs(arr):

	pairs = {}

	for key in arr:

		if key in pairs:
			pairs[key] += 1
		else:
			pairs[key] = 0

	return sum(pairs.values())


arr = [2, 1, 4, 5, 2, 3, 7, 4, 1, 5]

print(goodPairs(arr))

#Time Complexity: O(n)
#Space Complexity: O(distinct elements in array)