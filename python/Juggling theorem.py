# input an array
arr = [1,2,3,4,5,6,7,8,9,10,11,12]
# calculate length of the array
N = len(arr)
# enter the number of left rotations
K = 6
# calculate gcd of N,K and divide the array into that many peices
# def gcd(N,K): #recursion to calculate gcd
# 	if (N%K == 0):
# 		return K
# 	return gcd(K, N%K)

# G = gcd(N,K)
if (N//2 >= K):
	for k in range(K):
		temp = arr[k]
		for n in range(K+k, N, K):
			arr[n-K] = arr[n]
		arr[N-K+k] = temp
	print(arr)
else:
	print('enter K < ' + str(N//2+1))