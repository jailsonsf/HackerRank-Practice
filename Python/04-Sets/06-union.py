n = int(input())
english = set(map(int, input().split()))

b = int(input())
french = set(map(int, input().split()))

result_union = english | french

print(len(result_union))
