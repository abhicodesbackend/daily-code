'''
limit = 2000000

def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

sum = 0
count = 0
num = 2

while count != limit:
    if prime(num):
        sum += num
        count +=1
    num+=1
print(sum)
'''        
import sympy
print(sum(sympy.primerange(1,2000000)))
