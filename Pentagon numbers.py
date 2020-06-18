def is_pentagonal(n):
    pen_test = ((1 + 24 * n)**0.5 + 1)/6
    return pen_test == int(pen_test)

def generate_pentagons(n):
	return [i for i in range(n) if is_pentagonal(i)]

def get_pentagons(n_of_pentagons):
    pentagons = set(generate_pentagons(n_of_pentagons))
    for pentagon1 in pentagons:
        for pentagon2 in pentagons:
            if pentagon1 + pentagon2 in pentagons and abs(pentagon1 - pentagon2) in pentagons:
                print(pentagon1, pentagon2, abs(pentagon1 - pentagon2))


get_pentagons(10000000)

# The answer: 5482660
