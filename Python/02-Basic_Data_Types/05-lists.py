result = list()

def lists_operations(operator, values):
    if operator == 'insert':
        result.insert(values[0], values[1])

    elif operator == 'remove':
        result.remove(values[0])

    elif operator == 'append':
        result.append(values[0])


def lists_presentation(operator):
    if operator == 'print':
        print(result)

    elif operator == 'sort':
        result.sort()
    
    elif operator == 'pop':
        result.pop(-1)

    elif operator == 'reverse':
        result.reverse()


N = int(input())

for i in range(N):
    operator, *line = input().split()
    values = list(map(int, line))

    if len(values) > 0:
        lists_operations(operator, values)

    else:
        lists_presentation(operator)