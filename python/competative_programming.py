'''
#input=7
#output=1 3 5 7 9 11 13

#n = int(input())
n=7
for i in range(1,n*2,2):
	print(i,end=' ')
'''

'''
#input=7
#output=7 6 5 4 3 2 1

#n = int(input())
n=7
for i in range(n,0,-1):
	print(i,end=' ')
'''

'''
#input=7
#output=1 2 3 4 5 6 7

#n = int(input())
n=7
for i in range(1,n+1):
	print(i,end=' ')
'''

'''
#input=5
#output= * * * * *
		#* * * * *
		#* * * * *
		#* * * * *
		#* * * * *

#n=int(input())
n=5
for i in range(n):
	for j in range(n):
		print('*',end=' ')
	print()
'''

'''
#input=5
#output= Aa
		#Bb
		#Cc
		#Dd
		#Ee

#n = int(input())
n = 5
for i in range(n):
	print(chr(65+i),end='')
	print(chr(97+i))
'''

'''
#input=5
#output= Aa
		#bB
		#Cc
		#dD
		#Ee

#n = int(input())
n = 5
x,y=65,97
for i in range(n):
	print(chr(x+i),end='')
	print(chr(y+i))
	x,y=y,x
'''

'''
#input=4
#output= A B C = C B A

#n = int(input())
n=4
for i in range(n-1):
	print(chr(65+i),end=' ')
print('=',end=' ')
for i in range(1,n):
	print(chr(65+n-1-i),end=' ')
'''

'''
#input=4
#output=A B C D C B A

n=4
for i in range(n):
	print(chr(65+i),end=' ')
for i in range(1,n):
	print(chr(65+n-1-i),end=' ')
'''

'''
#input=4
#output=1 2 3 4 3 2 1

n=4
for i in range(1,n):
	print(i,end=' ')
for i in range(n,0,-1):
	print(i,end=' ')
'''

'''
#input=3
#output=3 2 1 0 1 2 3

n=3
for i in range(n,0,-1):
	print(i,end=' ')
for i in range(n+1):
	print(i,end=' ')
'''

'''
#input=3
#output=-3 -2 -1 0 1 2 3

n=3
for i in range(-n,n+1,1):
	print(i,end=' ')
'''

'''
#input=9
#output=1 -9 2 -8 3 -7 4 -6 5

n=9
for i in range(n-5):
	print(i+1,end=' ')
	print(-n+i,end=' ')
print(i+2)
'''

'''
#input=10
#output=1 * A 2 * B 3 * C 4

n=10
for i in range(n-7):
	print(i+1,end=' ')
	print('*',end=' ')
	print(chr(65+i),end=' ')
print(n-6)
'''

'''
#input=7
#output=1 A 3 B 5 C 7

n=7
for i in range(1,n+1):
	if (i%2==1):
		print(i,end=' ')
	else:
		print(chr(64+i//2),end=' ')
'''

'''
#input=7
#output=A Z C X E V G

n=7
for i in range(n):
	if (i%2==0):
		print(chr(65+i),end=' ')
	else:
		print(chr(90-(i//2)),end=' ')
'''

'''
#input=7
#output=A b C d E f G

n=7
for i in range(n):
	if (i%2==0):
		print(chr(65+i),end=' ')
	else:
		print(chr(97+i),end=' ')
'''

'''
#input=7
#output=Aa Bb Cc Dd Ee Ff Gg

n=7
for i in range(n):
	print(chr(65+i)+chr(97+i),end=' ')
'''

'''
#input=7
#output=T U V W X Y Z

n=7
for i in range(n):
	print(chr(65+26-7+i),end=' ')
'''

'''
#input=7
#output=Z Y X W V U T

n=7
for i in range(n):
	print(chr(65+25-i),end=' ')
'''

'''
#input=7
#output=G F E D C B A

n=7
for i in range(n):
	print(chr(64+n-i),end=' ')
'''

'''
#input=7
#output=A B C D E F G

n=7
for i in range(n):
	print(chr(65+i),end=' ')
'''


#input=7
#output=* # @ * % @ *

n=7
for i in range(1,n+1):
	if(i%3==1):
		print('*',end=' ')
	elif(i%3==2):
		print(chr(35-i//3),end=' ')    #64 @
	else:							#35 #
		print(chr(64),end=' ')	#37 %

