import pandas as pd

data = [[1, 2, 3], [4, 5, 6], [1, 2, 3], [7, 8, 9], [7, 8, 9], [6, 7, 8]]
df = pd.DataFrame(
    data, index=["Index1", "Index2", "Index3", "Index4", "Index5", "Index6"], columns=["Col1", "Col2", "Col3"]
)

print(df)
print(df.drop_duplicates())
