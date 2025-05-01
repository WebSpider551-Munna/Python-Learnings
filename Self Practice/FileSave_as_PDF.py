from datetime import datetime
from fpdf import FPDF

no_items = int(input(f"\nEnter Number of items to add: "))
items = []
quantities = []
prices = []
subtotals = []
grandtotal = 0

for i in range(no_items):
    print(f"\nEnter Item detials {i+1}: ")
    item = input(f"Enter item Name: ")
    qualtity = int(input(f"Enter qualtity: "))
    price = float(input(f"Enter price per item: "))

    items.append(item)
    quantities.append(qualtity)
    prices.append(price)

for i in range(no_items):
    subtotal = quantities[i] * prices[i]
    subtotals.append(subtotal)
    grandtotal+=subtotal

discount = (10/100)*grandtotal
tax = (5/100)*(grandtotal-discount)
total_payable = grandtotal-discount+tax

# Generate unique filename with date and time
now = datetime.now()
date_str = now.strftime("%d%b%Y").upper()
time_str = now.strftime("%H%M%S")
filename = f"Bill{date_str}{time_str}.pdf"

print(f"\n============================-:FINAL BILL:-===========================")
print(f"{'S.No':<15}{'Item':<15}{'Quntity':<15}{'Price':<15}{'Subtotal':<15}")
print("_" * 69)

for i in range(no_items):
    print(f"{i+1:<15}{items[i]:<15}{quantities[i]:<15}{prices[i]:<15.2f}{subtotals[i]:<15.2f}")
print("_" * 69)
print(f"{'Grandtotal: ':<59}:{grandtotal:.2f}")
print(f"{'Discount:(10%) ':<59}:{discount:.2f}")
print(f"{'tax:(5%) ':<59}:{tax:.2f}")
print("-" * 69)
print(f"{'Total Payable: ':<59}:{total_payable:.2f}")
print("-" * 69)
print("\n")

# Create PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", style="B", size=14)
pdf.cell(200, 10, "Final Bill", ln=True, align="C")
pdf.ln(10)

pdf.set_font("Arial", size=8)
pdf.cell(50, 10, "Item", border=1)
pdf.cell(30, 10, "Qty", border=1)
pdf.cell(40, 10, "Price", border=1)
pdf.cell(40, 10, "Subtotal", border=1)
pdf.ln()

# Add items
for i in range(no_items):
    pdf.cell(50, 10, items[i], border=1)
    pdf.cell(30, 10, str(quantities[i]), border=1)
    pdf.cell(40, 10, f"{prices[i]:.2f}", border=1)
    pdf.cell(40, 10, f"{subtotals[i]:.2f}", border=1)
    pdf.ln()

pdf.ln(5)
pdf.cell(160, 10, f"Grand Subtotal: {grandtotal:.2f}", ln=True)
pdf.cell(160, 10, f"Discount (10%): {discount:.2f}", ln=True)
pdf.cell(160, 10, f"Tax (5%): {tax:.2f}", ln=True)
pdf.cell(160, 10, f"Total Payable: {total_payable:.2f}", ln=True)

# Save PDF
pdf.output(filename)
print(f"✅ Bill has been saved as '{filename}'!")