import pandas as pd

df = pd.read_csv("000001.SH.csv")  # Read from CSV
df = df.set_index(df.columns[0])  # Set #1 Useless Column as Index
df = df.reset_index(drop=True)  # Drop the Index Data, Make it Original (0, 1, 2, ..., 7999)
print(df)
