n = int(input())
a = list(map(int, input().split()))
c = 0
mx = 0
for i in a:
    if i % 2 == 0:
        c += 1
        mx = max(mx, c)
    else:
        c = 0
print(mx)