# ## Project V: **Thread Shed**

# You’ve recently been hired as a cashier at the local sewing hobby shop, ***Thread Shed***. Some of your daily responsibilities involve tallying the number of sales during the day, calculating the total amount of money made, and keeping track of the names of the customers.

# Unfortunately, the ***Thread Shed*** has an extremely outdated register system and stores all of the transaction information in one huge unwieldy string called `daily_sales`.

# All day, for each transaction, the name of the customer, amount spent, types of thread purchased, and the date of sale is all recorded in this same string. Your task is to use your Python skills to iterate through this string and clean up each transaction and store all the information in easier-to-access lists.

# ### Project Requirements

# Break down daily sales data into organized lists and analyze thread color sales.

# ### Data Processing Steps

# - Clean and Parse Data
#     - Replace delimiters and split transactions
#     - Remove whitespace and format data
# - Create Lists
#     - Customers list: Store customer names
#     - Sales list: Store transaction amounts
#     - Thread sold list: Store thread colors
# - Calculate Sales
#     - Convert string amounts to floats
#     - Sum total daily sales
# - Analyze Thread Colors
#     - Split multiple colors into individual entries
#     - Count occurrences of each color
#     - Generate color sales report

    daily_sales = \
"""Edith Mcbride   ;,;$1.21   ;,;   white ;,; 09/15/17   ,
Herbert Tran   ;,;   $7.29;,; white&blue;,;   09/15/17 ,
Paul Clarke ;,;$12.52 ;,;   white&blue ;,; 09/15/17 ,
Lucille Caldwell   ;,;   $5.13   ;,; white   ;,; 09/15/17,
Eduardo George   ;,;$20.39;,; white&yellow ;,;09/15/17   ,   
Danny Mclaughlin;,;$30.82;,;  purple ;,;09/15/17 ,
Stacy Vargas;,; $1.85   ;,; purple&yellow ;,;09/15/17,  
Shaun Brock;,; $17.98;,;purple&yellow ;,; 09/15/17 , 
Erick Harper ;,;$17.41;,; blue ;,; 09/15/17, 
Michelle Howell ;,;$28.59;,; blue;,;   09/15/17   , 
Carroll Boyd;,; $14.51;,;   purple&blue   ;,; 09/15/17 , 
Teresa Carter   ;,; $19.64 ;,; white;,;09/15/17 ,   
Jacob Kennedy ;,; $11.40   ;,; white&red   ;,; 09/15/17, 
Craig Chambers;,; $8.79 ;,; white&blue&red   ;,;09/15/17, 
Peggy Bell;,; $8.65 ;,;blue   ;,; 09/15/17, 
Kenneth Cunningham ;,;   $10.53;,;   green&blue   ;,; 09/15/17   ,   
Marvin Morgan;,;   $16.49;,; green&blue&red   ;,;   09/15/17 ,
Marjorie Russell ;,; $6.55 ;,;   green&blue&red;,;   09/15/17 ,
Israel Cummings;,;   $11.86   ;,;black;,;  09/15/17,   
June Doyle   ;,;   $22.29 ;,;  black&yellow ;,;09/15/17"""


# Clean and format data
daily_sales_replaced = daily_sales.replace(';,;',';')
daily_transactions = daily_sales_replaced.split(',')

# Split transactions into components
daily_transactions_split = []
for x in daily_transactions:
    daily_transactions_split.append(x.split(';'))

# Remove whitespace and clean data
transactions_clean = []
for y in daily_transactions_split:
    new_list = []
    for data_point in y:
        new_list.append(data_point.strip(" ").replace('\n', ' '))
    transactions_clean.append(new_list)

# Create separate lists
customers = []
sales = []
thread_sold = []
for z in transactions_clean:
    customers.append(z[0])
    sales.append(z[1])
    thread_sold.append(z[2])

# Calculate total sales
total_sales = 0
for s in sales:
    f = s.strip(' $').strip()
    total_sales = total_sales + float(f)

# Process thread colors
thread_sold_split = []
for t in thread_sold:
    if '&' not in t:
        thread_sold_split.append(t.strip())
    else:
        c = t.split('&')
        for colors in c:
            thread_sold_split.append(colors.strip())

# Color counting function
def color_count(color):
    counter = 0
    for J in thread_sold_split:
        if J == color:
            counter += 1
    return counter

# Generate color sales report
colors = ['red', 'yellow', 'green', 'white', 'black', 'blue', 'purple']
for color in colors:
    print('Thread Shed sold', color_count(color), 'threads of', color, 'thread today.')


