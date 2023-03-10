# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path


# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('Resources/menu_data.csv')
sales_filepath = Path('Resources/sales_data.csv')

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# @TODO: Read in the menu data into the menu list

with open(menu_filepath, 'r') as csvfile:
    
    #menu_filepath = csv.reader(csvfile, delimiter = ',', quotechar='"')
    
    menu_file = csv.reader(csvfile, delimiter = ',')  
    
    header = next(menu_file)
    
    for row in menu_file:
        menu.append(row)
        
    
print(menu)
print("----------------------------------------------------------------------------------")

# @TODO: Read in the sales data into the sales list

with open(sales_filepath, 'r') as csvfile:
    
    # sales_filepath = csv.reader(csvfile, delimiter = ',', quotechar='"')
    
    sales_file = csv.reader(csvfile, delimiter = ',')
    
    header = next(sales_file)
    
    for row in sales_file:
        sales.append(row)
    
print(sales)
print("----------------------------------------------------------------------------------")

# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0


print("----------------------------------------------------------------------------------")

# @TODO: Loop over every row in the sales list object
    # do something with quantity and menu_item
    
for row in sales:
    # print(row)
    
    quantity = int(row[3])
    sales_item = row[4]
    
    row_count += 1
    
    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables


    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit

    if sales_item not in report.keys():
        report[sales_item] = {
             "01-count": 0,
             "02-revenue": 0,
             "03-cogs": 0,
             "04-profit": 0,
        }


    # @TODO: For every row in our sales data, loop over the menu records to determine a match

        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables

    for row in menu:
        item = row[0]
        price = float(row[3])
        cost = float(row[4])
    
        
# print(f"{item}: price {price}, cost {cost}")

        # @TODO: Calculate profit of each item in the menu data
        profit = price - cost

        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
        if sales_item == item:
            
        # @TODO: Print out matching menu data
        # print ('item)
        # @TODO: Cumulatively add up the metrics for each item key
            report[sales_item]["01-count"] += quantity
            report[sales_item]["02-revenue"] += price * quantity
            report[sales_item]["03-cogs"] += cost * quantity
            report[sales_item]["04-profit"] += profit * quantity
            print(f"{sales_item} equal {item}")
               
        # @TODO: Else, the sales item does not equal any fo the item in the menu data, therefore no match
        else:
            print(f"{sales_item} does not equal {item}! NO MATCH!")
    


    # @TODO: Increment the row counter by 1
    

# @TODO: Print total number of records in sales data

print(f"Processed {row_count} rows of data")

# @TODO: Write out report to a text file (won't appear on the command line output)


print(report)

output_path = Path("output.txt")

with open(output_path, 'w') as file:
    file.write(f"This is the report: {report}")
    file.write()