# # print("Retail Product Demand Analyzer")
# # print("Project started successfully!")

# # from data_manager import load_orders,add_order

# # print("before adding an order : \n")
# # print(load_orders())

# # add_order("22-09-2026", "Biscuit", "Grocery", 5)

# # print("After adding an order : \n")
# # print(load_orders())


from data_manager import load_orders,add_order
from analyzer import (
    total_demand,
    avg_demand,
    product_demand,
    highest_demand_product,
    lowest_demand_product,
    monthly_demand,
    compare_products,
    search_product,
    filter_category,
    filter_date,
    filter_orders
)
import tkinter as tk
from tkinter import ttk

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
    quantity_text = quantity_entry.get()

    try:
        # Check empty fields
        if product == "" or category == "" or date == "" or quantity_text == "":
            print("Please fill all fields.")
            return

        # Convert quantity to integer
        quantity = int(quantity_text)

        # Check positive quantity
        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return

        add_order(
            date,
            product,
            category,
            quantity
        )

        load_table()

        # Clear fields
        product_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)
        quantity_entry.delete(0, tk.END)

        print("Order added successfully.")

    except ValueError:
        print("Quantity must be a number.")

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

#category
category_filter_label = tk.Label(
    window,
    text="Filter Category:"
)

category_filter_label.pack()

category_filter_entry = tk.Entry(
    window,
    width=30
)

category_filter_entry.pack(pady=5)

def filter_category_orders():
    category = category_filter_entry.get()

    orders = load_orders()

    result = filter_category(
        orders,
        category
    )

    # Clear table
    for row in table.get_children():
        table.delete(row)

    # Display filtered results
    for _, order in result.iterrows():
        table.insert(
            "",
            "end",
            values=(
                order["Order_ID"],
                order["Date"],
                order["Product"],
                order["Category"],
                order["Quantity"]
            )
        )

filter_button = tk.Button(
    window,
    text="Filter",
    command=filter_category_orders
)

filter_button.pack(pady=5)

#search
search_label = tk.Label(
    window, text = "Search Product:"
)

search_label.pack()
search_entry = tk.Entry(
    window,
    width=30
)
search_entry.pack(pady=5)

def search_orders():
    product_name = search_entry.get()

    orders = load_orders()

    result = search_product(
        orders,
        product_name
    )

    # Clear table
    for row in table.get_children():
        table.delete(row)

    # Display search results
    for _, order in result.iterrows():
        table.insert(
            "",
            "end",
            values=(
                order["Order_ID"],
                order["Date"],
                order["Product"],
                order["Category"],
                order["Quantity"]
            )
        )

search_button = tk.Button(
    window,
    text="Search",
    command=search_orders
)

search_button.pack(pady=5)

#orders table
table = ttk.Treeview(
    window, 
    columns = ("ID", "Date", "Product", "Category", "Quantity"),
    show="headings"
)

table.heading("ID", text = "Order ID")
table.heading("Date", text = "Date")
table.heading("Product", text = "Product")
table.heading("Category", text = "Category")
table.heading("Quantity", text = "Quantity")

table.pack(pady=20, padx=20, fill="both", expand=True)


def load_table():
    orders = load_orders()

    # Remove old rows
    for row in table.get_children():
        table.delete(row)

    # Add orders to table
    for _, order in orders.iterrows():
        table.insert(
            "",
            "end",
            values=(
                order["Order_ID"],
                order["Date"],
                order["Product"],
                order["Category"],
                order["Quantity"]
            )
        )
show_all_button = tk.Button(
    window,
    text="Show All",
    command = load_table
)

show_all_button.pack(pady=5)

window.mainloop()
