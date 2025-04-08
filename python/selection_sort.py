def selectionSort(array):

	n = len(array)
	min = 0

	for i in range(n):

		min = array[i]

		for j in range(i+1, n):

			if min > array[j]:

				min, array[j] = array[j], min
				#min = array[j]

		#min, array[i] = array[i], min
		array[i] = min

	return array

array = list(map(int, input().split()))

print(selectionSort(array))
