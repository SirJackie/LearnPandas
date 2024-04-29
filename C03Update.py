import pandas as pd

#
# Update the DataFrame (U of CRUD) @@@ 先Index后Column @@@
#

df = pd.DataFrame(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    index=["Index1", "Index2", "Index3"],
    columns=["Col1", "Col2", "Col3"]
)

#
# Update a single value
#

# 使用df.iloc[i, c]，相对应df.iloc[i_names, c_names]
df.iloc[0, 1] = 23456  # @@@ 先Index后Column @@@
print(df)

# 使用df.at[i_name, c_name]，相对应df.loc[i_names, c_names]
df.at["Index1", "Col3"] = 34567  # @@@ 先Index后Column @@@
print(df)

#
# Add a row / column
#

# Add a column
column4_values = [4, 4, 4]
column5_values = [5, 5, 5]
df["Col4"] = column4_values         # 用df["col_name"]赋值，来实现添加列
df.loc[:, "Col5"] = column5_values  # 用df.loc直接赋值，来实现添加列（df.loc可以扩大表格，df.iloc不允许扩大）
print(df)

# Add a row
row4_values = [44, 44, 44, 44, 44]
df.loc["Index4"] = row4_values      # 用df.loc直接赋值，来实现添加行（df.loc可以扩大表格，df.iloc不允许扩大）
print(df)
