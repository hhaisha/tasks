n = int(input())
num = n
rev = 0
while n > 0:
    rev = rev * 10 + (n % 10)
    n //= 10
if num == rev:
    print('Читается в обе стороны')
else:
    print('Не читается в обе стороны')