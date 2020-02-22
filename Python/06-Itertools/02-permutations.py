from itertools import permutations

char, n = input().split()
n = int(n)

permutations = sorted(list(permutations(char, n)))

for val in permutations:
    permutation = ''

    for i in val:
        permutation += i

    print(permutation)
