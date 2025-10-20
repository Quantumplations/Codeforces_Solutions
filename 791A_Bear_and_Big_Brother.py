a, b = map(int, input().split())
t = 0
while a <= b:
    t += 1
    a *= 3
    b *= 2
print(t)
