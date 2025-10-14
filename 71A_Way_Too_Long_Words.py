n = int(input())
for _ in range(n):
    word = input()
    print(word[0] + str(len(word)-2) + word[-1])
