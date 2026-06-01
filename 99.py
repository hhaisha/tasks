n = int(input())
a = list(map(int, input().split()))
mx = 1
c = 1
for i in range(n-1):
    if abs(a[i] - a[i+1]) == 1:
        c += 1
    else:
        c = 1
    if c > mx:
        mx = c
print(mx)