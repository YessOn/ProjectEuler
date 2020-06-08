def divisors(n):
    divisors = []
    for i in range(2, int(n**0.5)+1):
        q, r = divmod(n, i)
        if r == 0:
            if q >= i:
                divisors.append(i)
                if q > i:
                    divisors.append(n//i)
    return divisors

d = lambda n: 1 + sum(divisors(n))
result = 0
for a in range(1, 10000):
    if d(d(a)) == a and a != d(a):
        result += a
print(result)

# The answer: 31626
