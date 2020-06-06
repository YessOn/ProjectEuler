sum_of_squares_of_100 = sum([i**2 for i in range(101)])
square_of_sums_of_100 = sum([i for i in range(101)])**2
dx = square_of_sums_of_100 - sum_of_squares_of_100
print(dx)

# The answer: 25164150
