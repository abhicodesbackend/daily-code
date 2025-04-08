# 1 1 2 3 4 9 8 27 16 81 32 243 64 729 128 2187 ...

n = int(input())

even_series = 1
odd_series = 1

for i in range(1, n+1):
	if (i%2 == 0):
		odd_series *= 3
	else: 
		even_series *= 2

if (n%2 == 0):
	print(odd_series//3)
else:
	print(even_series//2)