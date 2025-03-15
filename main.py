from product_manager import ProductManager
from product import Product
from cart import Cart


manager = ProductManager()

p1 = Product("Telefon", 50000, 10)
p2 = Product("Laptop", 120000, 5)
p3 = Product("Slusalice", 3000, 15)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)



cart = Cart()

cart.add_to_cart(p1)
cart.add_to_cart(p2)
cart.add_to_cart(p3)


manager.display_products()
print(f"Ukupna vrednost inventara: {manager.total_inventory_value()} RSD")

print("Sadržaj korpe:")
cart.display_cart()
print(f"Ukupna vrednost korpe: {cart.total_cart_value()} RSD")