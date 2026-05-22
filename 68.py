n = int(input())
a = list(map(int, input().split()))
current = a[0]
sm = a[0]
for i in range(1, n):
    current = max(a[i], current + a[i])
    sm = max(sm, current)
print(sm)