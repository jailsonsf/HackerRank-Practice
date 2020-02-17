n, m = map(int, input().split())
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0

for val in arr:
    if val in A:
        happiness += 1

    if val in B:
        happiness -= 1
        
print(happiness)
