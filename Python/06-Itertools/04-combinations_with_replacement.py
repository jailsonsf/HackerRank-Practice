from itertools import combinations_with_replacement

char, n = input().split()

for val in combinations_with_replacement(sorted(char), int(n)):
    print(''.join(val))
