workers = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for worker in workers:
    name_worker = worker.split(' ')[-1].title()
    print(f'Привет, {name_worker} !')