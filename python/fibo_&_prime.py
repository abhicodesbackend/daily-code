# 1 2 1 3 2 5 3 7 5 11 8 13 13 ...

n = int(input())

first = 0
second = 1
notPrime = False
prime = 2

for i in range(3,n+1):

	if (i%2 != 0):
	# odd series fibonacci
		fibo = first + second
		first = second
		second = fibo
	else:
		while (True):
			for k in range(2,prime+1):
				if(prime != k):
					if ((prime+1)%k == 0):
						notPrime = True
						break
			if (notPrime == False):
				break
			prime += 1

if (n%2 != 0):
	print(fibo)
else:
	print(prime)

