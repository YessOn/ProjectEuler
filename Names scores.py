with open("names.txt", "rt") as f:
    names = sorted(list(eval(f.read())))

result = sum([sum([ord(i)-64 for i in j]) * (i+1) for i, j in enumerate(names)])

print(result)

# The answer: 871198282
