m = int(input())
set_m = set(map(int, input().split()))

n = int(input())
set_n = set(map(int, input().split()))

symmetric_diff = set_m.symmetric_difference(set_n)
symmetric_diff = sorted(symmetric_diff)

for val in symmetric_diff:
    print(val)
