from math import factorial as fct
def combin(i): return fct(i[1])//(fct(i[0])*fct(i[1]-i[0]))

x = len(list(filter(lambda i: combin(i) > 10**6, [(i, j) for i in range(1, 101) for j in range(i, 101)])))

print(x)

# The answer: 4075
