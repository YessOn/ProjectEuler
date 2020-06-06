n = 1000
for a in range(1, n):
	for b in range(1, n):
		for c in range(1, n):
			if c**2 == a**2 + b**2 and a+b+c == 1000:
				print(a, b, c)
				print(a*b*c)
print("Done!")
# (a, b, c)= (200, 375, 425)
# The answer: 31875000
