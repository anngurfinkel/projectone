# Генератори:
# Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
# Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.

# Ітератори:
# Реалізуйте ітератор для зворотного виведення елементів списку.
# Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.

# Декоратори:
# Напишіть декоратор, який логує аргументи та результати викликаної функції.
# Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.


import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Генератори:

def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b


# Ітератори:

class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.current = -2

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 2
        if self.current > self.n:
            raise StopIteration
        return self.current
            

# Декоратори:

def log_function(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.info(f"Test {func.__name__} executed with result: {result}")
        return result
    return wrapper

def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Помилка у {func.__name__}: {e}")
            return None
    return wrapper

@log_function
@exception_handler
def devide(a, b):
    return a/b

if __name__ == "main":
    print("Парни чісла до 10:", list(even_numbers(10)))
    print("Фібоначчі до 50:", list(fibonacci(50)))

    rev_iter = ReverseIterator([1, 2, 3, 4, 5])
    print("Зворотний список:", list(rev_iter))

    even_iter = EvenIterator(10)
    print("Парні числа з ітератора:", list(even_iter))

    print("Ділення 10 на 2:", devide(10,2))
    print("Ділення 10 на 0:", devide(10,0))