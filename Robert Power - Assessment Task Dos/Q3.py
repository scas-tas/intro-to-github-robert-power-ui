#the function that represents the process of adding an item to inventory or increasing its quantity.
def add_item(inventory: dict, name: str, quantity: int) -> None:
    if name in inventory: #checks whether the item is already in the inventory or not.
        inventory[name] = inventory[name] + quantity #adds the quantity chosen to the pre-existing item, rather than creating a new one.
    else: #if the item is not in the inventory already,
        inventory[name] = quantity #adds the item and its quantity to the inventory.
    pass #ends the function
#the function that represents the process of removing an item from the inventory or decreasing its quantity.
def remove_item(inventory: dict, name: str, quantity: int) -> None:
    if name in inventory: #checks whether the item is already in the inventory or not.
        inventory[name] = inventory[name] - quantity #removes the quantity chosen from the pre-existing item
        if inventory[name] <= 0: #checks whether the item's quantity is at 0 or below (somehow).
            inventory[name] = 0 #sets the quantity to zero to avoid it going negative.
            del inventory[name] #deletes the item from the inventory.
    else:
        pass #disregards the function if the item isn't in the inventory at the moment.
    pass

 #the function that represents the process of printing the inventory to the screen.
def get_stock_report(inventory: dict) -> str:
    for item in sorted(inventory): #lists through each item in the inventory after alphabetisising them.
        print(f"{item}: {inventory[item]}") #prints a string involving the item and its quantity.
    pass


inv = {}
add_item(inv, 'apples', 10)
add_item(inv, 'bananas', 5)
get_stock_report(inv)
add_item(inv, 'apples', 5)
remove_item(inv, 'bananas', 10)
get_stock_report(inv)
remove_item(inv, 'oranges', 3)
get_stock_report(inv)
