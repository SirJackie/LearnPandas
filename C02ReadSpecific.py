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
# 选取某一列 or 某一行
#

# 新用法：df.iloc[sth, sth]
# - sth如果是列表（[0, 1]），就是选取指定列 => 输出一个DataFrame
# - sth如果是切片（0:-1），就是选取一个区间（从x到y） => 输出一个DataFrame
# - sth如果是数值（0），就是选取唯一列 => 输出一个Series
# - sth如果两个都是数值（df.iloc[0, 0]），就是选取x列y行的，单独一个数值 => 输出一个int32

# 要注意：# “0:-1”会漏掉最后一个column，但“0:”就不会漏掉了

# --- 方法1：选取出一个DataFrame ---
# 选取单独一行
chosen_row = df.iloc[[0], 0:]  # [0]代表选取第0个Index（as one of the indexes），0:代表选取从0到-0所有Columns
# 选取单独一列
chosen_column = df.iloc[0:, [0]]
# 打印结果
print(chosen_row, chosen_column)
print(chosen_column.values)  # [[1], [4], [7]], harder to iterate

# --- 方法2：选取出一个Series ---
# 选取单独一行
chosen_row = df.iloc[0, 0:]  # 0代表选取第0个Index（as THE ONLY index），0:代表选取从0到-0所有Columns
# 选取单独一列
chosen_column = df.iloc[0:, 0]
# 打印结果
print(chosen_row, chosen_column)
print(chosen_column.values)  # [1 4 7], easier to iterate

#
# 选取特定地方的单独一个值
#

the_value = df.iloc[1, 2]  # should be int32: 6
print(the_value)
