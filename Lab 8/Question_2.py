# Using the dictionary created in the previous problem, allow the user to enter a dollar amount and print out all the products whose price is less than that amount.

def main():
    product_dict = {}
    while True:
        product = input("Enter product name: ")
        if product == "":
            break
        price = input("Enter price: ")
        product_dict[product] = price
    while True:
        amount = input("Enter amount: ")
        if amount == "":
            break
        for product in product_dict:
            if float(product_dict[product]) < float(amount):
                print(product)
    
main()