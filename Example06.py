"""
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""
# Определение класса Stationery
class Stationery:
    title: str

    def draw(self):
        print("Запуск отрисовки")
# Определение дочернего класса Pen (от Stationery)
class Pen(Stationery):
    # Переопределение метода draw()
    def draw(self):
        print("Отрисовка ручкой")
# Определение дочернего класса Pencil (от Stationery)
class Pencil(Stationery):
    # Переопределение метода draw()
    def draw(self):
        print("Отрисовка карандашом")
# Определение дочернего класса Handle (от Stationery)
class Handle(Stationery):
    # Переопределение метода draw()
    def draw(self):
        print("Отрисовка маркером")
# Создание экземпляра класса Pen
blue_pen = Pen()
blue_pen.draw()
# Создание экземпляра класса Pencil
grey_pencil = Pencil()
grey_pencil.draw()
# Создание экземпляра класса Handle
black_handle = Handle()
black_handle.draw()