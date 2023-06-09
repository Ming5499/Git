menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee', 
        "price": 2.50},
    3: {"name": 'cake', 
        "price": 2.79},
    4: {"name": 'soup', 
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
}

def calculate_subtotal(order):
    print('Calculating bill subtotal...')
    items = []
    items = [float(item["price"]) for item in order]
    print(items)
    return round(max(items),2)


def display_menu():
    print("------- Menu -------")
    for choice in menu:
        print(f"{choice}. {menu[choice]['name'] : <9} | {menu[choice]['price'] :>5}")
    print()


def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input('Select menu item number ' + str(count) + ' (from 1 to 5): ')
        count += 1
        order.append(menu[int(item)])
    return order

def main():
    order = take_order()
    
    subtotal = calculate_subtotal(order)
    print("Subtotal for the order is: " + str(subtotal))

if __name__ == "__main__":
    main()