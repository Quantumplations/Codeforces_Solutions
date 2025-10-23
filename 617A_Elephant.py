x = int(input())
s = 0
if x%5 == 0:
    s = x//5
else:
    s = x//5 + 1
print(s)