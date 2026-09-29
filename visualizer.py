import matplotlib.pyplot as plt
import pandas as pd

def product_demand_chart(orders):
    demand = orders.groupby("Product")["Quantity"].sum()

    plt.figure(figsize=(8,5))
    demand.plot(kind = "bar")
    plt.title("Product Demand")
    plt.xlabel("Product")
    plt.ylabel("Total Quantity")

    plt.tight_layout()
    plt.show()


def monthly_demand_chart(orders):
    orders = orders.copy()

    orders["Date"] = pd.to_datetime(
        orders["Date"],
        format="%d-%m-%Y"
    )

    monthly = orders.groupby(
        orders["Date"].dt.to_period("M")
    )["Quantity"].sum()

    # Convert month periods to text
    months = monthly.index.astype(str)

    plt.figure(figsize=(8, 5))

    plt.plot(
        months,
        monthly.values,
        marker="o"
    )

    plt.title("Monthly Demand")
    plt.xlabel("Month")
    plt.ylabel("Total Quantity")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    orders = pd.read_csv("data/orders.csv")
    monthly_demand_chart(orders)