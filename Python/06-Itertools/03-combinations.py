from itertools import combinations

char, n = input().split()

for i in range(1, int(n) + 1):

    for val in combinations(sorted(char), i):
        print(''.join(val))
