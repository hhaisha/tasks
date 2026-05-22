n = int(input())
a = list(map(int, input().split()))
s = set()
for i in a:
    if i not in s:
        s.add(i)
print(s)