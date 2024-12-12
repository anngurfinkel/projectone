alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

# task 01 == print('''"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."''')

# task 03 == text = "alice_in_the_wonderland"
print(text)



"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""

# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
Square_Black_sea = 436402
Square_Azov_sea = 37800

Total_square = Square_Black_sea + Square_Azov_sea
print(Total_square) # Total_square = 474202

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
First_storage = "First"
Second_storage = "Second"
Third_storage = "Third"

First_Second = 250449 
Second_Third = 222950
First_Second_Third = 375291

Third = First_Second_Third - First_Second 
First = First_Second_Third - Second_Third
Second = First_Second_Third - First - Third

print(First) # На першому складі 152341 товарів
print(Second) # На другому складі 98108 товарів
print(Third) # На третьому складі 124842 товарів


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
Month = 18
Uah = 1179

Cost_of_computer = Month * Uah

print(Cost_of_computer) # Cost_of_computer = 21222


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9

print(8019 % 8 ) # Остача від ділення 3
print(9907 % 9 ) # Остача від ділення 7
print(2789 % 5 ) # Остача від ділення 4
print(7248 % 6 ) # Остача від ділення 0
print(128 % 5) # Остача від ділення 3
print(19224 % 9) # Остача від ділення 0

"""


# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн

Pizza_large = 274 
Pizza_middle = 218
Juice = 35
Cake = 350 
Water = 21

Budget = (4*Pizza_large + 2*Pizza_middle + 4*Juice + 1*Cake + 3*Water)

print(Budget) # Budget = 2085

"""


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
Total_photos = 232
Page = 8

Total_pages = print(Total_photos/Page)

print(Total_pages) # Total_pages = 29


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
Distance = 1600
Kilometers = 100
Literes = 9


1)
Total_liters = Distance/Kilometers*Literes
print(Total_liters) # Total_liters = 144

2)
Total_liters = 144
Full_tank = 48

Stops = Total_liters/Full_tank
print(Stops) # Stops = 3

