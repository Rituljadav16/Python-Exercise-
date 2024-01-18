# Exercise: E002
# •	Create a new class named "Customer" with below members. "name","email","phone","street","city","state","country","company","type".
# •	"type" must be from "company,contact,billing,shipping".
# •	"Company" must be a Customer object which is the parent object.
# •	Apply Multiple possible validation for phone number and email
# •	Does not allowed number in name,city,state and country

# •	Create a new class named "Order" with members "number","date", "company", "billing", "shipping", "total_amount","order_lines".
# •	"company", "billing", "shipping" are objects of Customer.
# •	"date" must be today or the future. Does not allow past date.
# •	"total_amount" auto calculated based on different products inside order.
# •	"order_lines" is list of objects of "OrderLine"

# •	create a new class named "OrderLine" with members "order", "product", "quantity", "price", "subtotal".
# •	"order" is the object of Order.
# •	"subtotal" is auto calculated based on quantity and price.

# •	Display Order and Customer Information
# •	Sort orders based on "date".
# •	User can filter the current month orders
# •	Search Orders from its number.
# •	List/Display all orders of a specific product.
import re,sys,datetime

class Customer:
    def __init__(self, name, email, phone, street, city, state, country, company, type):
        if type not in ["company","contact","billing","shipping"]:
            print("Invalid type. Must be one of: company, contact, billing, shipping")
            sys.exit()
        self.validate_and_set_attrs(
            name, r"^[a-zA-Z]+$", "name",
            city, r"^[a-zA-Z]+$", "city",
            state, r"^[a-zA-Z]+$", "state",
            country, r"^[a-zA-Z]+$", "country",
            email, r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', "email",
            phone, r"(0|91)?[6-9]\d{9}", "phone"
        )
        self.street = street
        self.company = company
        self.type = type

    def validate_and_set_attrs(self, *args):
        for value, pattern, attr_name in zip(*[iter(args)] * 3):
            if re.match(pattern, value):
                setattr(self, attr_name, value)
            else:
                print(f"Invalid value for {attr_name}. Please enter a valid {attr_name}.")
                sys.exit()

    def Display(self):
        print(f"\nName : {self.name}")
        print(f"Email : {self.email}")
        print(f"Phone : {self.phone}")
        print(f"Address : {self.street}, {self.city}, {self.state}, {self.state}, {company.country}")
        print(f"Company : {company.name}")
        print(f"Type : {self.type}")

class OrderLine:
    def __init__(self, order, product, quantity, price):
        self.order = order
        self.product = product
        self.quantity = quantity
        self.price = price
        self.subtotal = self.quantity * self.price
    
    def Display_Orderline(self):
        print(f"\nOrder : {self.order}")
        print(f"Product : {self.product}")
        print(f"Quantity : {self.quantity}")
        print(f"Price : {self.price}")
        print(f"Sub-Total : {self.subtotal}")

class Order:
    def __init__(self,number,date,company,billing,shipping,order_lines):
        self.number = number
        self.set_date(date)
        self.company = company
        self.billing = billing
        self.shipping = shipping
        self.order_lines = order_lines
        self.total_amount = self.calculate_total_amount()
    
    def set_date(self, date):
        if date < datetime.date.today():
            print("\nDate cannot be in the past.\n")
            sys.exit()
        self.date = date
    
    def calculate_total_amount(self):
        total = 0
        for order_line in self.order_lines:
            total += order_line.subtotal
        return total

    def display_order_and_customer(self):

        print(f"\nOrder Number : {self.number}")
        print(f"Date : {self.date}")

        print("\nBiling Customar Info :- \n")

        print(f"Name : {self.billing.name}")
        print(f"Email : {self.billing.email}")
        print(f"Phone : {self.billing.phone}")
        print(f"Billing : {self.billing.street}, {self.billing.city}, {self.billing.state}, {self.billing.country}")

        print("\nShipping Customar Info :- \n")

        print(f"Name : {self.shipping.name}")
        print(f"Email : {self.shipping.email}")
        print(f"Phone : {self.shipping.phone}")
        print(f"Shipping : {self.shipping.street}, {self.shipping.city}, {self.shipping.state}, {self.shipping.country}")

        print(f"\nOrder Info :- ")
        for i in self.order_lines:
            print(f"Product No : {i.order.number},  Name : {i.product},  Price : {i.price},  Qty : {i.quantity},  Sub_total : {i.subtotal}")

        print(f"\nTotal Amount : {self.total_amount}\n")
        print("--------------------------------------------------------------------------------------------------------------")
    
    def sort_orders_by_date(self,list_of_order):
        for i in range(len(list_of_order)):
            for j in range(i+1,len(list_of_order)):
                if list_of_order[i].date > list_of_order[j].date:
                    temp = list_of_order[i]
                    list_of_order[i],list_of_order[j] = list_of_order[j],temp

    def display_orders_of_specific_product(self,list_of_order, product_name):
        filtered_orders = [order for order in list_of_order for order_line in order.order_lines if order_line.product == product_name]
        for order in filtered_orders:
            print(f"Order Number: {order.number}")
            print(f"Order Date: {order.date}")
            print(f"Total Amount: {order.total_amount}\n")
    
    def Search(self,search,found = False):
        for i in list_of_order:
            if i.number == search:
                i.display_order_and_customer()
                found = True
        if not found:
            print("Not found...")

# customer object
company = Customer("Relution","relution@gmail.com","919913317632","walking street","Ahemdabad","Gujarat","India",None,"company")
billing = Customer("Ritul", "Ritul@gmail.com", "919913317638", "billing street", "Rajkot", "Gujarat", "India", company, "billing")
shipping = Customer("Ankur", "Ankur@gmail.com", "919913317639", "shipping street", "Amreli", "Gujarat", "India", company, "shipping")

customer_list = [company,billing,shipping]

# order line object
ol_1 = OrderLine(None,"Laptop",5,1000)
ol_2 = OrderLine(None,"Phone",2,10000)
ol_3 = OrderLine(None,"Watch",5,500)
ol_4 = OrderLine(None,"Shirt",10,800)
ol_5 = OrderLine(None,"TShirt",4,400)

ol_list = [ol_1,ol_2,ol_3,ol_4,ol_5]

# order object
order_1 = Order(1,datetime.date(2024,1,17),company,billing,shipping,[ol_1,ol_2])
order_2 = Order(2,datetime.date(2024,1,18),company,billing,shipping,[ol_2,ol_3])
order_3 = Order(3,datetime.date(2024,2,26),company,billing,shipping,[ol_3,ol_5])
order_4 = Order(4,datetime.date(2024,3,1),company,billing,shipping,[ol_5,ol_4]) 
order_5 = Order(5,datetime.date(2024,2,1),company,billing,shipping,[ol_4,ol_1]) 
 
list_of_order = [order_1,order_2,order_3,order_4,order_5]

ol_1.order = order_1
ol_2.order = order_2
ol_3.order = order_3
ol_4.order = order_4
ol_5.order = order_5

# Sort orders based on "date"
order_1.sort_orders_by_date(list_of_order)

# Display Order and Customer Information
for i in list_of_order:
    i.display_order_and_customer()


# User can filter the current month orders
print("--------------------------------------------Current month orders------------------------------------------------------")
for i in list_of_order:
    if datetime.date.today().month == i.date.month:
        i.display_order_and_customer()

# •	List/Display all orders of a specific product.
for i in ol_list:
    print(f"\n-----------------------{i.product}---------------------------\n")
    order_1.display_orders_of_specific_product(list_of_order, i.product)

# •	Search Orders from its number.
search = int(input("Enter Order number to search : "))
order_1.Search(search)


    