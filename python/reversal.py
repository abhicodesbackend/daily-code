# array reversal

string = list(input('Input string: '))
size = len(string)

for index in range(size//2):
	string[index], string[-index-1] = string[-index-1], string[index]	
	
print(''.join(string))

# time complexity: O(n/2)
# space complexity: O(1)

# # array reversal(optimised)

# array = list(input())
# print(reverse(array))