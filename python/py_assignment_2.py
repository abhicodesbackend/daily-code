x=0
y=1
add = 0
for num in range(100):
    p=x+y
    x=y
    y=p
    if (p%2==0):
        add += p
        if (add > 4000000):
            add -= p
            break
print('Sum: ',add)

    


