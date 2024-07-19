import pandas as pd
from decimal import Decimal

#
# ------------------------------
#

# Load
df = pd.read_csv("000001.SZ-Main.csv")

# Convert to Decimal
df.iloc[0:, 1:] = df.iloc[0:, 1:].map(lambda x: Decimal(str(x)))

# Print
print(df)

#
# ------------------------------
#

# Convert Back to Floats
df.iloc[0:, 1:] = df.iloc[0:, 1:].map(lambda x: float(x))

# First-Line Pre-Process
df.set_index(df.columns[0], inplace=True)

# Save
df.to_csv("000001.SZ-Final.csv")
