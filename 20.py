weight = float(input())
if weight <= 60:
    print('Легкая категория')
elif weight <= 64:
    print('Первая полусредняя категория')
elif weight <= 69:
    print('Полусредняя категория')
else:
    print('Не подходит')