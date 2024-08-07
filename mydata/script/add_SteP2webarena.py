import pandas as pd

# 读取两个Excel文件
df1 = pd.read_excel('mydata/process/SteP_WebArena.xlsx')
df2 = pd.read_csv('log-all/summary.csv')

# 合并数据
merged_df = pd.merge(df1, df2, on='task_id', how='outer')

# 保存合并后的数据到新的Excel文件
merged_df.to_excel('mydata/SteP_WebArena_all_result.xlsx', index=False)