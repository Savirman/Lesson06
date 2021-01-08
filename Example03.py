"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
вызвать методы экземпляров)."""

# Определение класса Worker
class Worker:
    name: str
    surname: str
    position: str
    _income = {"wage": float, "bonus": float}

# Определение класса Position, дочернего Worker
class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        self.total = self._income.setdefault("wage") + self._income.setdefault("bonus")
        return f"{self.total}"

# Создание экземпляра класса Position
petrov = Position()
petrov.name = "Alex"
petrov.surname = "Petrov"
petrov.position = "DevOps-engineer"
petrov._income = {"wage": 90000, "bonus": 40000}
print(petrov.get_full_name())
print(petrov.get_total_income())