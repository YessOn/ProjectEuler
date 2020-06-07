import math
n = 20
# it's more like the number of possible combinations n routes of 2n times.
res = math.factorial(2*n)//math.factorial(n)**2
print(res)

# The answer: 137846528820
