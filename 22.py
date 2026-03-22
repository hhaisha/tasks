month = int(input())
a = [1, 3, 5, 7, 8, 10, 12]
b = [4, 6, 9, 11]
c = [2]
if month in a:
    print('В месяце 31 день')
elif month in b:
    print('В месяце 30 дней')
elif month in c:
    print('В месяце 28 дней')