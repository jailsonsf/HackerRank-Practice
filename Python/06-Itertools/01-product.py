from itertools import product

A = map(int, input().split())
B = map(int, input().split())

AxB = list(product(A, B))

for val in AxB:
    print(val, end=' ')
