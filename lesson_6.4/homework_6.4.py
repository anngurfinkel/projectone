# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = 0

for i in lst1:
    if i%2 == 0:
        result = result + i 

print(result)