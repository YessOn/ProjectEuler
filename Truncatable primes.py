def is_prime(n):
    if n == 1: return False
    if n == 2: return True
    elif n%2 == 0: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0: return False
    return True

def is_right_truncable(a): return all([is_prime(int(str(a)[:len(str(a))-i])) for i in range(0, len(str(a)))])
def is_left_truncable(a): return all([is_prime(int(str(a)[i:])) for i in range(0, len(str(a)))])

st_eleven = []

i = 23
while len(st_ele) < 11:
	if is_left_truncable(i) and is_right_truncable(i):
		st_ele.append(i)
	i += 1

print(sum(st_eleven))

# The answer: 748317
