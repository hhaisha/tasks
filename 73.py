n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(n):
    if a[-i:] + a[:-i] == b:
        print(i)
        break
else:
    print(-1)