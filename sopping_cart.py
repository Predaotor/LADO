products = [
    {"name": "SmartPhone", "price": 500, "description": "Smart device"},
    {"name": "Laptop", "price": 1200, "description": "Portable Pc"},
    {"name": "Headphones", "price": 140, "description": "A pair of earphones"},
    {"name": "Smartwatch", "price": 100, "description": "Smart hand device"},
    {"name": "Bluetooth_speaker", "price": 120, "description": "Bluetooth device"}
]

cart = []

while True:
    choice = input("Do you want to continue shopping? (yes/no): ")
    
    if choice.lower() == "yes":
        print("\nList of products and prices:")
        for index, product in enumerate(products):
            print(f"{index}: {product['name']}, {product['description']}, {product['price']}$")
        
        try:
            product_id = int(input("\nEnter the ID of the product you want to buy: "))
            if 0 <= product_id < len(products):
                cart.append(products[product_id])
                print(f"\nAdded {products[product_id]['name']} to your cart.\n")
            else:
                print("\nInvalid product ID. Please try again.\n")
        except ValueError:
            print("\nPlease enter a valid number.\n")
    else:
        break

# Display the final cart and total price
if cart:
    print("\nThank you for shopping! Your final cart contents are:\n")
    print(f"{'Product Name':<20} {'Price ($)':<10}")
    print("=" * 30)
    
    total_price = 0
    for item in cart:
        print(f"{item['name']:<20} {item['price']:<10}")
        total_price += item['price']
    
    print("=" * 30)
    print(f"{'Total':<20} {total_price}$")
else:
    print("\nYour cart is empty. Thank you for visiting!")
