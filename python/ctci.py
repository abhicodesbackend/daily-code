# MODERATE

#16.1 Number Swapping
# def swap(a,b):
# 	a = a+b
# 	b = a-b
# 	a = a-b
# 	return a,b

# print(swap(1,2))

#16.2 Word Frequencies
# def freqCheck(words):
# 	freq = {}
# 	for word in words:
# 		if word.lower() in freq:
# 			freq[word.lower()] += 1
# 		else:
# 			freq[word.lower()] = 1
# 	return freq

# words = input().split()
# print(freqCheck(words))

#16.3 Intersection
#a(x,y), b(p,q)
# A = input().split()
# A = list(range(int(A[0]), int(A[1])+1))
# B = input().split()
# B = list(range(int(B[0]), int(B[1])+1))
# for a in A:
# 	if a in B:
# 		print(a, end=' ')
# else:
# 	print('No Intersection')

# n = int(input())
# prime = list(range(n+1))
# p = 2

# while p*p < n:

# 	for i in range(p,n):

# 		if (p*i > n):
# 			break
# 		prime[p*i] = False

# 	p += 1

# for i in range(2,n+1):
# 	if prime[i]:
# 		print(prime[i], end = ' ') 
# print()
# prime = prime[2:]
# print(prime)
# arr = list(filter(bool, prime))
# print(arr)

# n = int(input())

# for num in range(2,n+1):

# 	flag = 0

# 	for i in range(2,num):

# 		if (num%i == 0):

# 			flag = 1
# 			break

# 	if (flag==0):
# 		print(num)