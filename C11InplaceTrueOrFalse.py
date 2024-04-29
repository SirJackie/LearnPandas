import pandas as pd

df = pd.DataFrame(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    index=["Index1", "Index2", "Index3"],
    columns=["Col1", "Col2", "Col3"]
)

print(df)

# Normally: df is immutable.
df2 = df.drop("Index1", axis=0)
print(df)

# When Inplace=True, df itself will be changed.
df.drop("Index1", axis=0, inplace=True)
print(df)
