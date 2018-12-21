n = int(input())
scores = input().split()
scores= map(int, scores)
scores = list(scores)
max_score = max(scores)
summ=0
for i in scores:
    summ += i/max_score

print(summ/n*100)
