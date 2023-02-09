print ("Welcome To The 'Store Down The Block'")
print ("*************************************")

purchased_item = input ("What item are you purchasing?")
price = input (f"What is the price of {purchased_item}?")
quantity = input (f"How many {purchased_item} are you buying?")

subtotal = float(price) * int(quantity)

print (f"Added {quantity} {purchased_item} to shopping cart")
print (f"Subtotal: ${subtotal}")

