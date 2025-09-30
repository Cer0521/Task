import pandas as pd

# Sample data for last year's inventory
last_year_inventory = pd.DataFrame({
    'Item ID': [101, 102, 103, 104, 105],
    'Item Name': ['Book 1', 'Book 2', 'Book 3', 'Book 4', 'Book 5'],
    'Unit Cost': [50.00, 75.00, 120.00, 200.00, 90.00],
    'Quantity': [100, 150, 200, 80, 120]
})

# Sample data for this year's inventory
this_year_inventory = pd.DataFrame({
    'Item ID': [101, 102, 103, 104, 105],
    'Item Name': ['Book 1', 'Book 2', 'Book 3', 'Book 4', 'Book 5'],
    'Unit Cost': [55.00, 78.00, 150.00, 250.00, 100.00],
    'Quantity': [110, 140, 210, 90, 130]
})

# Define thresholds
unit_cost_threshold = 100.00  # $100
percentage_increase_threshold = 10.0  # 10%

# Merge the data
merged_inventory = pd.merge(
    last_year_inventory,
    this_year_inventory,
    on='Item ID',
    suffixes=('_LastYear', '_ThisYear')
)

# Calculate the percentage increase
merged_inventory['Unit Cost Increase (%)'] = (
    (merged_inventory['Unit Cost_ThisYear'] - merged_inventory['Unit Cost_LastYear']) /
    merged_inventory['Unit Cost_LastYear'] * 100
)

# Filter based on thresholds
filtered_inventory = merged_inventory[
    (merged_inventory['Unit Cost_ThisYear'] > unit_cost_threshold) &
    (merged_inventory['Unit Cost Increase (%)'] > percentage_increase_threshold)
]

# Show the result
print(filtered_inventory[['Item ID', 'Item Name_ThisYear', 'Unit Cost_LastYear', 'Unit Cost_ThisYear', 'Unit Cost Increase (%)']])
