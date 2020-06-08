def cycle_len(n):
    r = 10
    i = 0
    while r != 10 or i < 1:
        r = (r % n) * 10
        i += 1
    return i

l = 0
for i in range(2, 1000):
    if i%2 != 0 and i%5 != 0:
        lenn = cycle_len(i)
        if lenn > l:
            l = lenn
            result = i
print(result)

# The answer: 983
