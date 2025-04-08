import itertools

a = {'a', 'b', 'c', 'd'}
data = itertools.combinations(a,3)
x = list(data)
x.sort()
print(x)
print(''.join(x[0]))