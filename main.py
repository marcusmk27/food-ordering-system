import random

with open('Menu_Description.txt', 'r') as f:
    menu = {}
    for line in f:
        values = line.strip().split(',')
        if len(values) == 2:
            food_name = values[0].strip()
            price = float(values[1].strip())
            menu[food_name] = price
    for food_name, price in menu.items():
        print(f'{food_name}  ${price:.2f}')


def take_order():
    menu = {
        'Burger': 40.00,
        'Drink': 15.00,
        'Fries': 20.00,
        'Wraps': 32.00,
        'Wings': 30.00,
        'Lamb Chops': 76.00
    }

    order = {}
    total_cost = 0.0

    while True:
        food_name = input("What would you like to order? (type 'n' to finish) ")
        if food_name == 'n':
            break

        if food_name not in menu:
            print("Sorry, we don't have that at the moment.")
            continue

        item_num = int(input(f"How many {food_name}s would you like to order? "))
        total = menu[food_name] * item_num
        order[food_name] = item_num
        total_cost += total

        order_number = random.randint(10, 1000)
    print("Your order number: ", order_number)
    with open('order.txt', 'w') as f:
        for food_name, item_num, in order.items():
            order_line = f"{item_num} {food_name}(s)\n"
            print(order_line, end='')
            f.write(order_line)

        total_line = f"Total cost: {total_cost:.2f}"

        f.write(total_line)

    print(f"Total cost: {total_cost:.2f}")


take_order()



