n = int(input())
a = list(map(int, input().split()))
unq = []
u = set()
for i in a:
    if a.count(i) == 1:
        unq.append(i)
for i in a:
    if a.count(i) > 1 and i not in u:
        unq.append(i)
        u.add(i)
print(unq)

