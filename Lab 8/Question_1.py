# Write a program that repeatedly asks the user to enter product names and prices. Store all of these in a dictionary whose keys are the product names and whose values are the prices.
# When the user is done entering products and prices, allow them to repeatedly enter a product name and print the corresponding price or a message indicating that the product is not in the dictionary.

def main():
    product_dict = {}
    while True:
        product = input("Enter product name: ")
        if product == "":
            break
        price = input("Enter price: ")
        product_dict[product] = price
    while True:
        product = input("Enter product name: ")
        if product == "":
            break
        if product in product_dict:
            print(product_dict[product])
        else:
            print("Product not in dictionary")
        
main()