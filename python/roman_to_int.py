s = 'MCMXCIV'

Roman_dict   = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
Special_dict = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
num = 0
while s != '':
    for special in Special_dict.keys():
        if special in s:
            num += Special_dict[special]
            s = s.replace(special,'',1)
    for norm in Roman_dict.keys():
        if norm in s:
            num += Roman_dict[norm]
            s = s.replace(norm,'',1)

print(num)