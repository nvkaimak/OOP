# ЗАДАНИЕ 1-2
def read_receipt(PATH):
    cook_book = {}
    list_dishes = []
    with open(PATH, encoding='utf-8') as f:
        lines = f.readlines()
        lines_dish = ''.join(lines).split('\n\n')
        for dish in lines_dish:
            list_dishes.append(dish.split('\n'))

    for dish in list_dishes:
        ingredients = [ingredient.split('|') for ingredient in dish[2:]]
        cook_book[dish[0]] = []
        for ingredient in ingredients:
            cook_book[dish[0]].append(
                {'ingredient_name': ingredient[0], 'quantity': int(ingredient[1]), 'measure': ingredient[2]})
    return cook_book


cook_book = read_receipt('receipt.txt')


def get_shop_list_by_dishes(dishes, person_count):
    needed_ingredients = {}
    for dish in dishes:
        for dish_name, ingredients in cook_book.items():
            if dish == dish_name:
                for ingredient in ingredients:
                    if ingredient['ingredient_name'] in needed_ingredients.keys():
                        needed_ingredients[ingredient['ingredient_name']]['quantity'] += person_count * ingredient[
                            'quantity']
                    else:
                        needed_ingredients[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                                             'quantity': person_count * ingredient[
                                                                                 'quantity']}

    return needed_ingredients


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

# Задание 3

list_path = {'1.txt', '2.txt', '3.txt'}
sort_list = {}
for path in list_path:
    with open(path, encoding='utf-8') as f:
        lines = f.readlines()
        sort_list[path] = len(lines)
list_path_sorted = sorted(sort_list.items(), key=lambda item: item[1])
with open('итоговый файл.txt', 'a', encoding='utf-8') as f1:
    for path in list_path_sorted:
        with open(path[0], encoding='utf-8') as f:
            f1.write(path[0] + '\n' + str(path[1]) + '\n' + f.read() + '\n')
