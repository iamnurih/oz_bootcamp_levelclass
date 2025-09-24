participants = 5
score = []

for i in range(participants):
    a, b, c, d = map(int, input().split())
    score.append([a, b, c, d])

total_score = []
for i in range(participants):
    participants_total = sum(score[i])
    total_score.append(participants_total)

max_score = max(total_score)
winner_index = total_score.index(max_score) + 1

print(winner_index, max_score)






