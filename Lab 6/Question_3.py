# Write a program in Python that repeatedly asks the user to enter product names and prices.

Product = {}
Element = 5
while Element != 0:
    ProductName = input("Enter a product name: ")
    if ProductName == "":
        break
    ProductPrice = input("Enter a product price: ")
    Product[ProductName] = ProductPrice
    Element -= 1

# Print Dictionary
print("\nProduct\t\tPrice")
for i in Product:
    print(i, "\t\t", Product[i])

# Search for a product
ProductSearch = input("Enter a product name to search: ")
if ProductSearch in Product:
    print("Price of", ProductSearch, "is", Product[ProductSearch])