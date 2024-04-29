import pandas as pd

df = pd.read_csv("000001.SH.csv")

# Remove First Useless Line
df.set_index(df.columns[0], inplace=True)
df.reset_index(drop=True, inplace=True)

# Set trade_date as index (when saving CSV, it will be cleaner.)
df.set_index(df.columns[0], inplace=True)

# Save
print(df)
df.to_csv("000001.SH.Clean.csv")
