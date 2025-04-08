List = ["flower","flow","flight"]

def lcp(List):
	# limit = min(list(map(len, List)))
	        
	prefix = ''
	p = ''

	flag = 0

	for i in range(len(List[0])):

	    word = List[0]

	    p = word[0:i+1]

	    for item in List:
	        if (not item.startswith(p)):
	            return prefix

	    prefix = p

	return prefix

print(lcp(List))