b = 1
while True:
	for i in range(1, 30):
		if (b % i != 0):
			break
		if i == 20:
			print(b)

	b += 1
# The answer: 232792560
