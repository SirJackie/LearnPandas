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
