import pandas as pd

df = pd.read_csv("000001.SH.csv")  # Read from CSV

# Remove First Useless Line
df.set_index(df.columns[0], inplace=True)
df.reset_index(drop=True, inplace=True)

print(df)
