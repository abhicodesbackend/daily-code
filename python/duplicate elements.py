array = [1,2,3,3,4,5,6,7,7,7,8,9,1,4,6]
items = dict.fromkeys(array, False)
duplicates = []
count = 1

print(f'original array: {array}')
for element in array:

	if items[element]:
		duplicates.append(element)
	else:
		items[element] = True

print(f'duplicates: {duplicates}')

print(f'array after duplicates removal: {list(set(array))}')