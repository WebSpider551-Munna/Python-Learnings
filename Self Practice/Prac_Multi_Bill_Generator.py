no_items = int(input(f"\nEnter Number of items to add: "))
items = []
qunatities = []
prices = []

for i in range(no_items):
    print(f"\nEnter Item detials {i+1}: ")
    item = input(f"Enter item Name: ")
    qualtity = int(input(f"Enter qualtity: "))
    price = float(input(f"Enter price per item: "))

    items.append(item)
    qunatities.append(qualtity)
    prices.append(price)

subtotals = []
grandtotal = 0
for i in range(no_items):
    subtotal = qunatities[i] * prices[i]
    subtotals.append(subtotal)
    grandtotal+=subtotal

discount = (10/100)*grandtotal
tax = (5/100)*(grandtotal-discount)
total_payable = grandtotal-discount+tax

print(f"\n============================-:FINAL BILL:-===========================")
print(f"{'S.No':<15}{'Item':<15}{'Quntity':<15}{'Price':<15}{'Subtotal':<15}")
print("_" * 69)

for i in range(no_items):
    print(f"{i+1:<15}{items[i]:<15}{qunatities[i]:<15}{prices[i]:<15.2f}{subtotals[i]:<15.2f}")
print("_" * 69)
print(f"{'Grandtotal: ':<59}:{grandtotal:.2f}")
print(f"{'Discount:(10%) ':<59}:{discount:.2f}")
print(f"{'tax:(5%) ':<59}:{tax:.2f}")
print("-" * 69)
print(f"{'Total Payable: ':<59}:{total_payable:.2f}")
print("-" * 69)
print("\n")