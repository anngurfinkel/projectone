# Порахувати кількість унікальних символів в строці. 
# Якщо їх більше 10 - вивести в консоль True, інакше - False. 
# Строку отримати за допомогою функції input()

my_string = input("Enter your string: ")

print(len(set(my_string)))

if len(set(my_string)) >=10:
    print(True)
else: 
    print(False)