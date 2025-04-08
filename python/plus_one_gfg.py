def plus_one(numbers):

    numbers[-1] += 1
    
    for i in range(1,len(numbers)+1):
        
        if numbers[-i] > 9:

            numbers[-i] = 0
            numbers[-(i+1)] += 1

        if numbers[-len(numbers)] > 9:

            numbers.insert(0,1)
    
    return numbers

numbers = list(map(int, input('Enter number: ').split()))

print(plus_one(numbers))

