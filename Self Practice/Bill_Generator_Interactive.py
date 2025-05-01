item = input("Enter item name: ")
quantity = int(input("Enter quantity: "))
price_per_item = float(input("Enter price per item: "))

subtotal = quantity * price_per_item
discount = (10 / 100) * subtotal
tax = (5 / 100) * (subtotal - discount)
total = subtotal - discount + tax

print("\n----- BILL -----")
print(f"{'Item':<15}: {item}")
print(f"{'Quantity':<15}: {quantity}")
print(f"{'Price/item':<15}: {price_per_item:.2f}")
print(f"{'Subtotal':<15}: {subtotal:.2f}")
print(f"{'Discount (10%)':<15}: {discount:.2f}")
print(f"{'Tax (5%)':<15}: {tax:.2f}")
print(f"{'Total Payable':<15}: {total:.2f}")