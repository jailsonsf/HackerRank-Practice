def minion_game(s):
    s_len = len(s)
    player1, player2 = 0, 0

    for i in range(s_len):
        if s[i] in 'AEIOU':
            player1 += s_len - i

        else:
            player2 += s_len - i

    if  player1 > player2:
        print(f'Kevin {player1}')

    elif player2 > player1:
        print(f'Stuart {player2}')

    else:
        print('Draw')


s = input()
minion_game(s)
