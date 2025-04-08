def checkNiven(n):
	s = 0
	for i in str(n):
		print(i)
		s += int(i)
	if n%s:
		return 0
	else:
		return n//s
	

print(checkNiven(57))