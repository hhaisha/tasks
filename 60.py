n = int(input())
a = list(map(int, input().split()))
c = 0
for i in range(n//2):
    if  a[i] != a[len(a) - i - 1]:
        c = 0
        break
    else:
        c = 1
if c == 1:
    print('Список является палиндромом')
else:
    print('Список не является палиндромом')

