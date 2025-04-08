num = int(input()) # user input 

def Prime(num): # function to check prime
	for i in range(2,num//2):
		if(num%i == 0): # condition to check if the number is divisible by 2
			return 'not prime'
	return 'prime'

if (num < 0): # condition to check if the number is negative
	print('enter positive number: ')
	num = int(input())

print(Prime(num))