# •	Create one class named "category" with members "name", "code", "no_of_products"
# •	Create one class named "product" with members "name", "code", "category", "Price"
# •	Create three objects of a category.
# •	Create 10 different products. The code must be unique.
# •	Print category info with its no_of_products
# •	Sort and Print products based on price ( Price High to Low and Low to High) with all details.
# •	Search product using its code.

class Category:

    def __init__(self, category_name, category_code,no_of_products):
        self.category_name = category_name
        self.category_code = category_code
        self.no_of_products = no_of_products

    def Show_Category(self):
        print("\nCategory Name : {:^4}".format(self.category_name))    
        print("Category Code : {:^4}".format(self.category_code))    
        print("No of products : {:^4}".format(self.no_of_products))       
        
class Product:
    def __init__(self, product_name, product_code, product_category,product_price):
        self.product_name = product_name
        self.product_code = product_code
        self.product_category = product_category
        self.product_price = product_price

    def Show_Product(self):
        print("\nProduct Name : {:^4}".format(self.product_name))
        print("Product Code : {:^4}".format(self.product_code))
        print("Product Category : {:^4}".format(self.product_category))
        print("Product Price : {:^4}".format(self.product_price))

# vag 
product1 = Product("Burger","p01","veg",120)
product2 = Product("Pizza","p02","veg",250)
product3 = Product("Paneer-chilly","p03","veg",360)
product4 = Product("Fride-rice","p04","veg",150)
# Non-Veg
product5 = Product("egg","p05","Non-veg",20)
product6 = Product("Egg-fride-rice","p06","Non-veg",160)
product7 = Product("Egg-Chizz-roll","p07","Non-veg",260)
product8 = Product("Chikan-Butter-masala","p08","Non-veg",400)
# vegan
product9 = Product("Nuts","p09","vegan",230)
product10 = Product("Seaweed","p10","vegan",250)

# list of all object
product_list = [product1,product2,product3,product4,product5,product6,product7,product8,product9,product10]

# to print all Product

# for i in product_list:
#     i.Show_Product()

def category_veg(product_count = 0):
    for i in product_list:
        if i.product_category == "veg":
            product_count += 1
    return product_count

def category_Nonveg(product_count = 0):
    for i in product_list:
        if i.product_category == "Non-veg":
            product_count += 1
    return product_count

def category_vegan(product_count = 0):
    for i in product_list:
        if i.product_category == "vegan":
            product_count += 1
    return product_count

c1 = Category("veg","vg001",category_veg())
c2 = Category("Non-veg","nv001",category_Nonveg())
c3 = Category("vegan","ve001",category_vegan())

Category_list = [c1,c2,c3]

# To print all Category

# for i in Category_list:
#     i.Show_Category()

# Searching
def Search(flag = False,count = 1):
    input_product_code = input("Enter Product code to search : ")

    for i in product_list:
            if i.product_code == input_product_code:
                flag = True
                break
            else:
                flag = False
            count +=1
    if flag:
        print("\nProduct Name : {0}".format(product_list[count].product_name))
        print("Product Code : {0}".format(product_list[count].product_code))
        print("Product Category : {0}".format(product_list[count].product_category))
        print("Product Price : {0}".format(product_list[count].product_price))
    else:
        print("\nProduct not found!!")

#Sorting Price High to Low
def High_to_Low():

    print("\n - - - - - - - Sorted by price (High to Low) - - - - - - - \n")

    for i in range(len(product_list)):
        for j in range(i+1,len(product_list)):
            if product_list[i].product_price < product_list[j].product_price:
                temp = product_list[i].product_price
                product_list[i].product_price = product_list[j].product_price
                product_list[j].product_price = temp

    for i in product_list:
        i.Show_Product()

#Sorting Price Low to High
def Low_to_High():

    print("\n - - - - - - - Sorted by price (Low to High) - - - - - - - \n")

    for i in range(len(product_list)):
        for j in range(i+1,len(product_list)):
            if product_list[i].product_price > product_list[j].product_price:
                temp = product_list[i].product_price
                product_list[i].product_price = product_list[j].product_price
                product_list[j].product_price = temp

    for i in product_list:
        i.Show_Product()    
        

Search() 
High_to_Low()
Low_to_High()
