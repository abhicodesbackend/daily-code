d = {}
string = 'abhishekapece'

for i in string:

	if i in d:
		d[i] += 1
	else:
		d[i] = 1

print(d)
arr = []
for key in d:
	print(key)
	arr.append(key*d[key])

print(arr)
# pallindrome = [1,2,3]
# odd = 0
# index = 0

# # for key in d:
	
# # 	if (d[key]%2 == 1):

# # 		odd = 1
# # 		pallindrome.insert(key*d[key], i)

# pallindrome.insert(3)

# print(pallindrome)
