arr = [1,2,3,4,5,6,7,8,9,10] # input array

print(f'Original array:{arr}') # print the array

n = len(arr) # calculate array length

k = n//2 # calculate half of the length and take its quotient

for i in range(k): # logic for array reversal
	
	arr[i], arr[n-1-i] = arr[n-1-i], arr[i] # swap the terminal elements

print(f'Reversed array:{arr}'# print the reversed array

#time complexity: O(floor(len(array)/2))
#space complexity: O(1)