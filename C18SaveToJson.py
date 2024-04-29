import pandas as pd

# df = pd.read_csv("000001.SH.csv")
# print(len(df.index))  # int: 8000
# print(len(df.columns))  # int:7
# df.index = ["第"+str(i+1)+"天" for i in range(0, len(df.index))]
# df.columns = ["没用的废物", "交易日期", "收盘价", "开盘价", "最高价", "最低价", "成交量"]

#
# Create the DataFrame (C of CRUD) @@@ 从左到右 @@@
#

# 如果是二维数组，那么横向排布（从左到右，下一行，从左到右）
data1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
df1 = pd.DataFrame(data1, index=["Index1", "Index2", "Index3"], columns=["Col1", "Col2", "Col3"])

# 如果是字典，那么纵向排布（从上到下，下一列，从上到下）
data2 = {"Col1": [1, 2, 3], "Col2": [4, 5, 6], "Col3": [7, 8, 9]}
df2 = pd.DataFrame(data2, index=["Index1", "Index2", "Index3"])

df = df1  # For the convenience of the following codes.

#
# Read the DataFrame (R of CRUD) @@@ 先Index后Column @@@
#

# 选取表格的子集
# 不管是df.loc[]还是df.iloc[]，都是先Index再Column（先选择行，后选择列）
# 特别注意！！！loc和iloc不是函数，而是位置索引列表 (not df.loc() but df.loc[])
subset_loc = df.loc[["Index1", "Index2"], ["Col2", "Col3"]]
subset_iloc = df.iloc[[0, 1], [1, 2]]

# 用for循环遍历DataFrame
for index, row in df.iterrows():
    for column, value in row.items():
        print(f"{value} 在第 {column} 列，第 {index} 行。")

# 选取某一列 or 某一行
# 特别注意！！！loc和iloc不是函数，而是位置索引列表 (not df.loc() but df.loc[])
# 新用法：df.iloc[a, b]，a/b如果是列表（[0, 1]），就是选取指定列；a/b如果是切片（0:-1），就是选取一个区间（从x到y）
selected_index = df.iloc[[0, 1], 0:-1]  # 0:-1 会漏掉最后一个column
print(selected_index)
selected_index = df.iloc[[0, 1], 0:]  # 0: 就不会漏掉了
print(selected_index)
