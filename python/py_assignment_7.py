'''
num = 2
prime = []
while True:
    for i in range(2,num):
        if (num%i)==0:
            break
        if (num == i+1):
            prime.append(num)
    num+=1
    if (len(prime)==10001):
        break

print(prime[10000])
'''
import sympy
print(sympy.prime(10001))
        
