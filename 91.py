n = int(input())
a = list(map(int, input().split()))
mx = 0
el = None
fst = n
for i in range(n):
    x = a[i]
    c = a.count(x)
    if c > mx:
        mx = c
        el = x
        fst = i
    elif c == mx and i < fst:
        el = x
        fst = i
print(el, mx)