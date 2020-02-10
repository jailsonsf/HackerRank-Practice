def swap_case(s):
    result_swap = ''
    for letter in s:
        if letter.isupper():
            result_swap += letter.lower()
        
        elif letter.islower():
            result_swap += letter.upper()

        else:
            result_swap += letter

    return result_swap


s = input()
result = swap_case(s)
print(result)
