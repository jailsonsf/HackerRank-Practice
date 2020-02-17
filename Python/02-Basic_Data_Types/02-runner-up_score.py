n = int(input())
arr = map(int, input().split())

arr = list(arr)

maximun = max(arr)
second_maximun = min(arr)

for i in arr:
    if i < maximun and i > second_maximun:
        second_maximun = i

print(second_maximun)
