import pandas as pd
from decimal import Decimal

# Load
df = pd.read_csv("000001.SH.Clean.csv")

# Convert to Decimal
df.iloc[0:, 1:] = df.iloc[0:, 1:].map(lambda x: Decimal(str(x)))

# Print
print(df)
