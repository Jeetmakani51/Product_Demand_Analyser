# print("Retail Product Demand Analyzer")
# print("Project started successfully!")

# from data_manager import load_orders,add_order

# print("before adding an order : \n")
# print(load_orders())

# add_order("22-09-2026", "Biscuit", "Grocery", 5)

# print("After adding an order : \n")
# print(load_orders())


from data_manager import load_orders
from analyzer import (
    total_demand,
    avg_demand,
    product_demand,
    highest_demand_product,
    lowest_demand_product,
    monthly_demand,
    compare_products
)


orders = load_orders()

print("ALL ORDERS")
print(orders)

print("\nTOTAL DEMAND:")
print(total_demand(orders))

print("\nAVERAGE DEMAND:")
print(avg_demand(orders))

print("\nDEMAND BY PRODUCT:")
print(product_demand(orders))

print("\nHIGHEST DEMAND PRODUCT:")
print(highest_demand_product(orders))

print("\nLOWEST DEMAND PRODUCT:")
print(lowest_demand_product(orders))

print("\nMONTHLY DEMAND:")
print(monthly_demand(orders))

print("\nRICE VS MILK:")
print(compare_products(orders, "Rice", "Milk"))