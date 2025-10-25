## Project III: **Carly's Clippers**

# You are the Data Analyst at Carly's Clippers, the newest hair salon on the block. Your job is to analyze recent data and calculate key metrics for business planning.

### Project Requirements

# - Calculate and analyze pricing metrics:
#     - Determine the average price of haircuts
#     - Create new pricing with $5 discount
# - Calculate revenue metrics:
#     - Compute total weekly revenue
#     - Calculate average daily revenue
#     - Identify haircuts under $30 for marketing


#1. Price Analysis Implementation

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Calculate average price
total_price = 0
for price in prices:
    total_price += price
print(total_price)

average_price = total_price / len(prices)
print('Average Haircut Price:', average_price)

# Create new prices with $5 discount
new_prices = [price - 5 for price in prices]
print(new_prices)


# Calculate revenue
total_revenue = 0
for i in range(0, len(hairstyles)):
    total_revenue = prices[i] + last_week[i]
print('Total Revenue:', total_revenue)

# Calculate daily average
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

# Find cuts under $30
cuts_under_30 = [hairstyles[i] for i in range(0, len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)

