sum=0
for n in range(1,1000):
    if(n%3==0 | n%5==0):
        sum=sum+n
print(sum)
