n = int(input())
a = list(map(int, input().split()))
c = 0
mx = 0
for i in range(1, n):
    if (a[i] > 0 and a[i-1] < 0) or (a[i] < 0 and a[i-1] > 0):
        c += 1
    else:
        c = 1
    mx = max(mx, c)
print(mx)