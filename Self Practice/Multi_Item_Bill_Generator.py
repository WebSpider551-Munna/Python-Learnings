num_items = int(input("How many items do you want to add? "))

items = []
quantities = []
prices = []

#for i in range(num_items):
#  items.append(input("Enter item name: "))
#  quantities.append(input("Enter no.of quantity: "))
#  prices.append(input("Price per item: "))
for i in range(num_items):
    print(f"\nEnter details for Item {i+1}:")
    item = input("Item name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price per item: "))
    
    items.append(item)
    quantities.append(quantity)
    prices.append(price)
 
subtotals = []
grand_subtotal = 0

for i in range(num_items):
    subtotal = quantities[i] * prices[i]
    subtotals.append(subtotal)
    grand_subtotal += subtotal


discount = (10 / 100) * grand_subtotal
tax = (5 / 100) * (grand_subtotal - discount)
total_payable = grand_subtotal - discount + tax

print("\n========== FINAL BILL ==========")
print(f"{'Item':<15}{'Qty':<10}{'Price':<12}{'Subtotal':<12}")
print("-" * 50)

for i in range(num_items):
    print(f"{items[i]:<15}{quantities[i]:<10}{prices[i]:<12.2f}{subtotals[i]:<12.2f}")

print("-" * 50)
print(f"{'Grand Subtotal':<37}: {grand_subtotal:.2f}")
print(f"{'Discount (10%)':<37}: {discount:.2f}")
print(f"{'Tax (5%)':<37}: {tax:.2f}")
print(f"{'Total Payable':<37}: {total_payable:.2f}")

