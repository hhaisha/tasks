n = int(input())
a = list(map(int, input().split()))
total = sum(a)
left = 0
c = 0
for i in range(n - 1):
    left += a[i]
    right = total - left
    if left == right:
        c += 1
print(c)