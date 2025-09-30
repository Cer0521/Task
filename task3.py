import pandas as pd

# Example inventory data (replace with your real file or DataFrame)
data = {
    'Tag Number': ['INV1001', 'INV1002', 'INV1003', 'INV1004', 'INV1005'],
    'Item Name': ['Widget A', 'Widget B', 'Gadget C', 'Gadget D', 'Tool E'],
    'Unit Cost': [50, 75, 120, 200, 90],
    'Quantity': [100, 150, 200, 80, 120]
}

df = pd.DataFrame(data)

# Set how many tag numbers to sample
sample_size = 3

# Sample from the 'Tag Number' column
sample = df['Tag Number'].sample(n=sample_size, random_state=42)

# Print the sample
print("🎯 Sampled Inventory Tag Numbers:")
print(sample.to_string(index=False))
