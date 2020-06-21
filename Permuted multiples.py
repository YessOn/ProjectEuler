def checker(x):
	return sorted(list(str(x))) == sorted(list(str(2*x))) and sorted(list(str(x))) == sorted(list(str(3*x))) and sorted(list(str(x))) == sorted(list(str(4*x))) and sorted(list(str(x))) == sorted(list(str(5*x))) and sorted(list(str(x))) == sorted(list(str(6*x)))

run = True
i = 1
while run:
	if checker(i):
		print(i)
		run = False
		break
	i += 1

# The answer: 142857
