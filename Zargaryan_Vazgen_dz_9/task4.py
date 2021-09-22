class Car:
    def __init__(self, name,speed,color, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} is going'

    def stop(self):
        return f'{self.name} stoped'

    def turn(self, direction):
        return f' {self.name} turned {direction}'

    def show_speed(self):
        return f' The speed is {self.speed}'

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f' The speed is higher: {self.speed}'
        else:
            return f'The speed is normal:{self.speed}'


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f' The speed is higher: {self.speed}'
        else:
            return f'The speed is normal:{self.speed}'



class PoliceCar(Car):
    pass


class SportCar(Car):
    pass


town_car = TownCar('BMW',80,'blue', False)
print('1:' + town_car.go(), town_car.show_speed(), town_car.turn('left'), town_car.turn('right'), town_car.stop())

work_car = WorkCar('Lada',37,'yellow',False)
print('2:' + work_car.go(), work_car.show_speed(), work_car.turn('left'), work_car.turn('right'), work_car.stop())

police_car = PoliceCar('Honda',120,'blue',True)
print('3:' + police_car.go(), police_car.show_speed(), police_car.turn('left'), police_car.turn('right'), police_car.stop())

sport_car = SportCar('Ferrari',110,'red',False)
print('4:' + sport_car.go(), sport_car.show_speed(), sport_car.turn('left'), sport_car.turn('right'), sport_car.stop())