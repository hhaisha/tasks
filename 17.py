a = int(input())
b = int(input())
c = int(input())
d = int(input())

#а) ладья
if a == c or b == d:
    print('а) да')
else:
    print('а) нет')
#б) слон
if abs(a - c) == abs(b - d):
    print('б) да')
else:
    print('б) нет')
#в) король
if abs(a - c) <= 1 and abs(b - d) <= 1:
    print('в) да')
else:
    print('в) нет')
#г) ферзь
if a == c or b == d or abs(a - c) == abs(b - d):
    print('г) да')
else:
    print('г) нет')
#д) белая пешка
if a == c and d == b + 1:
    print('д) да')
elif abs(a - c) == 1 and d == b + 1:
    print('д) да')
else:
    print('д) нет')