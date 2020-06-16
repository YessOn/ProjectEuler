#Method1:
from math import fct as fct

fcts = [fct(0), fct(1), fct(2), fct(3), fct(4), fct(5), fct(6), fct(7), fct(8), fct(9)]
def fct_digits(n):
	s = 0
	while n:
		s += fcts[n%10]
		n //= 10
	return s

res = 0
for i in range(10,1854721):
	if fct_digits(i) == i: res += i
print(res)

#Method2:
strt_range = 10
end_range = 1854721
x = sum([i for i in range(strt_range, end_range) if i == sum(map(fct, list(map(int, [d for d in str(i)]))))])
print(x)

# The answer: 40730
