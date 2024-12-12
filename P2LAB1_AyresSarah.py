#Sarah Ayres
#10-12-2024
#P2LAB1
# A program to sell Items
#------------------------
#Function to calculate Total price
def calculate_total(price_per_item, amount):
    return price_per_item * amount

#Get User Input
item_name = input("What are you buying?  ")
amount = int(input("How many of this item do you want?  "))
price_per_item = float(input("What is the price of one of these items?  $"))


#Calculate Total Price
total_price = calculate_total(price_per_item, amount)

#Print out the details
print("-------------------------------------------")
print("\nReceipt:")
print(f"Item: {item_name}")
print(f"Quantity: {amount}")
print(f"Price per item: ${price_per_item:.2f}")
print(f"Total: ${total_price:.2f}")

