len_A = int(input())
A = set(map(int, input().split()))

number_op = int(input())

for i in range(number_op):
    op, len_set = input().split()

    if op == 'update':
        A |= set(map(int, input().split()))

    elif op == 'intersection_update':
        A &= set(map(int, input().split()))

    elif op == 'difference_update':
        A -= set(map(int, input().split()))

    elif op == 'symmetric_difference_update':
        A ^= set(map(int, input().split()))

print(sum(A))