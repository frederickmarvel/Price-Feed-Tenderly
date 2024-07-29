import pandas as pd

# Read the CSV file
df = pd.read_csv('sol_data.csv')

# Convert Unix timestamps to datetime format
df['Timestamp Start'] = pd.to_datetime(df['Timestamp Start'], unit='ms')
df['Timestamp End'] = pd.to_datetime(df['Timestamp End'], unit='ms')

# Save the modified DataFrame back to a CSV file
df.to_csv('sol_data_mod.csv', index=False)