
with open("cook_book.txt", "rt", encoding ="utf-8") as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip().lower() #омлет
        quantity = int(file.readline()) # колличество
        ingredient = [] #список ингр
        for _ in range(quantity):
            quan = file.readline().strip().split(" | ")
            name, quantity_ingredient, measure = quan
            ingredient.append({"name": name, "quantity_ingredient": int(quantity_ingredient),
                               "measure": measure})
        file.readline()
        cook_book[dish_name] = ingredient
    print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    sp = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            ingridient["quantity_ingredient"] *= person_count
            if ingridient["name"] not in sp:
                sp[ingridient["name"]] = ingridient
            else:
                sp[ingridient["name"]]["quantity_ingredient"] += ingridient["quantity_ingredient"]
    return sp


def print_shop_list(shop_list, person_count, dishes):
    print(f'Продукты для блюд(а): "{", ".join(list(dishes)).title()}" на {person_count} человек(а):')
    for shop_list_item in shop_list.values():
        print(shop_list_item["name"], shop_list_item["quantity_ingredient"],
              shop_list_item["measure"])


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    print(f'Список блюд: "{", ".join(list(cook_book.keys())).title()}"')
    dishes = input('Введите блюда (через запятую): ').lower().split(', ')
    for dishe in dishes:
        if dishe not in cook_book.keys():
            return print('Нет такого блюда!')

        else:
            ...
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list, person_count, dishes)


create_shop_list()

a = {1: '1.txt', 2: '2.txt', 3: '3.txt'}

def read_file(dict):
    all_file = {}
    for key, values in dict.items():
        with open(values, encoding='utf-8') as file:
            list = [values]
            number_of_rows = 0
            for line in file:
                number_of_rows += 1
                list.append(line)
        all_file[number_of_rows] = list
    return all_file


def file_wr():
    file_write = read_file(a)
    sorted_tuple = dict(sorted(file_write.items()))
    print(sorted_tuple)
    for key, values in sorted_tuple.items():
        with open("file1.txt", "a", encoding="utf-8") as file:
            file.write(f' {values[0]}\n')
            file.write(f' {str(key)}\n')
            file.write(f'{" ".join(values[1:])}\n')

file_wr()
