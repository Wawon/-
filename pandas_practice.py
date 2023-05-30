import pandas as pd

# 创建DataFrame对象
df = pd.DataFrame({'ID:': [1, 2, 3, 4], 'Name:': ['JosephBean', 'Nick', 'Joshua', 'Mike']})

# 把ID所在的列设置为索引
df = df.set_index('ID:')

# 将DataFrame对象写入d盘的people.xlsx文件
# r 为转义符，避免后面出现\n \t被识别为换行和tab
df.to_excel(r'D:\people.xlsx')

# 读取excel, header=0表示表头为表格第一行
excel = pd.read_excel(r'D:\people.xlsx', header=0)
# print(excel)
# print(excel.shape)  # 输出行数和列数
# print(excel.columns)  # 输出列的名字
# print(excel.head(3))  # 输出前三行
# print(excel.tail(3))  # 输出尾三行

# 读取people，但是理解为没有表头 全是数据
excel = pd.read_excel(r'D:\people.xlsx', header=0)
# excel.columns = ['id', 'name']  # 表头设置为id 和 name
# excel = excel.set_index('id')  # 把索引设置为id
excel.to_excel(r'D:\people.xlsx')  # 写入

print(excel)
# print(excel.head())
