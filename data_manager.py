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

def add_order(Date, Product, Category, Quantity):
    try:
        orders = load_orders()

        if orders.empty:
            Order_ID = 1 #first order
        else:
            Order_ID = orders["Order_ID"].max() + 1 #if the max order is 10, the new one order id will be 11

        new_order = {
            "Order_ID" : Order_ID,
            "Date" : Date,
            "Product" : Product,
            "Category" : Category,
            "Quantity" : Quantity
        }
        orders.loc[len(orders)] = new_order
        orders.to_csv(FILEPATH, index=False)
        return True

    except Exception as e:
        print("Error while adding the order : ", e)
        return False