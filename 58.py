n = int(input())
a = list(map(int, input().split()))
ind = 0
for i in range(1, n - 1):
    if  a[i-1] > a[i] < a[i+1]:
        ind = i
if ind == 0:
    print('no')
else:
    print(ind)
