a = int(input())
b = int(input())

def hcf(a,b):
	if a==0:
		return b;
	return hcf(b%a, a)

print('HCF:', hcf(a,b))

hcf = hcf(a,b)

def lcm(a, b, hcf):
	return(a*b/hcf)

print('LCM:', lcm(a,b,hcf))