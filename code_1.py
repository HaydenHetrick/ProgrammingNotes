menu_item = {"Hamburger": 2.99, "French Frys": 0.99, "Sea Salt Frys": 1.99, "Milk Shake": 4.99}

customer_1_item = "Hamburger"  # Assuming the customer ordered a Hamburger
item_price = menu_item.get(customer_1_item)

if item_price is not None:
    print(f"Customer 1 Ordered {customer_1_item} for ${item_price}")
else:
    print(f"Item {customer_1_item} is not on the menu.")
