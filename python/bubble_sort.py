def bubbleSort(array): # ascending order

	n = len(array)

	for i in range(n):

		for j in range(i+1, n):

			if array[i] > array[j]:

				array[i], array[j] = array[j], array[i]

	return array

array = list(map(int, input().split()))

print(bubbleSort(array))

# Time complexity: O(n^2)
# Space complexity: O(1)
