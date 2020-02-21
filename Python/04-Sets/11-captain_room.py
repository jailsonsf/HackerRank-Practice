K = int(input())
rooms = list(map(int, input().split()))

set_Rooms = set(rooms)
sumlist = sum(rooms)

print((sum(set_Rooms) * K - sumlist) // (K - 1))
