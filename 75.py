n = int(input())
a = list(map(int, input().split()))
mx = 0
for i in range(n):
    u = set()
    c = 0
    for j in range(i, n):
        if a[j] in u:
            break
        u.add(a[j])
        c += 1
    if c > mx:
        mx = c
print(mx)
