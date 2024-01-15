# Python-Exercise-

Exercise: E001-V1
•	Create one class named "category" with members "name", "code", "no_of_products"
•	Create one class named "product" with members "name", "code", "category", "Price"
•	Create three objects of a category.
•	Create 10 different products. The code must be unique.
•	Print category info with its no_of_products
•	Sort and Print products based on price ( Price High to Low and Low to High) with all details.
•	Search product using its code.

Exercise: E001-V2

•  Add new data members “parent”, “display_name”, and “products” (list of product objects) inside the category class.
•  Add a new member function to generate “display_name”.
•  “display_name” has the text value as below.
           1.	Vehicle category without parent then “Vehicle” 
           2.	Car category with “Vehicle” as a parent then “Vehicle > Car”
           3.	Petrol category with “Car” as a parent then “Vehicle > Car > Petrol”
•  Create 5 category objects with parent and child relation.
•  Create 3 product objects in each category.
•  Display the Category with its Code, Display Name, and all product details inside that category.
•  Display product list by category (group by category, order by category name).

Exercise: E001-V3 : 
Create one class named “location” with members “name”, “code”.
Create one class named “movement” with members “from_location”, “to_location”, “product”, “quantity”.
Create one static method named “movements_by_product” inside the “movement” class with one argument named “product”.
--This method will return all “movement” objects which belong to the passed “product” as an argument.
Add new members inside the product “stock_at_locations”. This new member is a type of Dictionary and it contains “location” as key and actual stock of that product on that location as value.
Create 4 different location objects.
Create 5 different product objects.
Move those 5 products from one location to another location using movement. Manage exceptions if product stock goes in -ve. 
Display movements of each product using the “movement_by_product” method.
Display product details with its stock at various locations using “stock_at_locations”.
Display product list by location ( group by location).
