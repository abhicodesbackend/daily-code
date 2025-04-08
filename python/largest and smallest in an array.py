array = [8,5,9,2,7,2,1,4,8,10,82,74,0,-1,56,-10,-100]
largest, smallest = array[0], array[0]
for index in range(len(array)):
	if array[index] > largest:
		largest = array[index]
	if array[index] < smallest:
		smallest = array[index]

print(f'largest:{largest}, smallest:{smallest}')