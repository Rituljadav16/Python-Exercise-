# •	Create one class named "category" with members "name", "code", "no_of_products"
# •	Create one class named "product" with members "name", "code", "category", "Price"
# •	Create three objects of a category.
# •	Create 10 different products. The code must be unique.
# •	Print category info with its no_of_products
# •	Sort and Print products based on price ( Price High to Low and Low to High) with all details.
# •	Search product using its code.

class Category:

    def __init__(self, category_name, category_code):
        self.category_name = category_name
        self.category_code = category_code
        self.no_of_products = 0

    def Show_Category(self):
        print("\nCategory Name : {0}".format(self.category_name))    
        print("Category Code : {0}".format(self.category_code))    
        print("No of products : {0}".format(self.no_of_products))   
        
class Product:
    def __init__(self, product_name, product_code, product_category,product_price):
        self.product_name = product_name
        self.product_code = product_code
        self.product_category = product_category
        self.product_price = product_price
        product_category.no_of_products += 1
        
    def Show_Product(self):
        print("\nProduct Name : {0}".format(self.product_name))
        print("Product Code : {0}".format(self.product_code))
        print("Product Category : {0}".format(self.product_category.category_name))
        print("Product Price : {0}".format(self.product_price))

    def Search(self,count = 0):
        input_product_code = input("\nEnter Product code to search : ")

        for i in product_list:
            if i.product_code == input_product_code:
                i.Show_Product()
                break
            count += 1
        else:
            print("\nProduct not found!!")
           
    def High_to_Low(self):

        print("\n - - - - - - - Sorted by price (High to Low) - - - - - - - \n")

        for i in range(len(product_list)):
            for j in range(i+1,len(product_list)):
                if product_list[i].product_price < product_list[j].product_price:
                    temp = product_list[i]
                    product_list[i] = product_list[j]
                    product_list[j] = temp
            product_list[i].Show_Product()

    def Low_to_High(self):

        print("\n - - - - - - - Sorted by price (Low to High) - - - - - - - \n")

        for i in range(len(product_list)):
            for j in range(i+1,len(product_list)):
                if product_list[i].product_price > product_list[j].product_price:
                    temp = product_list[i]
                    product_list[i] = product_list[j]
                    product_list[j] = temp
            product_list[i].Show_Product() 

c1 = Category("veg","vg001")
c2 = Category("Non-veg","nv001")
c3 = Category("vegan","ve001")

        
# vag 
product1 = Product("Burger","p01",c1,120)
product2 = Product("Pizza","p02",c1,250)
product3 = Product("Paneer-chilly","p03",c1,360)
product4 = Product("Fride-rice","p04",c1,150)
# Non-Veg
product5 = Product("Egg","p05",c2,20)
product6 = Product("Egg-fride-rice","p06",c2,160)
product7 = Product("Egg-Chizz-roll","p07",c2,260)
product8 = Product("Chikan-Butter-masala","p08",c2,400)
# vegan
product9 = Product("Nuts","p09",c3,230)
product10 = Product("Seaweed","p10",c3,250)

# list of all Category
Category_list = [c1,c2,c3]

# list of all all product
product_list = [product1,product2,product3,product4,product5,product6,product7,product8,product9,product10]

# To print all Category with Category Count
for i in Category_list:
    i.Show_Category()


# Object Calling

product1.Search()
product1.High_to_Low()
product1.Low_to_High()

          