n_test_case = int(input())

for i in range(n_test_case):
    n_A = int(input())
    A = set(map(int, input().split()))

    n_B = int(input())
    B = set(map(int, input().split()))

    result = A.issubset(B)
    print(result)
