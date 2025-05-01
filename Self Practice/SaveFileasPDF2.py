from datetime import datetime
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Final Bill", 0, 1, "C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, title, 0, 1, "L", 1)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font("Arial", "", 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_table(self, items, quantities, prices, subtotals):
        self.set_fill_color(224, 235, 255)
        self.set_text_color(0)
        self.set_draw_color(128, 0, 0)
        self.set_line_width(.3)
        self.set_font("Arial", "B", 10)
        self.cell(50, 10, "Item", 1, 0, "C", 1)
        self.cell(30, 10, "Qty", 1, 0, "C", 1)
        self.cell(40, 10, "Price", 1, 0, "C", 1)
        self.cell(40, 10, "Subtotal", 1, 0, "C", 1)
        self.ln()
        self.set_font("Arial", "", 10)
        for i in range(len(items)):
            self.cell(50, 10, items[i], 1)
            self.cell(30, 10, str(quantities[i]), 1)
            self.cell(40, 10, f"{prices[i]:.2f}", 1)
            self.cell(40, 10, f"{subtotals[i]:.2f}", 1)
            self.ln()

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
    grandtotal += subtotal

discount = (10 / 100) * grandtotal
tax = (5 / 100) * (grandtotal - discount)
total_payable = grandtotal - discount + tax

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
pdf = PDF()
pdf.add_page()
pdf.chapter_title("Bill Summary")
pdf.add_table(items, quantities, prices, subtotals)
pdf.ln(5)
pdf.set_font("Arial", "B", 10)
pdf.cell(0, 10, f"Grand Subtotal: {grandtotal:.2f}", ln=True, align="R")
pdf.cell(0, 10, f"Discount (10%): {discount:.2f}", ln=True, align="R")
pdf.cell(0, 10, f"Tax (5%): {tax:.2f}", ln=True, align="R")
pdf.cell(0, 10, f"Total Payable: {total_payable:.2f}", ln=True, align="R")

# Save PDF
pdf.output(filename)
print(f"✅ Bill has been saved as '{filename}'!")