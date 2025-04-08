
num = 2520

while True:
    for i in range(11,21):
        if (num%i)!=0:
            break
        if (i==20):
            print('The number is: ',num)
            break
    if (i==20):
        break
    num+=1

#The number is: 232792560
'''
def factors(num):
    while True:
        for i in range(11,21):
            if (num%i)!=0:
                break
            if (i==20):
                print(num)
                quit()
        num+=1
    return num
factor = factors(2520)
print(factor)
#the number is 232792560
'''
