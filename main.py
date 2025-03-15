from product_manager import ProductManager
from product import Product

manager = ProductManager()

# Dodavanje proizvoda
p1 = Product("Telefon", 50000, 10)
p2 = Product("Laptop", 120000, 5)
p3 = Product("Slusalice", 3000, 15)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

# Prikaz svih proizvoda i ukupne vrednosti
manager.display_products()
print(f"Ukupna vrednost inventara: {manager.total_inventory_value()} RSD")