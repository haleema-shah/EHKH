       # Welcome User
userName=input("Please Enter Your Name")
welcomeMessage=f"Welcome to BanoQabil Store{userName}"
lenWCMsg=len(welcomeMessage)
print("-"*lenWCMsg)
print(welcomeMessage)
print("-"*lenWCMsg)

# _Shopping Cart_ #

cart = {}

while True:
    product = input("Enter a product to buy (q to quit): ")
    if product == 'q' or product == 'q':
        break
    else:
        price = int(input("Enter the amount you want to purchase: RS"))
        cart[product] = price
        for product, price in cart.items():
            print(f"{product} : RS{price}")

print("----- YOUR CART -----")

sum = 0
for product, price in cart.items():
    print(f"{product} : RS{price}")
    sum+=price
print("The total cost for all items purchased is RS{0}".format(sum))

print("Thank you for buying from us, we look forward to having you another time")