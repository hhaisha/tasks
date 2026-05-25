n = int(input())
a = list(map(int, input().split()))
st = set(a)
if (len(a) - len(st)) <= 1:
    print('Да')
else:
    print('Нет')