import pandas as pd

# Load the CSV files
last_year = pd.read_csv('inventory_2024.csv')
this_year = pd.read_csv('inventory_2025.csv')

# Merge on Item ID
merged = pd.merge(last_year, this_year, on='Item ID', suffixes=('_2024', '_2025'))

# Calculate cost increase and percentage
merged['Cost Increase'] = merged['Unit Cost_2025'] - merged['Unit Cost_2024']
merged['% Increase'] = (merged['Cost Increase'] / merged['Unit Cost_2024']) * 100

# Set filter thresholds
min_cost = 50.00
min_percent = 15.0

# Filter items
filtered = merged[
    (merged['Unit Cost_2025'] > min_cost) &
    (merged['% Increase'] > min_percent)
]

# Show results
print("Filtered Items with High Cost and Increase:\n")
print(filtered[['Item ID', 'Item Name_2025', 'Unit Cost_2024', 'Unit Cost_2025', '% Increase']])

# Optional: Save results to a new CSV
filtered.to_csv('filtered_inventory.csv', index=False)
