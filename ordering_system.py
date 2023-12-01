# Dictionary

menu = {
    1: {
        "name": 'espresso',
        "price": 1.99
    },
    2: {
        "name": 'coffee',
        "price": 2.50
    },
    3: {
        "name": 'cake',
        "price": 2.79
    },
    4: {
        "name": 'soup',
        "price": 4.50
    },
    5: {
        "name": 'sandwich',
        "price": 4.99
    }
}

# functions


def calculate_subtotal(order):
    print('Calculating bill subtotal...')
    subtotal = 0
    for item in order:
        item_price = item["price"]
        subtotal += item_price
    return round(subtotal, 2)

    raise NotImplementedError()

# 15 % tax


def calculate_tax(subtotal):
    print('Calculating tax from subtotal...')
    tax = 0.15
    total_tax = subtotal * tax
    return round(total_tax, 2)
    raise NotImplementedError()


def summarize_order(order):
    print_order(order)

    sum = 0
    for price in order:
        sum += price['price']
    tax = round(sum * 0.15, 2)
    total = round(tax + sum, 2)
    names = []
    names = [item["name"] for item in order]
    return names, total

    raise NotImplementedError()


def print_order(order):
    print(f'You have ordered: {str(len(order))} items.')
    items = []
    items = [item["name"] for item in order]
    print(items)
    return order


def display_menu():
    print("---Menu---")
    for item in menu:
        print(
            f'{item}: {menu[item]["name"].capitalize() : <9} | {menu[item]["price"] : >5}')
    print()
    print('Order Three Items.')
    print('Select menu item number.')
    print()


def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input(f'Item number {str(count)} (from 1 to 5): ')
        count += 1
        order.append(menu[int(item)])
    return order


def main():
    newOrder = take_order()
    print_order(newOrder)

    subtotal = calculate_subtotal(newOrder)
    print("Subtotal for the order is: " + str(subtotal))

    tax = calculate_tax(subtotal)
    print("Tax for the order is: " + str(tax))

    items, subtotal = summarize_order(newOrder)


if __name__ == "__main__":
    main()
