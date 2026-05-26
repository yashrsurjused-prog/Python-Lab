def sum_of_digits_recursive(n):
	n = int(n)
	if n==0:
		return 0
	# Write your code here
	
	return (n % 10) +     sum_of_digits_recursive(  n // 10 )


number = input()

result = sum_of_digits_recursive(number)	
print(result)

	
