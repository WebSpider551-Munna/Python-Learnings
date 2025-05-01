#Item           : Pen  
#Quantity       : 3  
#Price/item     : 10.50  
#Subtotal       : 31.50  
#Discount (10%) : 3.15  
#Tax (5%)       : 1.42  
#Total Payable  : 29.77

Item = "Pen"
Quantity = 3
Price_per_item = 10.50
Subtotal = Quantity * Price_per_item
Discount = (10/100)*Subtotal
Tax = (5/100) * (Subtotal - Discount)
Total = Subtotal - Discount + Tax

print(f"{'Item':<15}:{Item}")
print(f"{'Quantity':<15}:{Quantity}")
print(f"{'Price/item':<15}:{Price_per_item:.2f}")
print(f"{'Subtotal':<15}:{Subtotal:.2f}")
print(f"{'Discount (10%)':<15}:{Discount:.2f}")
print(f"{'Tax (5%)':<15}:{Tax:.2f}")
print(f"{'Total Payable':<15}:{Total:.2f}")