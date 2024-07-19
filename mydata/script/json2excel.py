import pandas as pd
import json

# 假设你的 JSON 数据存储在 'data.json' 文件中
with open('tasks/webarena/test.raw.json', 'r') as file:
    data = json.load(file)

# 将 JSON 数据转换为 DataFrame
df = pd.json_normalize(data)

# 将 DataFrame 转换为 Excel 文件
df.to_excel('output.xlsx', index=False)