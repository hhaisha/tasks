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
    if a[i] == b[j]:
        r.append(a[i])
        i += 1
        j += 1
    elif a[i] < b[j]:
        i += 1
    else:
        j += 1
print(r)