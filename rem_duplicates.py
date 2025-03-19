import pandas as pd

# Read the CSV file
df = pd.read_csv('contacts.csv')

# Remove duplicates based on Phone column
df_cleaned = df.drop_duplicates(subset=['Phone'], keep='first')

# Reset the index and rename persons sequentially
df_cleaned['Name'] = [f'Person{i+1}' for i in range(len(df_cleaned))]

# Save to CSV
df_cleaned.to_csv('contacts_cleaned.csv', index=False)

# Print statistics
print(f"Original entries: {len(df)}")
print(f"After removing duplicates: {len(df_cleaned)}")
print(f"Removed {len(df) - len(df_cleaned)} duplicate entries")