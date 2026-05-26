a = int(input())
b=int(input())
count = 0
for num in range (a,b+1):
	if num > 1:
		is_prime = True
		for i in range (2 ,num):
			if num % i == 0:
				is_prime = False
				break
		if is_prime:
			print(num)
			count+=1
if count==0:
	print("No primes")
