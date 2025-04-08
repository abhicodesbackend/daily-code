n = int(input("enter n: "))
arr = list(map(int, input().split()))

sum = (n*(n+1))//2


for i in arr:

	sum = sum - i
	

print('missing number: ', sum)