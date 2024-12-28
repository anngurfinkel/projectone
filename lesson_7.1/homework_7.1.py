# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= number:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            break
            # Enter the action to take if the result is greater than 25
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def sum(a, b):
    return a + b

print(sum(1, 9))



# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average(*lst):
    return sum(lst) / len(lst)

print(average(1,2,3))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def palindrom(string):
    return string[::-1]
print(palindrom("hello"))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def list(*strings):
    result = sorted(strings, key = len)
    return result[-1]
print(list("a", "asdfg", "ghjk", "wqsdefrthyujhjk"))


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
car_data = {
  'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
  'Audi': ('black', 2020, 2.0, 'sedan', 55000),
  'BMW': ('white', 2018, 3.0, 'suv', 70000),
  'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
  'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
  'Honda': ('red', 2017, 1.5, 'sedan', 30000),
  'Ford': ('green', 2019, 2.3, 'suv', 40000),
  'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
  'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
  'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
  'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
  'Kia': ('white', 2020, 2.0, 'sedan', 28000),
  'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
  'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
  'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
  'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
  'Jeep': ('green', 2021, 3.0, 'suv', 50000),
  'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
  'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
  'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
  'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
  'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
  'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
  'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
  'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
  'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
  'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
  'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
  'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
  'Acura': ('white', 2017, 2.4, 'suv', 40000),
  'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
  'Infiniti': ('gray', 2018, 2.0, 'sedan', 35000),
  'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
  'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
  'Ram': ('black', 2019, 5.7, 'pickup', 40000),
  'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
  'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
  'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
  'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000)
}
search_criteria = (2017, 1.6, 36000)

car_attributes = list(car_data.values())

def get_car(car):
   if car[1] >= 2017 and car[2] >= 1.6 and car[4] <= 36000:
          return car
   
def get_price(car):
     return car[4]

filtered_cars = list(filter(get_car, car_attributes))
print(filtered_cars)

filtered_cars.sort(key = get_price)
print(filtered_cars)

first_five_cars = filtered_cars[:5]
print(first_five_cars)


# task 8
people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

def add_person(people_records, person):
     people_records.insert(0,person)
     return people_records
     
new_person = ('Anna', 'Hurfinkel', 28, 'QA Specialist', 'Kyiv')

print(add_person(people_records, new_person))

# task 9
people_records = [
  ('Anna', 'Hurfinkel', 28, 'QA Specialist', 'Kyiv'),
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]
def swap_people(people_records, index1, index5):
     people_records[index1], people_records[index5] = people_records[index5], people_records[index1]
     return people_records

print(swap_people(people_records, 1, 5))


# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
people_records =[
 ('Anna', 'Hurfinkel', 28, 'QA Specialist', 'Kyiv'), 
 ('Michael', 'Brown', 22, 'Student', 'Seattle'), 
 ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'), 
 ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'), 
 ('Emily', 'Williams', 30, 'Artist', 'San Francisco'), 
 ('John', 'Doe', 28, 'Engineer', 'New York'), 
 ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'), 
 ('David', 'Miller', 33, 'Software Developer', 'Austin'), 
 ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'), 
 ('Daniel', 'Taylor', 38, 'Architect', 'Portland'), 
 ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'), 
 ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'), 
 ('Emma', 'Hall', 31, 'Chef', 'Dallas'), 
 ('William', 'Clark', 29, 'Financial Analyst', 'Houston'), 
 ('Ava', 'White', 42, 'Journalist', 'San Diego'), 
 ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')]


#indexes 6, 10, 13

people_records_2 = (people_records[6],people_records[10],people_records[13])
print(people_records_2)

#age >=30

def criteria(age):
    return age[2] >=30
    

def people(records):
        result = list(filter(criteria, records))
        return result

print(people(people_records_2))
