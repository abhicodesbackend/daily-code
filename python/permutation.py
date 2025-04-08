def factorial(n):
		# fact = 1
		# for i in range(2,n+1):
		# 	fact *= i
		# if (n-1 == 1):
		# 	return fact
		#return factorial(n-1)
		fact = [i for i in range(1,n+1)]
		print(fact)
		return fact


n = int(input())
#r = int(input())

# permutation = factorial(n) / factorial(n-r)
# print(permutation)

print(factorial(n))