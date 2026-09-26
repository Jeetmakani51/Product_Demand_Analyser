# # print("Retail Product Demand Analyzer")
# # print("Project started successfully!")

# # from data_manager import load_orders,add_order

# # print("before adding an order : \n")
# # print(load_orders())

# # add_order("22-09-2026", "Biscuit", "Grocery", 5)

# # print("After adding an order : \n")
# # print(load_orders())


from data_manager import load_orders,add_order
# from analyzer import (
#     total_demand,
#     avg_demand,
#     product_demand,
#     highest_demand_product,
#     lowest_demand_product,
#     monthly_demand,
#     compare_products,
#     search_product,
#     filter_category,
#     filter_date,
#     filter_orders
# )
import tkinter as tk


# orders = load_orders()

# print("ALL ORDERS")
# print(orders)

# print("\nTOTAL DEMAND:")
# print(total_demand(orders))

# print("\nAVERAGE DEMAND:")
# print(avg_demand(orders))

# print("\nDEMAND BY PRODUCT:")
# print(product_demand(orders))

# print("\nHIGHEST DEMAND PRODUCT:")
# print(highest_demand_product(orders))

# print("\nLOWEST DEMAND PRODUCT:")
# print(lowest_demand_product(orders))

# print("\nMONTHLY DEMAND:")
# print(monthly_demand(orders))

# print("\nRICE VS MILK:")
# print(compare_products(orders, "Rice", "Milk"))

# print("SEARCH FOR RICE")
# print(search_product(orders, "Rice"))

# print("\nFILTER BY GROCERY CATEGORY")
# print(filter_category(orders, "Grocery"))

# print("\nFILTER BY DATE")
# print(filter_date(orders, "05-09-2026"))

# print("\nRICE + GROCERY")
# print(filter_orders(
#     orders,
#     product="Rice",
#     category="Grocery"
# ))

def add_order_from_gui():
    product = product_entry.get()
    category = category_entry.get()
    date = date_entry.get()
    quantity = int(quantity_entry.get())

    add_order(
        date,
        product,
        category,
        quantity
    )

window = tk.Tk()
window.title("Retail Product Demand Analyzer")
window.geometry("800x600")
title = tk.Label(
    window,
    text = "Retail Product Demand Analyzer",
    font = ("Arial", 20, "bold")
)
title.pack(pady=20)

#product
product_label = tk.Label(window, text="Product: ")
product_label.pack()

product_entry = tk.Entry(window, width = "40")
product_entry.pack(pady = 5)

#category
category_label = tk.Label(window, text = "Category: ")
category_label.pack()

category_entry = tk.Entry(window, width = "40")
category_entry.pack(pady = 5)

#date
date_label = tk.Label(window, text = "Date(DD/MM/YY): ")
date_label.pack()

date_entry = tk.Entry(window, width = "40")
date_entry.pack(pady = 5)

#quantity
quantity_label = tk.Label(window, text = "Quantity: ")
quantity_label.pack()

quantity_entry = tk.Entry(window, width = "40")
quantity_entry.pack(pady = 5)

add_button = tk.Button(window, text = "Add order", command=add_order_from_gui)
add_button.pack(pady = 15)
window.mainloop()