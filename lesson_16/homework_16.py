# Завдання 1

# Створіть клас Employee, який має атрибути name та salary. Далі створіть два класи, Manager та Developer, які успадковуються від Employee. Клас Manager повинен мати додатковий атрибут department, а клас Developer - атрибут programming_language.

# Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer. Цей клас представляє керівника з команди розробників. Клас TeamLead повинен мати всі атрибути як Manager (ім'я, зарплата, відділ), а також атрибут team_size, який вказує на кількість розробників у команді, якою керує керівник.

# Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead

# Завдання 2

# Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру. Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру. Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор. Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.

#1

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language


class TeamLead(Employee):
    def __init__(self, name, salary, department, programming_language, team_size):
        super().__init__(name, salary)
        self.department = department
        self.programming_language = programming_language
        self.team_size = team_size

import unittest

class TestTeamLead(unittest.TestCase):
    def test_attributes(self):
        lead = TeamLead("Tom", 1000, "Finance", "Java", 7)
        self.assertEqual(lead.name, "Tom")
        self.assertEqual(lead.salary, 1000)
        self.assertEqual(lead.department, "Finance")
        self.assertEqual(lead.programming_language, "Java")
        self.assertEqual(lead.team_size, 7)

if __name__ == '__main__':
    unittest.main()


#2
from abc import ABC, abstractmethod
class Figure(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Figure):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)
    
class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return 3.14 * self.__radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.__radius
    
class Square(Figure):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return (self.__side)**2

    def perimeter(self):
        return 4 * self.__side

rectangle = Rectangle(2,4)
circle = Circle(5)
square = Square(6)

print(f"Rectangle: Area = {rectangle.area()}, Perimeter = {rectangle.perimeter()}")
print(f"Circle: Area = {circle.area()}, Perimeter = {circle.perimeter()}")
print(f"Square: Area = {square.area()}, Perimeter = {square.perimeter()}")