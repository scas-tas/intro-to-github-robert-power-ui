def add_item(inventory: dict, name: str, quantity: int) -> None:
    inventory[name] = quantity
    print(inv)
    pass
 
def remove_item(inventory: dict, name: str, quantity: int) -> None:
    pass
 
def get_stock_report(inventory: dict) -> str:
    pass


inv = {}
add_item(inv, 'apples', 10)
add_item(inv, 'bananas', 5)
get_stock_report(inv)
