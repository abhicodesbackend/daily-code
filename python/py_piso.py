import time
datadec = int(input('enter decimal value: '))
databin = bin(datadec)
print(databin)
i = 0
"""
clock = 0
while True:
    clock = ~(clock)
    time.sleep(1)
    if (clock == 1 & i != len(data)):
        print(data[i])
        i = i + 1
"""
for i in range(0,len(databin)):
    time.sleep(0.5)
    print(databin[i])






