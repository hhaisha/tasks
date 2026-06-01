n = int(input())
a1 = list(map(int, input().split()))
m = int(input())
b1 = list(map(int, input().split()))

a = sorted(a1)
b = sorted(b1)
i = 0
j = 0
r = []

while i < n and j < m:
    if a[i] < b[j]:
        x = a[i]
        i += 1
    elif a[i] > b[j]:
        x = b[j]
        j += 1
    else:
        x = a[i]
        i += 1
        j += 1
    if len(r) == 0 or r[-1] != x:
        r.append(x)
while i < n:
    if len(r) == 0 or r[-1] != a[i]:
        r.append(a[i])
    i += 1
while j < m:
    if len(r) == 0 or r[-1] != b[j]:
        r.append(b[j])
    j += 1
print(r)
        