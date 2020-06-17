def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return set(factors)

nums = [i  for i in range(1, 200000)]
for i in range(len(nums)):
	if len(prime_factors(nums[i])) == 4 and len(prime_factors(nums[i+1])) == 4 and len(prime_factors(nums[i+2])) == 4 and len(prime_factors(nums[i+3])) == 4:
		print(i+1, i+2, i+3, i+4)

# The answer: 134043 134044 134045 134046
