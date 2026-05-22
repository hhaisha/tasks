n = int(input())
a = list(map(int, input().split()))

mx = 0
for i in range(n):
    sm = 0
    for j in range(i, n):
        sm += a[j]
        if sm == 0:
            mx = max(mx, j - i + 1)
print(mx)