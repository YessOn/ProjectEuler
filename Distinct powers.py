# for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100
terms = len(set([a**b for a in range(2, 101) for b in range(2, 101)]))
print(terms)
# The answer: 9183
