n = int(input())
a = list(map(int, input().split()))
c = 0
el = 0
for i in a:
    d = a.count(i)
    if d > c:
        c = d
        el = i
print(el)