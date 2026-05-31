n = int(input())
a = list(map(int, input().split()))
s = []
for i in range(n):
    c = 0
    for j in range(i+1, n):
        if a[i] == a[j]:
            c = j - 1
            break
    s.append([a[i], c])
print(s)