a = 'Jordan was born on 12-05-1999 and she was born on 6-05-1999 although they separated on 15-08-2015'
b = a.split()

years = []

for element in b:

	if(not element.isalpha()):
		element = element.replace('-',' ').split()
		#print(element, end = ' ')
		years.append(element[-1])

print(len(set(years)))

