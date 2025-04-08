# def decToBin(dec_num):
#     return bin(dec_num).replace('0b', '')

# num = input('enter a decimal number: ')
# binary = decToBin(int(num))
# print(binary)

def binToDec(bin_num):
    return int(bin_num, 2)

num = input('enter a binary number: ')
decimal = binToDec(num)
exponent(decimal, len(num))

for exp in range(len(num), 0, -1):
    if(decimal%2**exp == 0):
        print(exp)
        break

