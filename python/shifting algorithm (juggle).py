# Juggling algorithm (optimised)

array = [1,2,3,4,5,6,7,8,9,10]
size = len(array)
shift = int(input())

if (shift <= size/2):
	for turn in range(shift):
		temp = array[turn]
		
		for index in range(shift+turn, size, shift):
			array[index-shift] = array[index]

		array[size-shift+turn] = temp

	print(array)

else:
	print(f'shift has to be any number less than {int(size/2) + 1}')

#time complexity: O(n)
#space complexity: O(1)