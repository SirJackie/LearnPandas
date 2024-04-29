import pandas as pd

df = pd.DataFrame(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    index=["Index1", "Index2", "Index3"],
    columns=["Col1", "Col2", "Col3"]
)

# df.reset_index()：把 Index列 转换成 普通列
df_index_inside = df.reset_index()
df_column_inside = df.transpose().reset_index().transpose()
print(df_index_inside)
print(df_column_inside)

# df.set_index()：把 普通列 转换成 Index列
df_index_outside = df_index_inside.set_index("index")
df_column_outside = df_column_inside.transpose().set_index("index").transpose()
print(df_index_outside)
print(df_column_outside)
