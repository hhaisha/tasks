n = int(input())
a = list(map(int, input().split()))
s = set()
for i in range(n-2):
    b = [a[i], a[i+1], a[i+2]]
    b.sort()
    s.add(b[1])
print(len(s))