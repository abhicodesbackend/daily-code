data = '''Hello!, this is text for the file1
and this data would be used for further calculations...
		'''

# file can be created with any extensions
with open('file1.csv', 'w') as fp: # to write data into the file
	fp.write(data)

with open('file1.txt', 'r') as fp:  # to read data from the file
	d = fp.read()

# print(d)

with open('file1.txt', 'a') as fp: # to append the data into file
	fp.write(data)

with open('file1.txt', 'r') as fp:
	d = fp.read()

# print(d)	

fp = open('file1.csv', 'r')  # even this way can be used to perform file operations
print(fp.read())