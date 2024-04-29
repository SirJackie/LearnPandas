import pandas as pd
from decimal import Decimal

# Load
df = pd.read_csv("000001.SH.Clean.csv")

# Convert to Deciaml
df.iloc[0:, 1:] = df.iloc[0:, 1:].map(lambda x: Decimal(str(x)))

# Print
print(df)

# Convert Back to Floats
df.iloc[0:, 1:] = df.iloc[0:, 1:].map(lambda x: float(x))

# Print
print(df)

# Save
df.set_index(df.columns[0], inplace=True)
df.to_csv("000001.SH.DecimalBack.csv")
