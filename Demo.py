class Location:
    def __init__(self, name, code):
        self.name = name
        self.code = code

class Movement:
    movements = []

    def __init__(self, from_location, to_location, product, quantity):
        self.from_location = from_location
        self.to_location = to_location
        self.product = product
        self.quantity = quantity
        self.update_stock()

    def update_stock(self):
        if self.product.stock_at_locations.get(self.from_location.name, 0) < self.quantity:
            raise ValueError("Insufficient stock at origin location")
        else:
            self.product.stock_at_locations[self.from_location.name] -= self.quantity
            self.product.stock_at_locations[self.to_location.name] = (
                self.product.stock_at_locations.get(self.to_location.name, 0) + self.quantity
            )
            Movement.movements.append(self)

    @staticmethod
    def movements_by_product(product):
        return [m for m in Movement.movements if m.product == product]

class Product:
    def __init__(self, product_name, product_code, stock_at_locations=None):
        self.product_name = product_name
        self.product_code = product_code
        self.stock_at_locations = stock_at_locations if stock_at_locations else {}

    def display(self):
        print(f"\nProduct Name : {self.product_name}")
        print(f"Product Code : {self.product_code}")

    def move(self, movement):
        movement.update_stock()

# Location Objects
Rajkot = Location("Rajkot", "raj01")
Ahmedabad = Location("Ahmedabad", "abd02")
Mumbai = Location("Mumbai", "mum03")
Pune = Location("Pune", "pun04")

location_list = [Rajkot, Ahmedabad, Mumbai, Pune]

# Product Objects
Phone = Product("Phone", "pho", {Rajkot.name: 10, Ahmedabad.name: 20})
Laptop = Product("Laptop", "lap", {Mumbai.name: 10, Rajkot.name: 15})
Watch = Product("Watch", "wat", {Mumbai.name: 15, Ahmedabad.name: 20})
Shoes = Product("Shoes", "sho", {Ahmedabad.name: 15, Pune.name: 20})
TShirt = Product("Tshirt", "tsh", {Pune.name: 50, Mumbai.name: 10})

product_list = [Phone, Laptop, Watch, Shoes, TShirt]

# Movement object
m1 = Movement(Rajkot, Ahmedabad, Phone, 5)
m2 = Movement(Ahmedabad, Mumbai, Laptop, 2)
m3 = Movement(Pune, Rajkot, Watch, 4)
m4 = Movement(Mumbai, Ahmedabad, Shoes, 8)
m5 = Movement(Ahmedabad, Rajkot, TShirt, 10)

# Handle movements
try:
    for movement in [m5, m1, m2, m3, m4]:
        movement.update_stock()
except ValueError as e:
    print(e)

# Display movements by product
for product in product_list:
    print(f"\n - - - - - - - - Product Name : {product.product_name} - - - - - - - - \n")
    print("Movement : \n")
    for movement in Movement.movements_by_product(product):
        print(f"{movement.from_location.name} -> {movement.to_location.name} : {movement.quantity}")

# Stock Update
print(" - - - - - - - - - - Stock Update - - - - - - - - - - \n")
for product in product_list:
    print(f"{product.product_name} :- \n")
    for loc, price in product.stock_at_locations.items():
        print(f"{loc} - {price}")
    print("\n")

# Product details
for product in product_list:
    product.display()
    print("\n:::: Stock Details ::::")
    for loc, price in product.stock_at_locations.items():
        print(f"{loc} - {price}")

# Available Stock by location
for location in location_list:
    print("\n", location.name)
    print('---------------------')
    for product in product_list:
        stock = product.stock_at_locations.get(location.name, 0)
        if stock:
            product.display()
            print(f"Available Stock : {stock}")
