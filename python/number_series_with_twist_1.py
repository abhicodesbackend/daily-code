# 0 0 7 6 14 12 21 18 28... 

num = int(input())
odd_series = 0
even_series = 0

for i in range(3, num+1):
	if (i%2 != 0):
		odd_series += 7
		# print(odd_series, end = ' ')
	else: 
		even_series += 6
		# print(even_series, end = ' ')

# print()

if (num%2 == 0):
	print(even_series)
else:
	print(odd_series)