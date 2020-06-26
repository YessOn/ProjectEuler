def is_bouncy(n): return str(n) != ''.join(sorted(str(n))) and str(n) != ''.join(sorted(str(n)))[::-1]
count = 0
i = 99
while count < 0.99 * i:
	i = i + 1
	if is_bouncy(i):
		count = count + 1
print(i)

# The answer: 1587000
