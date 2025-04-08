string = input('Enter a sentence: ').strip().split()

string[0], string[-1] = string[-1], string[0]

print(' '.join(string))