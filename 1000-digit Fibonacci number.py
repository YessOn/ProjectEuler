a = 1
b = 1
index = 2
while len(str(b)) < 1000:
    a , b, index = b, a+b, index +1
print(index, " : ", a+b)

# The answer: 4782
