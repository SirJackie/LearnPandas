import pandas as pd

#
# Read the DataFrame (R of CRUD) @@@ 先Index后Column @@@
#

df = pd.DataFrame(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    index=["Index1", "Index2", "Index3"],
    columns=["Col1", "Col2", "Col3"]
)

#
# 获取DataFrame的Numpy表达
#

# 直接转换成Numpy数组，然后绕过pandas做自己的操作（列包着行，从左到右）

df_values = df.values
print(df_values)

#
# 选取表格的子集
#

# 不管是df.loc[]还是df.iloc[]，都是先Index再Column（先选择行，后选择列）
# 特别注意！！！loc和iloc不是函数，而是位置索引列表 (not df.loc() but df.loc[])

subset_loc = df.loc[["Index1", "Index2"], ["Col2", "Col3"]]
subset_iloc = df.iloc[[0, 1], [1, 2]]

print(subset_loc)
print(subset_iloc)

#
# 用for循环遍历DataFrame
#

# df.iterrows() 返回：（a）行名 Index（b）行数据 row
# row.items() 返回：（a）列名 Column（b）这行这列的值 Value

for index, row in df.iterrows():
    for column, value in row.items():
        print(f"{value} 在第 {column} 列，第 {index} 行。")

#
# 选取某一列 or 某一行
#

# 新用法：df.iloc[a, b]，a/b如果是列表（[0, 1]），就是选取指定列；a/b如果是切片（0:-1），就是选取一个区间（从x到y）
# 要注意：df.iloc[[0, 1], 0:-1]  # 0:-1 会漏掉最后一个column；df.iloc[[0, 1], 0:]  # 0: 就不会漏掉了

# 选取单独一行
chosen_row = df.iloc[[0], 0:]  # [0]代表选取第0个Index，0:代表选取从0到-0所有Columns
print(chosen_row)

# 如果要遍历选中的行，要像DataFrame一样遍历
for index, row in chosen_row.iterrows():
    for column, value in row.items():
        print(f"{value} 在第 {column} 列，第 {index} 行。")

# 如果要遍历选中的行，也可以先转换成ndarray，然后更方便遍历
chosen_row_values = chosen_row.values  # [[1 2 3]]
print(chosen_row_values)
for value in chosen_row_values[0]:
    print(value)

# 选取单独一列
chosen_column = df.iloc[0:, [0]]
print(chosen_column)

# 如果要遍历选中的列，要像DataFrame一样遍历
for index, row in chosen_column.iterrows():
    for column, value in row.items():
        print(f"{value} 在第 {column} 列，第 {index} 行。")

# 如果要遍历选中的行，也可以先转换成ndarray，然后更方便遍历
chosen_column_values = chosen_column.values  # [[1], [4], [7]]
chosen_column_values = chosen_column_values.T  # 转置成 [[1 4 7]] 方便遍历
print(chosen_column_values)
for value in chosen_column_values[0]:
    print(value)
