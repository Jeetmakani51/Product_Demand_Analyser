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
from tkinter import ttk, messagebox
from visualizer import(
    product_demand_chart,
    monthly_demand_chart
)
from datetime import datetime

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
    product = product_entry.get().strip()
    category = category_entry.get().strip()
    date = date_entry.get().strip()
    quantity_text = quantity_entry.get().strip()

    try:
        # Check empty fields
        if product == "" or category == "" or date == "" or quantity_text == "":
            messagebox.showwarning(
                "Input Error",
                "Please fill all fields."
            )
            return

        # Check date format
        datetime.strptime(date, "%d-%m-%Y")

        # Check quantity
        quantity = int(quantity_text)

        if quantity <= 0:
            messagebox.showwarning(
                "Input Error",
                "Quantity must be greater than 0."
            )
            return

        # Add order
        success = add_order(
            date,
            product,
            category,
            quantity
        )

        if success:
            load_table()

            product_entry.delete(0, tk.END)
            category_entry.delete(0, tk.END)
            date_entry.delete(0, tk.END)
            quantity_entry.delete(0, tk.END)

            messagebox.showinfo(
                "Success",
                "Order added successfully."
            )
        else:
            messagebox.showerror(
                "Error",
                "Could not add the order."
            )

    except ValueError:
        messagebox.showwarning(
            "Input Error",
            "Please enter a valid date (DD-MM-YYYY) and quantity."
        )

    except Exception as e:
        messagebox.showerror(
            "Error",
            f"Something went wrong:\n{e}"
        )



#filter and search

def filter_category_orders():
    category = category_filter_entry.get().strip()

    if category == "":
        messagebox.showwarning(
            "Input Required",
            "Please enter a category."
        )
        return

    orders = load_orders()
    result = filter_category(orders, category)

    for row in table.get_children():
        table.delete(row)

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


def search_orders():
    product_name = search_entry.get().strip()

    if product_name == "":
        messagebox.showwarning(
            "Input Required",
            "Please enter a product name."
        )
        return

    orders = load_orders()
    result = search_product(orders, product_name)

    for row in table.get_children():
        table.delete(row)

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


#analysis functions

def show_product_comparison():
    orders = load_orders()

    if orders.empty:
        messagebox.showinfo(
            "Product Comparison",
            "No orders available."
        )
        return

    product1 = product1_entry.get().strip()
    product2 = product2_entry.get().strip()

    if product1 == "" or product2 == "":
        messagebox.showwarning(
            "Input Required",
            "Please enter both product names."
        )
        return

    demand1, demand2 = compare_products(
        orders,
        product1,
        product2
    )

    message = (
        f"{product1} Demand: {demand1}\n"
        f"{product2} Demand: {demand2}"
    )

    messagebox.showinfo(
        "Product Comparison",
        message
    )


def show_product_chart():
    orders = load_orders()

    if orders.empty:
        messagebox.showinfo(
            "Product Demand Chart",
            "No orders available."
        )
        return

    product_demand_chart(orders)


def show_monthly_chart():
    orders = load_orders()

    if orders.empty:
        messagebox.showinfo(
            "Monthly Demand Chart",
            "No orders available."
        )
        return

    monthly_demand_chart(orders)


def show_demand_analysis():
    orders = load_orders()

    if orders.empty:
        messagebox.showinfo(
            "Demand Analysis",
            "No orders available."
        )
        return

    total = total_demand(orders)
    average = avg_demand(orders)

    highest = highest_demand_product(orders)
    lowest = lowest_demand_product(orders)

    message = (
        f"Total Demand: {total}\n"
        f"Average Demand: {average:.2f}\n\n"
        f"Highest Demand Product: {highest[0]}\n"
        f"Highest Demand: {highest[1]}\n\n"
        f"Lowest Demand Product: {lowest[0]}\n"
        f"Lowest Demand: {lowest[1]}"
    )

    messagebox.showinfo(
        "Demand Analysis",
        message
    )


def show_product_demand():
    orders = load_orders()

    if orders.empty:
        messagebox.showinfo(
            "Product Demand",
            "No orders available."
        )
        return

    demand = product_demand(orders)

    for row in table.get_children():
        table.delete(row)

    for product, quantity in demand.items():
        table.insert(
            "",
            "end",
            values=(
                "",
                "",
                product,
                "",
                quantity
            )
        )


def show_monthly_demand():
    orders = load_orders()

    if orders.empty:
        messagebox.showinfo(
            "Monthly Demand",
            "No orders available."
        )
        return

    monthly = monthly_demand(orders)

    message = "Monthly Demand\n\n"

    for month, quantity in monthly.items():
        message += f"{month}: {quantity}\n"

    messagebox.showinfo(
        "Monthly Demand",
        message
    )


#GUI

window = tk.Tk()
window.title("Retail Demand Analyzer")
window.geometry("1200x800")
window.minsize(1000, 700)

# ---------- Styling ----------

style = ttk.Style()
style.configure("Treeview", rowheight=28, font=("Arial", 10))
style.configure("Treeview.Heading", font=("Arial", 10, "bold"))

# ---------- Main Container ----------

main_frame = tk.Frame(window, padx=20, pady=15)
main_frame.pack(fill="both", expand=True)

# ---------- Title ----------

title = tk.Label(
    main_frame,
    text="Retail Demand Analyzer",
    font=("Arial", 24, "bold")
)
title.pack(pady=(0, 3))

subtitle = tk.Label(
    main_frame,
    text="Retail sales analysis and demand reporting system",
    font=("Arial", 11)
)
subtitle.pack(pady=(0, 12))


#top section

top_frame = tk.Frame(main_frame)
top_frame.pack(fill="x", pady=5)

# ---------- Add Order ----------

order_frame = tk.LabelFrame(
    top_frame,
    text="Add Order",
    padx=18,
    pady=12,
    font=("Arial", 10, "bold")
)
order_frame.pack(side="left", fill="both", expand=True, padx=(0, 8))

product_label = tk.Label(order_frame, text="Product:")
product_label.grid(row=0, column=0, sticky="w", pady=5)

product_entry = tk.Entry(order_frame, width=28)
product_entry.grid(row=0, column=1, padx=10, pady=5)

category_label = tk.Label(order_frame, text="Category:")
category_label.grid(row=1, column=0, sticky="w", pady=5)

category_entry = tk.Entry(order_frame, width=28)
category_entry.grid(row=1, column=1, padx=10, pady=5)

date_label = tk.Label(
    order_frame,
    text="Date (DD-MM-YYYY):"
)
date_label.grid(row=2, column=0, sticky="w", pady=5)

date_entry = tk.Entry(order_frame, width=28)
date_entry.grid(row=2, column=1, padx=10, pady=5)

quantity_label = tk.Label(order_frame, text="Quantity:")
quantity_label.grid(row=3, column=0, sticky="w", pady=5)

quantity_entry = tk.Entry(order_frame, width=28)
quantity_entry.grid(row=3, column=1, padx=10, pady=5)

add_button = tk.Button(
    order_frame,
    text="Add Order",
    command=add_order_from_gui,
    width=18
)
add_button.grid(
    row=4,
    column=0,
    columnspan=2,
    pady=(10, 0)
)


# ---------- Search & Filter ----------

search_frame = tk.LabelFrame(
    top_frame,
    text="Search & Filter",
    padx=18,
    pady=12,
    font=("Arial", 10, "bold")
)
search_frame.pack(side="left", fill="both", expand=True, padx=(8, 0))

category_filter_label = tk.Label(
    search_frame,
    text="Filter Category:"
)
category_filter_label.grid(
    row=0,
    column=0,
    sticky="w",
    pady=5
)

category_filter_entry = tk.Entry(
    search_frame,
    width=28
)
category_filter_entry.grid(
    row=0,
    column=1,
    padx=10,
    pady=5
)

filter_button = tk.Button(
    search_frame,
    text="Filter",
    command=filter_category_orders,
    width=12
)
filter_button.grid(
    row=0,
    column=2,
    padx=5
)

search_label = tk.Label(
    search_frame,
    text="Search Product:"
)
search_label.grid(
    row=1,
    column=0,
    sticky="w",
    pady=5
)

search_entry = tk.Entry(
    search_frame,
    width=28
)
search_entry.grid(
    row=1,
    column=1,
    padx=10,
    pady=5
)

search_button = tk.Button(
    search_frame,
    text="Search",
    command=search_orders,
    width=12
)
search_button.grid(
    row=1,
    column=2,
    padx=5
)


#analysis and reports

analysis_frame = tk.LabelFrame(
    main_frame,
    text="Analysis & Reports",
    padx=12,
    pady=10,
    font=("Arial", 10, "bold")
)
analysis_frame.pack(fill="x", pady=10)

# ---------- Product Comparison ----------

comparison_frame = tk.Frame(analysis_frame)
comparison_frame.pack(pady=(0, 8))

product1_label = tk.Label(
    comparison_frame,
    text="Product 1:"
)
product1_label.grid(row=0, column=0, padx=5)

product1_entry = tk.Entry(
    comparison_frame,
    width=18
)
product1_entry.grid(row=0, column=1, padx=5)

product2_label = tk.Label(
    comparison_frame,
    text="Product 2:"
)
product2_label.grid(row=0, column=2, padx=5)

product2_entry = tk.Entry(
    comparison_frame,
    width=18
)
product2_entry.grid(row=0, column=3, padx=5)

compare_button = tk.Button(
    comparison_frame,
    text="Compare Products",
    command=show_product_comparison
)
compare_button.grid(row=0, column=4, padx=10)

# ---------- Analysis Buttons ----------

button_frame = tk.Frame(analysis_frame)
button_frame.pack()

monthly_button = tk.Button(
    button_frame,
    text="Monthly Demand",
    command=show_monthly_demand,
    width=18
)
monthly_button.grid(row=0, column=0, padx=4, pady=4)

product_demand_button = tk.Button(
    button_frame,
    text="Product Demand",
    command=show_product_demand,
    width=18
)
product_demand_button.grid(row=0, column=1, padx=4, pady=4)

analysis_button = tk.Button(
    button_frame,
    text="Demand Analysis",
    command=show_demand_analysis,
    width=18
)
analysis_button.grid(row=0, column=2, padx=4, pady=4)

product_chart_button = tk.Button(
    button_frame,
    text="Product Demand Chart",
    command=show_product_chart,
    width=20
)
product_chart_button.grid(row=1, column=0, padx=4, pady=4)

monthly_chart_button = tk.Button(
    button_frame,
    text="Monthly Demand Chart",
    command=show_monthly_chart,
    width=20
)
monthly_chart_button.grid(row=1, column=1, padx=4, pady=4)

show_all_button = tk.Button(
    button_frame,
    text="Show All Orders",
    command=lambda: load_table(),
    width=18
)
show_all_button.grid(row=1, column=2, padx=4, pady=4)


#order table

table_frame = tk.LabelFrame(
    main_frame,
    text="Order Data",
    padx=8,
    pady=8,
    font=("Arial", 10, "bold")
)
table_frame.pack(
    fill="both",
    expand=True
)

table_scrollbar = ttk.Scrollbar(
    table_frame,
    orient="vertical"
)

table_horizontal_scrollbar = ttk.Scrollbar(
    table_frame,
    orient="horizontal"
)

table = ttk.Treeview(
    table_frame,
    columns=("ID", "Date", "Product", "Category", "Quantity"),
    show="headings",
    yscrollcommand=table_scrollbar.set,
    xscrollcommand=table_horizontal_scrollbar.set
)

table_scrollbar.config(command=table.yview)
table_horizontal_scrollbar.config(command=table.xview)

table.heading("ID", text="Order ID")
table.heading("Date", text="Date")
table.heading("Product", text="Product")
table.heading("Category", text="Category")
table.heading("Quantity", text="Quantity")

table.column("ID", width=100, anchor="center")
table.column("Date", width=150, anchor="center")
table.column("Product", width=200)
table.column("Category", width=180)
table.column("Quantity", width=120, anchor="center")

table_scrollbar.pack(
    side="right",
    fill="y"
)

table_horizontal_scrollbar.pack(
    side="bottom",
    fill="x"
)

table.pack(
    side="left",
    fill="both",
    expand=True
)

#filter / search 

def filter_category_orders():
    category = category_filter_entry.get().strip()

    if category == "":
        messagebox.showwarning(
            "Input Required",
            "Please enter a category."
        )
        return

    orders = load_orders()
    result = filter_category(orders, category)

    for row in table.get_children():
        table.delete(row)

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


def search_orders():
    product_name = search_entry.get().strip()

    if product_name == "":
        messagebox.showwarning(
            "Input Required",
            "Please enter a product name."
        )
        return

    orders = load_orders()
    result = search_product(orders, product_name)

    for row in table.get_children():
        table.delete(row)

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


#analysis functions

def show_product_comparison():
    orders = load_orders()

    if orders.empty:
        messagebox.showinfo(
            "Product Comparison",
            "No orders available."
        )
        return

    product1 = product1_entry.get().strip()
    product2 = product2_entry.get().strip()

    if product1 == "" or product2 == "":
        messagebox.showwarning(
            "Input Required",
            "Please enter both product names."
        )
        return

    demand1, demand2 = compare_products(
        orders,
        product1,
        product2
    )

    message = (
        f"{product1} Demand: {demand1}\n"
        f"{product2} Demand: {demand2}"
    )

    messagebox.showinfo(
        "Product Comparison",
        message
    )


def show_product_chart():
    orders = load_orders()

    if orders.empty:
        messagebox.showinfo(
            "Product Demand Chart",
            "No orders available."
        )
        return

    product_demand_chart(orders)


def show_monthly_chart():
    orders = load_orders()

    if orders.empty:
        messagebox.showinfo(
            "Monthly Demand Chart",
            "No orders available."
        )
        return

    monthly_demand_chart(orders)


def show_demand_analysis():
    orders = load_orders()

    if orders.empty:
        messagebox.showinfo(
            "Demand Analysis",
            "No orders available."
        )
        return

    total = total_demand(orders)
    average = avg_demand(orders)

    highest = highest_demand_product(orders)
    lowest = lowest_demand_product(orders)

    message = (
        f"Total Demand: {total}\n"
        f"Average Demand: {average:.2f}\n\n"
        f"Highest Demand Product: {highest[0]}\n"
        f"Highest Demand: {highest[1]}\n\n"
        f"Lowest Demand Product: {lowest[0]}\n"
        f"Lowest Demand: {lowest[1]}"
    )

    messagebox.showinfo(
        "Demand Analysis",
        message
    )


def show_product_demand():
    orders = load_orders()

    if orders.empty:
        messagebox.showinfo(
            "Product Demand",
            "No orders available."
        )
        return

    demand = product_demand(orders)

    for row in table.get_children():
        table.delete(row)

    for product, quantity in demand.items():
        table.insert(
            "",
            "end",
            values=(
                "",
                "",
                product,
                "",
                quantity
            )
        )


def show_monthly_demand():
    orders = load_orders()

    if orders.empty:
        messagebox.showinfo(
            "Monthly Demand",
            "No orders available."
        )
        return

    monthly = monthly_demand(orders)

    message = "Monthly Demand\n\n"

    for month, quantity in monthly.items():
        message += f"{month}: {quantity}\n"

    messagebox.showinfo(
        "Monthly Demand",
        message
    )


# table function

def load_table():
    orders = load_orders()

    for row in table.get_children():
        table.delete(row)

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


# start app

load_table()

window.mainloop()
