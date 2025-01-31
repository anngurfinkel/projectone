import csv

file_1 = "r-m-c.csv"
file_2 = "random-michaels.csv"
result_file = "csv/result_compares_files.csv"

with open('r-m-c.csv', 'r', encoding='utf-8') as csvfile_1:
    reader = csv.reader(csvfile_1)
    header_1 = next(reader_1)
    data_1 = []
    for row in reader_1:
        data_1.append(tuple(row))

with open('random-michaels.csv', 'r', encoding='utf-8') as csvfile_2:
    reader = csv.reader(csvfile_2)
    header_2 = next(reader_2)
    data_2 = []
    for row in reader_2:
        data_2.append(tuple(row))

if header_1 != header_2
    raise ValueError

unique_data = list(set(data_1).symmetric_difference(set(data_2)))

with open('result_compares_files.csv', 'w', encoding='utf-8', newline='') as result:
    writer = csv.writer(result)
    writer.writerow(header1)  # Записуємо заголовок у результуючий файл
    writer.writerows(unique_data) 

print(f"Дублікати видалено. Результат збережено у {result_file}.")
