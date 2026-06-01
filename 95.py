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
        r.append(x)
        i += 1
    elif a[i] > b[j]:
        j += 1
    else:
        i += 1
        j += 1
while i < n:
    r.append(a[i])
    i += 1
print(r)