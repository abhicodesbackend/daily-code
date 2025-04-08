x = int(input())
y = int(input())
num1 = x
num2 = y
if (x > y):
	y,x = x,y

while (True):
	r = y%x

	if (r ==0):
		hcf = x
		print('HCF:', x)
		break
	else:
		y = x
		x = r

lcm = int(hcf * num1/hcf * num2/hcf)
print('LCM:', lcm)