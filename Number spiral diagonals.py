n = res = 1
for k in range(2, 1001, 2):
    for j in range(4):
        n += k
        res += n
print(res)

# The answer: 669171001
