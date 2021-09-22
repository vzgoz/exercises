class Stationery:
    def __init__(self,title):
        self.title = title

    def draw(self):
        return f'Запуск'


class Pen(Stationery):
    def draw(self):
        return f'Запуск {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'Запуск {self.title}'

class Handle(Stationery):
    def draw(self):
        return f'Запуск {self.title}'

pen = Pen('с ручкой')
print(pen.draw())
pencil = Pencil('c карандашем')
print(pencil.draw())
handle = Handle ('с маркером')
print(handle.draw())