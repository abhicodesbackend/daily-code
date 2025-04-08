def gcd(a,b):
    if(b%a==0):
        return a
    return gcd(b%a, a)

a = int(input())
b = int(input())

print(gcd(a,b))

lcm = a*b/gcd(a,b)

print(lcm)