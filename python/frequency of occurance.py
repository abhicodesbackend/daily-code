# program to check the occurance of the numbers

num = [1,2,5,1,2,2,6,7,1,3,9]
freq = {}  # can use both the methods to declare a dictionary
#freq = dict()

for i in num:
    if (i not in freq):
        freq[i] = 1 # can use both the elements to add items into the dictionary
        #freq.update([(i,1)])                
    else:
        freq[i] += 1

print(f'Frequencies are: {freq}')

distinct = []

for k,v in freq.items():
    if v == 1:
        distinct.append(k)
    
print(f'Distinct elements are: {distinct}')



