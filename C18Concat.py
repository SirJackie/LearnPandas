import pandas as pd

# 如果是二维数组，那么横向排布（从左到右，下一行，从左到右）
data1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
df1 = pd.DataFrame(data1, index=["Index1", "Index2", "Index3"], columns=["Col1", "Col2", "Col3"])

data2 = [[11, 12, 13], [14, 15, 16], [17, 18, 19]]
df2 = pd.DataFrame(data2, index=["Index1", "Index2", "Index3"], columns=["Col1", "Col2", "Col3"])

df_all = pd.concat([df1, df2])

print(df1)
print(df2)
print(df_all)
