s = input()

validator = {
    'alnum': False,
    'alpha': False,
    'digit': False,
    'lower': False,
    'upper': False
}

for char in s:

    if char.isalnum():
        validator['alnum'] = True

    if char.isalpha():
        validator['alpha'] = True

    if char.isdigit():
        validator['digit'] = True

    if char.islower():
        validator['lower'] = True


    if char.isupper():
        validator['upper'] = True

for key in validator:
    print(validator[key])
