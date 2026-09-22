# read and add orders

import pandas as pd

FILEPATH = 'data/orders.csv'

def load_orders():
    try:
        orders = pd.read_csv(FILEPATH)
        return orders
    
    except FileNotFoundError:
        print("File Not Found")
        return pd.DataFrame()