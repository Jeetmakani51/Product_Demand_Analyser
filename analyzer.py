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

