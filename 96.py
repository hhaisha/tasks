n = int(input())
a = list(map(int, input().split()))
unq = set(a)
otv = n
for i in range(n):
    c = set()
    for j in range(i, n):
        c.add(a[j])
        if len(c) == len(unq):
            otv = min(otv, j - i + 1)
            break
print(otv)