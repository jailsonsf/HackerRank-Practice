from itertools import groupby

char = input()

for k, g in groupby(char):
    result = (len(list(g)), int(k))

    print(result, end=' ')
