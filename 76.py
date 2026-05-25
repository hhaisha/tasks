n = int(input())
a = list(map(int, input().split()))
u = set()
l = 0
mx = 0
for r in range(n):
    while a[r] in u:
        u.remove(a[l])
        l += 1
    u.add(a[r])
    mx = max(mx, r - l + 1)
print(mx)