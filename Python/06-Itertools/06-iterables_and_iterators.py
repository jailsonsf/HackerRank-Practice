from itertools import combinations

N = int(input())
arr = list(map(str, input().split()))
K = int(input())

num = 0
den = 0

for val in combinations(arr, K):
    den += 1
    num += 'a' in val

print(float(num) / den)
