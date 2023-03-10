#using DP

def fibonacci(n):
	a1 = 0
	a2 = 1
	if n < 0:
		print("Incorrect input")
	elif n == 0:
		return a1
	elif n == 1:
		return a2
	else:
		for i in range(2, n):
			a3 = a1 + a2
			a1 = a2
			a2 = a3
		return a3



print(fibonacci(10))

