strt_range = 2
end_range = 6 * 9**5

x = sum([i for i in range(strt_range, end_range) if i == sum(map(lambda i:i**5, list(map(int, [d for d in str(i)]))))])
print(x)

# The answer: 443839
