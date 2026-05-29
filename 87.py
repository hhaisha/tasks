n = int(input())
a = list(map(int, input().split()))
s = sorted(a)
c = 0
for i in range(n):
        if a[i] != s[i]:
            c += 1
if c == 2:
    print('Нельзя')
else:
    print('Можно')