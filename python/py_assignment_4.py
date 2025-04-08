prod = 1
pallindrome = []
m_value = []
n_value = []
for m in range(100,1000):
    for n in range(100,1000):
        x = 0
        prod = m*n
        num = str(prod)
        if (prod > 900000):
            for i in range(0,len(num)):
                if (num[i]==num[len(num)-1-i]):
                    x+=1
                if (x==6):
                    pallindrome.append(prod)
                    m_value.append(m)
                    n_value.append(n)

print('pallindrome number:',pallindrome)
print('m_values:',m_value)
print('n_values:',n_value)


