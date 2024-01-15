# Exercise: E001-V2
# •  Add new data members “parent”, “display_name”, and “products” (list of product objects) inside the category class.
# •  Add a new member function to generate “display_name”.
# •  “display_name” has the text value as below.
#            1.	Vehicle category without parent then “Vehicle” 
#            2.	Car category with “Vehicle” as a parent then “Vehicle > Car”
#            3.	Petrol category with “Car” as a parent then “Vehicle > Car > Petrol”
# •  Create 5 category objects with parent and child relation.
# •  Create 3 product objects in each category.
# •  Display the Category with its Code, Display Name, and all product details inside that category.
# •  Display product list by category (group by category, order by category name).

class Category:

    def __init__(self, category_name, category_code,parent = None):
        self.category_name = category_name
        self.category_code = category_code
        self.no_of_products = 0
        self.parent = parent
        self.display_name = self.Generate_display_name()
        self.products = []

    def Generate_display_name(self):
        self.display_name = self.category_name
        if self.parent:
            self.display_name = self.parent.Generate_display_name() + " > " + self.display_name

        return self.display_name
    
    def __str__(self):
        if self.parent:
            return f"\nCategory Name : {self.category_name} \n Category Code : {self.category_code} \n No of Productes : {self.no_of_products} \n Parent Name : {self.parent.category_name} \n Display Name : {self.display_name}  \n"
        else:
            return f"Category Name : {self.category_name} \n Category Code : {self.category_code} \n No of Productes : {self.no_of_products} \n Parent Name : None \n Display Name : {self.display_name}  \n"
            

    def Sorting(self,categories_list):

        print("\n  = = = = = = = = = = Sorted Categories  = = = = = = = = = =  \n")
        for i in range(len(categories_list)):
            for j in range(0,len(categories_list)-1):
                if categories_list[j].category_name > categories_list[j+1].category_name:
                    categories_list[j],categories_list[j+1] = categories_list[j+1],categories_list[j]
        for i in categories_list:
            print("\n - - - - - - - - - Category : {0} - - - - - - - - - " .format(i.category_name))
            print(i)
            for j in i.products:
                j.Display_Product()

class Product:
    def __init__(self, product_name, product_code, product_category,product_price):
        self.product_name = product_name
        self.product_code = product_code
        self.product_category = product_category
        self.product_price = product_price
        product_category.no_of_products += 1

    def Display_Product(self):
        print("\nProduct Name : {0} ".format(self.product_name))
        print("Product Code : {0} ".format(self.product_code))
        print("Product Category : {0} ".format(self.product_category.category_name))
        print("Product Price : {0} ".format(self.product_price))
    
vehicle = Category("Vehicle","Vh")
car = Category("Car","Ca",vehicle)
bike = Category("Bike","Bk",vehicle)
petrol = Category("Petrol","Pet",car)
diesel = Category("Diesel","Dsl",car)

vehicle.products.append(Product("Tyre","Vh-P1",vehicle,1800))
vehicle.products.append(Product("Engine","Vh-P2",vehicle,150000))
vehicle.products.append(Product("Headlight","Vh-P3",vehicle,4000))

car.products.append(Product("SUV","Car-P1",car,8000000))
car.products.append(Product("Sedan","Car-P2",car,5000000))
car.products.append(Product("Sports Car","Car-P2",car,12000000))

bike.products.append(Product("Scooter","Bk-P1",bike,60000))
bike.products.append(Product("Street Bike","Bk-P2",bike,80000))
bike.products.append(Product("Sports Bike","Bk-P3",bike,100000))

petrol.products.append(Product("Regular","Rp",petrol,60))
petrol.products.append(Product("Premium","Rp",petrol,80))
petrol.products.append(Product("Power","Rp",petrol,70))

diesel.products.append(Product("Regular","Rd",diesel,55))
diesel.products.append(Product("Premium","Pd",diesel,75))
diesel.products.append(Product("Bio","Bd",diesel,65))

categories_list = [vehicle, car, bike, petrol, diesel]

for i in categories_list:
    print(i)

vehicle.Sorting(categories_list)


