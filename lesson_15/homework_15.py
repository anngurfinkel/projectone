# Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:

# сторона_а (довжина сторони a).
# кут_а (кут між сторонами a і b).
# кут_б (суміжний з кутом кут_а).
# Необхідно реалізувати наступні вимоги:

# Значення сторони сторона_а повинно бути більше 0.
# Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
# Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично.
# Для встановлення значень атрибутів використовуйте метод __setattr__.

class Rhomb:
    def __init__(self, side_a, angle_a, angle_b):
            if angle_a is not None and angle_b is not None:
                if angle_a + angle_b != 180:
                    raise ValueError
            self.side_a = side_a 
            if angle_a is not None:
                self.angle_a = angle_a 
            elif angle_b is not None:
                self.angle_b = angle_b


    def __setattr__(self, key, value):
        if key == "side_a":
             if value <= 0:
                  value = abs(value)
        elif key == "angle_a":
             if not(0 < value < 180):
                  raise ValueError
             self.__dict__["angle_b"] = 180 - value
        elif key == "angle_b":
             if not(0 < value < 180):
                  raise ValueError
             self.__dict__["angle_a"] = 180 - value
        self.__dict__[key] = value

