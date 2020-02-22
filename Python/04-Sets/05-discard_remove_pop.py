n = int(input())
set_n = set([int(val) for val in input().split()])

m = int(input())
for i in range(m):
    arr = list(input().split())

    if arr[0] == 'pop':
        set_n.pop()

    elif arr[0] == 'discard':
        set_n.discard(int(arr[1]))

    elif arr[0] == 'remove':
        set_n.remove(int(arr[1]))

print(sum(set_n))