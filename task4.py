import pandas as pd
import re


data = {
    'Tag Number': ['INV1001', 'INV1002', 'INV1003', 'INV1005', 'INV1005', 'INV1007']
}

df = pd.DataFrame(data)


df['Tag Num Int'] = df['Tag Number'].apply(lambda x: int(re.search(r'\d+', x).group()))


sorted_tags = sorted(df['Tag Num Int'])


duplicates = df[df.duplicated('Tag Num Int')]['Tag Number'].unique()


full_range = set(range(min(sorted_tags), max(sorted_tags) + 1))
existing_tags = set(sorted_tags)
missing = sorted(full_range - existing_tags)


print("🔁 Duplicate Tag Numbers:")
print(duplicates if len(duplicates) > 0 else "None found.")

print("\n❌ Missing Tag Numbers in Sequence:")
print([f"INV{num}" for num in missing] if missing else "None found.")
