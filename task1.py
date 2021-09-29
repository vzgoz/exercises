class Date:
    def __init__(self,day_month_year):
        self.day_month_year = str(day_month_year)


    @classmethod
    def extract(cls, day_month_year):
        my_date = []


        for i in day_month_year.split():
            if i != '-': my_date.append(i)


        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'All right'
                else:
                    return f'Неправильно указан год'
            else:
                return f'Неправильно указан месяц'
        else:
            return f'Неправильный указан день'

    def __str__(self):
        return f'Текущая дата {Date.extract(self.day_month_year)}'


yesterday = Date('29 - 09 - 2021')
print(yesterday)
print(Date.valid(29, 9, 2021))
print(yesterday.valid(30, 9, 2021))
print(Date.extract('29 - 09 - 2021'))
print(yesterday.extract('12 - 02 - 2020'))
print(Date.valid(1, 11, 2000))
