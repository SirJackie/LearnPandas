import pandas as pd

#
# Create the DataFrame (C of CRUD) @@@ 从左到右 @@@
#

# 如果是二维数组，那么横向排布（从左到右，下一行，从左到右）
data1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
df1 = pd.DataFrame(data1, index=["Index1", "Index2", "Index3"], columns=["Col1", "Col2", "Col3"])

# 如果是字典，那么纵向排布（从上到下，下一列，从上到下）
data2 = {"Col1": [1, 2, 3], "Col2": [4, 5, 6], "Col3": [7, 8, 9]}
df2 = pd.DataFrame(data2, index=["Index1", "Index2", "Index3"])

print(df1)
print(df2)
