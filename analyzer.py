import pandas as pd
import numpy as np

def total_demand(orders):
    return orders['Quantity'].sum()

def avg_demand(orders):
    quantities = orders['Quantity'].to_numpy() #creates numpy array
    return np.mean(quantities)

def product_demand(orders):
    demand = orders.groupby('Product')['Quantity'].sum()
    return demand.sort_values(ascending = False) #highest to lowest

def highest_demand_product(orders):
    demand = product_demand(orders)
    if demand.empty:
        return None
    return demand.idxmax(), demand.max() # gives product, quantity

def lowest_demand_product(orders):
    demand = product_demand(orders)
    if demand.empty:
        return None
    return demand.idxmin(), demand.min()

def monthly_demand(orders):
    orders = orders.copy()

    orders["Date"] = pd.to_datetime(orders["Date"],format="%d-%m-%Y")
    monthly = orders.groupby(orders["Date"].dt.to_period("M"))["Quantity"].sum()
    return monthly

def compare_products(orders, product1, product2):
    demand = product_demand(orders)

    demand1 = demand.get(product1,0)
    demand2 = demand.get(product2,0)

    return demand1, demand2

def search_product(orders, product_name):
    result = orders[
        orders["Product"].str.contains(
            product_name,
            case=False, #not case sensitive ex rice and Rice
            na=False
        )
    ]
    return result

def filter_category(orders,category):
    result = orders[
        orders["Category"].str.contains(
            category,
            case=False,
            na=False
        )
    ]
    return result

def filter_date(orders,date):
    result = orders[orders["Date"] == date]
    return result

def filter_orders(orders, product = "", category = ""):
    result = orders.copy()
    if product:
        result = result[
            result["Product"].str.contains(
                product,
                case = False,
                na = False
            )
        ]
    if category:
        result = result[
            result["Category"].str.contains(
                category,
                case = False,
                na = False
            )
        ]
    return result