def is_subsequence(str2, str1):

    ptr1 = 0; ptr2 = 0

    while ptr1 < len(str1) and ptr2 < len(str2):

        if (str1[ptr1] == str2[ptr2]):

            ptr2 += 1
        
        ptr1 += 1
    
    return ptr2 == len(str2)

str1 = input('Enter main string: ').strip()
str2 = input('Enter substring: ').strip()

print(is_subsequence(str2, str1))