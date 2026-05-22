n = int(input())
a = list(map(int, input().split()))
current = a[0]
sm = a[0]
temp_start = 0
start = 0
end = 0
for i in range(1, n):
    if a[i] > current + a[i]:
        current = a[i]
        temp_start = i
    else:
        current += a[i]
    if current > sm:
        sm = current
        start = temp_start
        end = i
print(start, end)