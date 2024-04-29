import pandas as pd

#
# Delete the DataFrame (D of CRUD) @@@ 先Index后Column @@@
#

df = pd.DataFrame(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    index=["Index1", "Index2", "Index3"],
    columns=["Col1", "Col2", "Col3"]
)

#
# Delete a row / column
#

# Hint: df.drop is Immutable Operation

df = df.drop("Index2", axis=0)  # axis=0: drop a row
print(df)

df = df.drop("Col2", axis=1)  # axis=1: drop a column
print(df)

df = df.drop(df.index[0], axis=0)  # use index to drop a row
print(df)

df = df.drop(df.columns[0], axis=1)  # use index to drop a column
print(df)
