score_list = {}

for _ in range(int(input())):
    name = input()
    score = float(input())

    if score in score_list:
        score_list[score].append(name)

    else:
        score_list[score] = [name]

new_list_score = []
for i in score_list:
    new_list_score.append([i, score_list[i]])

new_list_score.sort()

result = new_list_score[1][1]
result.sort()

print(*result, sep='\n')