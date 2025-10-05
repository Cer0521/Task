import pandas as pd
import sys
from pymongo import MongoClient

def main():
    try:
        df = pd.read_csv('inventory_comparison_2024_2025.csv')
    except FileNotFoundError:
        print("❌ File 'inventory_comparison_2024_2025.csv' not found in the current directory.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")
        sys.exit(1)

    # Ensure columns exist
    required_cols = ['Item ID', 'Item Name', 'Year 2024', 'Year 2025']
    for col in required_cols:
        if col not in df.columns:
            print(f"❌ Missing column: {col}")
            sys.exit(1)

    # Convert year columns to numeric (in case they are strings)
    df['Year 2024'] = pd.to_numeric(df['Year 2024'], errors='coerce')
    df['Year 2025'] = pd.to_numeric(df['Year 2025'], errors='coerce')

    # Drop rows with missing data
    df = df.dropna(subset=['Year 2024', 'Year 2025'])

    # Compute cost increase and percentage increase
    df['Cost Increase'] = df['Year 2025'] - df['Year 2024']
    df['% Increase'] = (df['Cost Increase'] / df['Year 2024']) * 100
    df['% Increase'] = df['% Increase'].round(2)

    # Define thresholds
    min_cost = 20        # only show items costing > $20 in 2025
    min_percent = 10     # only show items that increased > 10%

    # Filter based on both conditions
    filtered = df[
        (df['Year 2025'] > min_cost) &
        (df['% Increase'] > min_percent)
    ]

    # Show filtered results
    print("Filtered items with high cost and significant increase:")
    if not filtered.empty:
        print(filtered[['Item ID', 'Item Name', 'Year 2024', 'Year 2025', '% Increase']].to_string(index=False))
    else:
        print("No items matched the criteria.")

    # Save the filtered results
    filtered.to_csv('filtered_inventory.csv', index=False)

    # --- Add to MongoDB ---
    # Connect to MongoDB Atlas
    client = MongoClient("mongodb+srv://espiritucypher_db_user:espiritu21@cluster0.suffibw.mongodb.net/")
    db = client["inventory_db"]  # database name
    collection = db["filtered_inventory"]  # collection name

    # Convert DataFrame to dictionary records and insert
    records = filtered.to_dict(orient='records')
    if records:
        collection.insert_many(records)
    else:
        print("\nNo records to insert into MongoDB.")

if __name__ == "__main__":
    main()
