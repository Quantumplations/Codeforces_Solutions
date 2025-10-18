n = int(input())
x = 0
for _ in range(n):
    statement = input()
    if statement[1] == "+":
        x += 1
    else:
        x -= 1
print(x)