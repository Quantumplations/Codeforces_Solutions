n = int(input())
total_num_probs = 0
for _ in range(n):
    P, V, T = map(int, input().split())
    if P + V + T >= 2:
        total_num_probs += 1
    else:
        continue
print(total_num_probs)