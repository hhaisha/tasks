n = int(input())
a = list(map(int, input().split()))
l = 0
while l + 1 < n and a[l] <= a[l+1]:
    l += 1
if l == n - 1:
    print(0)
r = n - 1
while r - 1 >= 0 and a[r-1] <= a[r]:
    r -= 1
otv = min(n - l - 1, r)
i = 0
j = r
while i <= l and j < n:
    if a[i] <= a[j]:
        otv = min(otv, j - i - 1)
        i += 1
    else:
        j += 1
print(otv)