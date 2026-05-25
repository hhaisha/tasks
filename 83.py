n = int(input())
a = list(map(int, input().split()))
mn = 10**5
for i in range(n):
    sm = 0
    for j in range(i, n):
        sm += a[j]
        if sm > 0:
            mn = min(mn, j - i + 1)
            break
if mn == 10**5:
    print('no')
else:
    print(mn)