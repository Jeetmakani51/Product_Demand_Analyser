# print("Retail Product Demand Analyzer")
# print("Project started successfully!")

from data_manager import load_orders,add_order

print("before adding an order : \n")
print(load_orders())

add_order("22-09-2026", "Biscuit", "Grocery", 5)

print("After adding an order : \n")
print(load_orders())
