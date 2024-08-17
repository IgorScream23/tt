from pprint import pprint
# Чтение данных из файла recipes.txt
with open('C:/Users/Анна/Desktop/homework/Code/recipes.txt', 'r', encoding='utf-8') as f:
    data = f.read().splitlines()

# Инициализация пустого словаря для хранения рецептов
cook_book = {}

# Переменные для хранения текущего блюда и его ингредиентов
current_dish = ''
ingredients = []

# Обработка строк файла
for line in data:
    if line.isdigit():  # Если строка содержит число, это количество ингредиентов
        continue
    elif '|' not in line:  # Если нет символа |, это название блюда
        if current_dish:
            cook_book[current_dish] = ingredients  # Сохранение предыдущего блюда в словарь
        current_dish = line
        ingredients = []  # Инициализация списка для ингредиентов нового блюда
    else:  # Если строка содержит |, это ингредиент
        ingredient_name, quantity, measure = map(str.strip, line.split('|'))
        ingredients.append({
            'ingredient_name': ingredient_name,
            'quantity': int(quantity),
            'measure': measure
        })

# Добавление последнего блюда в словарь
if current_dish:
    cook_book[current_dish] = ingredients

# Вывод результата
pprint (cook_book)