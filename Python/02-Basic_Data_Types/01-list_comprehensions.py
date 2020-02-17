x = int(input())
y = int(input())
z = int(input())
n = int(input())

arr = [
    [i, j, c]
    for i in range(x + 1)
        for j in range(y + 1)
            for c in range(z + 1)
                if ((i + j + c) != n)
]

print(arr)
