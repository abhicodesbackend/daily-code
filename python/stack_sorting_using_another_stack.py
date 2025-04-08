'''
Sorting a stack using another stack (in ascending order)
'''

s1 = [8,6,4,2,5]
max = len(s1)
s2 = []
s2.append(s1.pop())
top = 0
c = 0
while (top < max):

    print(c+1 )

    if s1[-1] > s2[top]:
        temp = s2.pop()
        s2.append(s1.pop())
        s1.append(temp)
    
    else:
        s2.append(s1.pop())
        top += 1
