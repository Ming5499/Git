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
    items = [item["price"] for item in order]
    return round(sum(items),2)


    raise NotImplementedError()

def calculate_tax(subtotal):
   
    print('Calculating tax from subtotal...')
    sub = float(subtotal)
    sub *= 0.15
    return round(sub, 2)
    raise NotImplementedError()

def summarize_order(order):
    print_order(order)
    
    items = [item["price"] for item in order]
    subtotal = 0.0
    for x in items:
        subtotal += x
    tax = subtotal * 15 / 100
    tax = round(tax, 2)
    total = round(subtotal + tax, 2)
    names = []
    names = [item["name"] for item in order]
    return names, total
    raise NotImplementedError()


def print_order(order):
    print('You have ordered ' + str(len(order)) + ' items')
    items = []
    items = [item["name"] for item in order]
    print(items)
    return order


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
    print_order(order)
    
    subtotal = calculate_subtotal(order)
    print("Subtotal for the order is: " + str(subtotal))

    
    print("Tax for the order is: " + str(calculate_tax(subtotal)))

    item ,subtotal = summarize_order(order)

if __name__ == "__main__":
    main()