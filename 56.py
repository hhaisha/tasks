n = list(map(int, input().split()))
c = 0
for i in range(len(n)):
    if n[i] % 2 == 0:
        c += 1
print(c)
