# Импортируем необходимые модули
import os

# Указываем имена файлов
filenames = ["1.txt", "2.txt", "3.txt"]

# Создаем пустой список для хранения данных файлов
file_data = []

# Читаем содержимое каждого файла и определяем количество строк
for filename in filenames:
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        num_lines = len(lines)
        file_data.append((filename, num_lines, lines))

# Сортируем список по количеству строк
file_data.sort(key=lambda x: x[1])

# Записываем данные в итоговый файл
with open("result.txt", "w", encoding="utf-8") as result_file:
    for filename, num_lines, lines in file_data:
        result_file.write(f"{filename}\n{num_lines}\n")
        for i, line in enumerate(lines, start=1):
            result_file.write(f"Строка номер {i} файла номер {filename.split('.')[0]}\n{line}")
        result_file.write("\n")  # Добавляем пустую строку между содержимым разных файлов

print("Файлы успешно объединены!")