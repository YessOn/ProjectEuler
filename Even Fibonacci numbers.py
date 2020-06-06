from functools import lru_cache
@lru_cache(maxsize=128)
def fibonacci(n):
	if n == 1:
		return 1
	elif n == 2:
		return 1
	elif n > 2:
		return fibonacci(n-1) + fibonacci(n-2)
# Quick Search: The term in the Fibonacci sequence whose values do not exceed four million is the 34th equals to 5702887

print(sum([fibonacci(i) for i in range(1, 35) if fibonacci(i) % 2 ==0]))

# The answer is 4613732
