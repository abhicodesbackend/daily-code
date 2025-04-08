x=0
y=1
fibonacci = []
pisano = []
for num in range(100):
    p=x+y
    x=y
    y=p
    #q=p%5
    fibonacci.append(p)
    #pisano.append(q)
print(fibonacci)
#print(pisano)

    
