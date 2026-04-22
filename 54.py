n = int(input())
a = list(map(int, input().split()))
c = 1
mx = 1
for i in range(1, n):
    if  a[i] > a[i+1]:
        c += 1
    else:
        c = 1
    if c > mx:
        mx = c
print(mx)
