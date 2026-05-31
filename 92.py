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
    if a[i] <= b[j]:
        r.append(a[i])
        i += 1
    else:
        r.append(b[j])
        j += 1
while i < n:
    r.append(a[i])
    i += 1
while j < m:
    r.append(b[j])
    j += 1
print(r)