def add_fruit(inventory, fruit, quantity = 0):
    inventory[fruit] = inventory.get(fruit, 0) + quantity
    return None
new_inventory = {}
add_fruit(new_inventory, "strawberries", 10)
print("strawberries" in new_inventory)
print(new_inventory["strawberries"] == 10)
add_fruit(new_inventory, "strawberries", 25)
print(new_inventory["strawberries"] == 35)
