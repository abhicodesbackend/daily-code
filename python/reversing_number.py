# reverse a number

# num = input().strip()

# x = int(num)

# if x > 0:

# 	num = num[::-1]
# 	x = int(num)
# 	print(x)

# else:

# 	num = str(abs(int(num)))
# 	num = '-' + num[::-1]
# 	x = int(num)
# 	print(x)


num = input().strip()
x = int(num)
if x > 0:
	num = []
	while x!=0:
		num.append(str(x%10))
		x = x//10

	print(int(''.join(num)))
else:
	num = []
	x = abs(x)
	while x!=0:
		num.append(str(x%10))
		x = x//10

	num.insert(0, '-')
	print(int(''.join(num)))