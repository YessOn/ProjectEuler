import math
def is_prime(n):
	if n == 1: return False
	if n == 2: return True
	if n > 2 and n % 2 == 0: return False
	max_divisor = math.floor(math.sqrt(n))
	for d in range(3, 1+max_divisor, 2):
		if n % d == 0: return False
	return True

my_primes = filter(is_prime, [i for i in range(1, 104750)])

print(list(my_primes)[10000]) # index start by 0
# The answer: 104743
