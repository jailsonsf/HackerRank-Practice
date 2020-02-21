A = set(map(int, input().split()))

n = int(input())
super_set = True
for i in range(n):
    B = set(map(int, input().split()))

    if (A.issuperset(B)) == False:
        super_set = False

print(super_set)
