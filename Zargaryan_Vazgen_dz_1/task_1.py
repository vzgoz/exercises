duration = int(input('Введите время в секундах: '))

if duration < 60: #Только секунды
    print(duration, ' сек')

elif duration >= 60 and duration < 3600: # Минуты и секунды
    print(duration // 60, ' минут', duration % 60, ' сек')

elif duration >= 3600 and duration < 86400: # Часы, минуты и секунды
    print(duration // 3600, ' час', (duration % 3600) // 60 , ' минут', duration % 60, ' сек')

else: # Дни, часы, минуты и секунды
    print(duration // 86400, ' дн.', (duration % 86400)//3600 , ' час', (duration % 3600) // 60, ' минут', duration % 60, ' сек')