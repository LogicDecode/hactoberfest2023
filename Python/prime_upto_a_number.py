import math
num = int(input("Enter last digit upto which you want prime numbers : "))
numbers = []
for i in range(2, num+1):
	isPrime = True
	for j in range(2, math.ceil(i**0.5)):
		if i % j == 0:
			isPrime = False
			break
	if isPrime:
		numbers.append(i)

print(numbers)