==================================================
       RETAIL PRODUCT DEMAND ANALYZER
==================================================

PROJECT OVERVIEW
----------------
Retail Product Demand Analyzer is a Python desktop
application used to analyze historical retail order data.

It allows users to add, search, filter and analyze
product orders and view demand through charts.


FEATURES
--------
- Add and store order records
- Search products
- Filter orders by category
- Calculate total and average demand
- Find highest and lowest demand products
- Compare two products
- Analyze monthly demand
- Generate product demand chart
- Generate monthly demand chart
- Input validation and exception handling


TECHNOLOGIES USED
-----------------
- Python
- Pandas
- NumPy
- Matplotlib
- Tkinter
- CSV


PROJECT STRUCTURE
-----------------
RetailDemandAnalyser/
|
|-- main.py
|-- data_manager.py
|-- analyzer.py
|-- visualizer.py
|
|-- data/
|   |-- orders.csv
|
|-- reports/
|
|-- README.txt


MODULES
-------
main.py
    Handles the Tkinter GUI and connects all modules.

data_manager.py
    Handles reading, adding and saving order data.

analyzer.py
    Performs demand calculations, searching,
    filtering and comparisons.

visualizer.py
    Creates product and monthly demand charts.


HOW TO RUN
----------
1. Install Python 3.x.
2. Install required libraries:

   pip install pandas numpy matplotlib

3. Run the application:

   python main.py


DATA FORMAT
-----------
Order data is stored in:

data/orders.csv

Fields:
Order_ID, Date, Product, Category, Quantity

Date format:
DD-MM-YYYY


DEMAND ANALYSIS
---------------
Total Demand:
Sum of all order quantities.

Average Demand:
Average quantity per order.

Product Demand:
Total quantity ordered for each product.

Monthly Demand:
Total quantity ordered in each month.


VALIDATION
----------
The application checks:
- Empty fields
- Invalid quantity
- Negative quantity
- Invalid date format

Exception handling is used to prevent unexpected
errors from crashing the application.


LIMITATIONS
-----------
- Uses CSV instead of a database.
- Analyzes historical demand only.
- Does not predict future demand.


CONCLUSION
----------
The project demonstrates the practical use of Python,
Pandas, NumPy, Matplotlib, Tkinter, file handling,
modular programming, validation and exception handling.
