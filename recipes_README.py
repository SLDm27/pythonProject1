from pprint import pprint

with open('recipes.txt', encoding= 'utf-8') as f:
    cook_book = {}
    for line in f:
        dish_name = line.strip()
        ingredients_count = int(f.readline())
        ingredients = []
        for i in range(ingredients_count):
            ingredient = f.readline().strip()
            ingredient_name, quantity, measure = ingredient.split(' | ')
            ingredients.append({'ingredient_name': ingredient_name,
                                'quantity': quantity,
                                'measure': measure})
        cook_book[dish_name] = ingredients
        f.readline()


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            quantity = int(ingredient['quantity']) * person_count
            measure = ingredient['measure']
            if ingredient_name in shop_list:
                shop_list[ingredient_name]['quantity'] += quantity
            else:
                shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
    return shop_list

dishes = ['Омлет', 'Фахитос', 'Утка по-пекински']
person_count = 3
shop_list = get_shop_list_by_dishes(dishes, person_count)
pprint(shop_list)

# print(get_shop_list_by_dishes)



