def calculate(a, b, op):
	switch_case = {'+': a+b, # addition
				   '-': a-b, # subtraction
				   '*': a*b, # multiplication
				   '/': a/b, # division
				   '%': a%b, # modulo
				   '**': a**b } # exponentiation
	print(switch_case[op])


num1 = 2
num2 = 2
operator = '**'
calculate(num1, num2, operator)
