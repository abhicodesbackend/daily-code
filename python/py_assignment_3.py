number = 12

divisor = 2

while divisor*divisor < number:
    while number % divisor == 0:
        number = int(number / divisor)
    divisor += 1

print(number)
