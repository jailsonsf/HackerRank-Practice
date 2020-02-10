def print_rangoli(size):
    for i in range(size):
        s = '-'.join(chr(ord('a') + n - j - 1) for j in range(i + 1))
        print((s + s[::-1][1:]).center(n * 4 - 3, '-'))

    for i in range(size - 1):
        s = '-'.join(chr(ord('a') + n - j - 1) for j in range(n - i - 1))
        print((s + s[::-1][1:]).center(n * 4 - 3, '-'))


n = int(input())
print_rangoli(n)
