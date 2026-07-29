def add_item(inventory: dict, name: str, quantity: int) -> None:
    if name in inv:
        inventory[name] = inventory[name] + quantity
    else:
        inventory[name] = quantity
    print(inv)
    pass
 
def remove_item(inventory: dict, name: str, quantity: int) -> None:
    if name in inv:
        inventory[name] = inventory[name] - quantity
        if inventory[name] <= 0:
            inventory[name] = 0
    else:
        pass
    print(inv)
    pass
 
def get_stock_report(inventory: dict) -> str:
    pass


inv = {'apples': 5,
       'mangos': 4129,
       'bananas': 150}
add_item(inv, 'apples', 10)
remove_item(inv, 'bananas', 5)
get_stock_report(inv)
