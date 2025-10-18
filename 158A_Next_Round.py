n, k = list(map(int, input().split()))
scores = list(map(int, input().split()))
threshold_score = scores[k-1]
for i in range(n):
    if scores[i] > 0 and scores[i] >= threshold_score:
        scores[i] = 1
    else:
        scores[i] = 0
print(sum(scores))

