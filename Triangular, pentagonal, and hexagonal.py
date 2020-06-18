def is_pentagonal(n):
    pen_test = ((1 + 24 * n)**0.5 + 1)/6
    return pen_test == int(pen_test)

result = 0
i = 143
while True:
	i += 1
	result = 2*i**2-i
	if is_pentagonal(result): break

print(result)

# The answer: 1533776805
