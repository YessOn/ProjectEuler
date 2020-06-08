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

def is_abundant(n):
    return sum(divisors(n))+1 > n

abundants = [i for i in range(2, 28124) if is_abundant(i)]

my_sums = {0} # If it is left empty it would be a type of dict
# we used the concept of sets here to avoid deleting duplicates
for i in range(len(abundants)):
    for j in range(i, len(abundants)):
        my_sum = abundants[i] + abundants[j]
        if my_sum > 28123:
            break
        my_sums.add(my_sum)


result = (28123*28124)//2 - sum(my_sums)
print(result)

# The answer: 4179871
