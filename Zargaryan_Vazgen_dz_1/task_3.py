percent = int(input('Введите процент: '))
if percent >= 11 and percent <= 14:
    print(percent, 'процентов')
elif percent % 10 == 1:
    print(percent, 'процент')
elif percent % 10 == 2 or percent % 10 == 3 or percent % 10 == 4:
    print(percent, 'процента')
else:
    print(percent, 'процентов')
