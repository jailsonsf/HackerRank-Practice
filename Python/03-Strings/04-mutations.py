def mutate_string(string, position, character):
    arr_string = list(string)

    arr_string[position] = character

    return  ''.join(arr_string)


s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)