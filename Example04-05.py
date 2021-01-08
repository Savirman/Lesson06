"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
# Определение класса Car с атрибутами и методами
class Car:
    speed: float
    color: str
    name: str
    is_police: bool

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn_left(self):
        print("Машина повернула налево")

    def turn_right(self):
        print("Машина повернула направо")

    def show_speed(self, speed):
        print(f"Текущая скорость {speed} км/ч")

# Определение дочернего (от Car) класса TownCar
class TownCar(Car):
    # Переопределение метода show_speed()
    def show_speed(self, speed):
        if speed > 60:
            print("Вы превысили скорость")
        else:
            print("Вы едете с допустимой скоростью")
# Определение дочернего (от Car) класса WorkCar
class WorkCar(Car):
    # Переопределение метода show_speed()
    def show_speed(self, speed):
        if speed >40:
            print("Вы превысили скорость")
        else:
            print("Вы едете с допустимой скоростью")
# Определение дочернего (от Car) класса PoliceCar
class PoliceCar(Car):
    is_police = True
# Определение дочернего (от Car) класса SportCar
class SportCar(Car):
    speed = 200
# Создание экземпляра класса TownCar
prius = TownCar()
prius.speed = float(input("Введите значение скорости для Toyota Prius>>> "))
prius.color = "Grey"
prius.name = "Toyota Prius"
prius.show_speed(prius.speed)
# Создание экземпляра класса WorkCar
gazel = WorkCar()
gazel.speed = float(input("Введите значение скорости для Газель Next>>> "))
gazel.color = "White"
gazel.name = "Газель Next"
gazel.show_speed(gazel.speed)
# Создание экземпляра класса PoliceCar
bobik = PoliceCar()
bobik.speed = float(input("Введите значение скорости для УАЗ Hunter>>> "))
bobik.color = "Blue"
bobik.name = "УАЗ Hunter"
bobik.show_speed(bobik.speed)
# Создание экземпляра класса SportCar
porsche = SportCar()
porsche.name = "Porsche 911"
porsche.name = "Red"
porsche.show_speed(porsche.speed)