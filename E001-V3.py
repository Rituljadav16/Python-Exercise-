# Exercise: E001-V3 : 
# Create one class named “location” with members “name”, “code”.
# Create one class named “movement” with members “from_location”, “to_location”, “product”, “quantity”.
# Create one static method named “movements_by_product” inside the “movement” class with one argument named “product”.
# --This method will return all “movement” objects which belong to the passed “product” as an argument.
# Add new members inside the product “stock_at_locations”. This new member is a type of Dictionary and it contains “location” as key and actual stock of that product on that location as value.
# Create 4 different location objects.
# Create 5 different product objects.
# Move those 5 products from one location to another location using movement. Manage exceptions if product stock goes in -ve. 
# Display movements of each product using the “movement_by_product” method.
# Display product details with its stock at various locations using “stock_at_locations”.
# Display product list by location ( group by location).

class Location:
    def __init__(self, name, code):
        self.name = name
        self.code = code

class Movement:
    def __init__(self,from_location,to_location,product,quantity):
        self.from_location = from_location
        self.to_location = to_location
        self.product = product 
        self.quantity = quantity
    
    @staticmethod
    def Movement_by_product(product):
        return [m for m in movements if m.product == product]
        
class Product:
    def __init__(self,product_name,product_code,stock_at_locations = None):
        self.product_name = product_name
        self.product_code = product_code
        self.stock_at_locations = stock_at_locations 

    def Display(self):
        print(f"\nProduct Name : {self.product_name}")
        print(f"Product Code : {self.product_code}")

    def Move(self,obj):
        if self.stock_at_locations.get(obj.from_location.name) < obj.quantity:
            raise ValueError("Insufficient stock at origin location")
        else:
            self.stock_at_locations[obj.from_location.name] -= obj.quantity
            self.stock_at_locations[obj.to_location.name] = self.stock_at_locations.get(obj.to_location.name,0) + obj.quantity
            movements.append(Movement(obj.from_location,obj.to_location,self,obj.quantity))

# Location Objects
Rajkot = Location("Rajkot","raj01")
Ahemdabad = Location("Ahemdabad","abd02")
Mumbai = Location("Mumbai","mum03")
Pune = Location("Pune","pun04")

location_list = [Rajkot,Ahemdabad,Mumbai,Pune]

# Product Objects
Phone = Product("Phone","pho",{Rajkot.name : 10,Ahemdabad.name:20})
Laptop = Product("Laptop","lap",{Mumbai.name:10,Rajkot.name:15})
Watch = Product("Watch","wat",{Mumbai.name:15,Ahemdabad.name:20})
Shoes = Product("Shoes","sho",{Ahemdabad.name:15,Pune.name:20})
TShirt = Product("Tshirt","tsh",{Pune.name:50,Mumbai.name:10})

product_list = [Phone,Laptop,Watch,Shoes,TShirt]

# Movement object
m1 = Movement(Rajkot,Ahemdabad,Phone,5)
m2 = Movement(Ahemdabad,Mumbai,Laptop,2)
m3 = Movement(Pune,Rajkot,Watch,4)
m4 = Movement(Mumbai,Ahemdabad,Shoes,8)
m5 = Movement(Ahemdabad,Rajkot,TShirt,10)

movements = []

# for i in product_list:
#     print(f"{i.product_name} : {i.stock_at_locations}\n")

try:
    product_list[0].Move(m5)
    product_list[1].Move(m1)
    product_list[2].Move(m2)
    product_list[3].Move(m3)
    product_list[4].Move(m4)
except ValueError as e:
    print(e)


for i in product_list:
    print(f"\n - - - - - - - - Product Name : {i.product_name} - - - - - - - - \n")
    print("Movement : \n")
    for j in m1.Movement_by_product(i):
        print(f"{j.from_location.name} -> {j.to_location.name} : {j.quantity}")

# # Stock Update        
print("\n - - - - - - - - - - Stock Update - - - - - - - - - - \n")
for i in product_list:
    print(f"{i.product_name} :- \n")
    for loc,price in i.stock_at_locations.items():
        print(f"{loc} - {price}")
    print("\n")

# # Product details
for i in product_list:
    i.Display()
    print("\n:::: Stock Details ::::")
    for loc,price in i.stock_at_locations.items():
        print(f"{loc} - {price}")

# Available Stock by location
for i in location_list:
    print("\n",i.name)
    print('---------------------')
    for j in product_list:
        for loc,sto in j.stock_at_locations.items():
            if loc == i.name:
                j.Display()
                print(f"Available Stock : {sto}")
