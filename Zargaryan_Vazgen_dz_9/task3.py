class Worker:


    def __init__(self, name, surname, position, wage,bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': int(wage), 'bonus': int(bonus)}


class Position(Worker):
    def __init__(self,name, surname, position, wage,bonus):
        super().__init__(name, surname, position, wage,bonus)

    def get_name(self):
        return self.name + ' ' + self.surname

    def get_income(self):
        return self._income['wage'] + self._income['bonus']


result = Position('Ivan','Ivanov', 'HR', 12322, 2101)
print(result.get_name(), result.get_income())