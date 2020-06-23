with open('triangle.txt', 'rt') as f:
	triangle = [[int(j) for j in i.split()] for i in f.read().split("\n")][::-1][1:]
def max_path_sum(triangle):
    for i in range(1, len(triangle)):
        for j, k in enumerate(triangle[i]): triangle[i][j] = k + max([triangle[i-1][j], triangle[i-1][j+1]])
    return triangle[-1][0]

print(max_path_sum(triangle))

# The answer: 7273
