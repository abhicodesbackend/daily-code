# Seive of Eratosthenes

# original sieve

n = 5
prime = list(range(n+1))
p = 2

while p*p < n:

    if(prime[p]):

        for i in range(p,n):
            if(p*i > n):
                break
            prime[p*i] = False
    
    p += 1

for i in prime:
    if i and not i==1:
        print(i, end=' ')

# optimised sieve

# import math
# n = 100
# prime = list(range(n+1))
# p = 2
# count = 0
# while p < math.sqrt(n):

#     if prime[p]:

#         for i in range(p,n//2):
#             count += 1
#             if(p*i > n):
#                 break
            
#             prime[p*i] = False
    
#     p += 1

# for i in prime:
#     if i and not i==1:
#         print(i, end = ' ')
#         count += 1

# print(f'count: {count}')

# # print()
# # num = int(input('Enter number to check if prime: '))
# # if(num in prime):
# #     print('it is prime')
# # else:
# #     print('it isn\'t prime')