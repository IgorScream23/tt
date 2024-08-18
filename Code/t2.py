from pprint import pprint

def get_shop_list_by_dishes(dishes, person_count):
    # Инициализация пустого словаря для хранения итогового списка покупок
    shop_list = {}

    # Перебираем список блюд, переданный в функцию
    for dish in dishes:
        if dish in cook_book:  # Проверяем, есть ли блюдо в cook_book
            for ingredient in cook_book[dish]:  # Перебираем ингредиенты блюда
                name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity'] * person_count

                # Если ингредиент уже есть в словаре, суммируем количество
                if name in shop_list:
                    shop_list[name]['quantity'] += quantity
                else:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
        else:
            print(f"Блюдо {dish} не найдено в книге рецептов!")

    return shop_list

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

# Пример использования функции
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))