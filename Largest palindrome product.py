def palindromic_3x(n, p):
	my_list = [i*j for i in range(n, p) for j in range(n, p)]
	pal = []
	for i in my_list:
		if len(str(i)) == 5:
			if str(i)[0] == str(i)[-1] and str(i)[1] == str(i)[-2]:
				pal.append(i)
		if len(str(i)) == 6:
			if str(i)[0] == str(i)[-1] and str(i)[1] == str(i)[-2] and str(i)[2] == str(i)[-3]:
				pal.append(i)
	return pal

print(max(palindromic_3x(100, 1000)))
# The answer: 906609
