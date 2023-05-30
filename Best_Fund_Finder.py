# 导入所需的库
import pandas as pd
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup

# 读取数据
path = r"e:\codeinfundranking.xlsx"
s1w = pd.read_excel(path, sheet_name="股票1周", dtype='object', header=None)
s1w = s1w.iloc[:, 2]
s1w = s1w.tolist()
s1m = pd.read_excel(path, sheet_name="股票1月", dtype='object', header=None)
s1m = s1m.iloc[:, 2]
s1m = s1m.tolist()
s3m = pd.read_excel(path, sheet_name="股票3月", dtype='object', header=None)
s3m = s3m.iloc[:, 2]
s3m = s3m.tolist()
s6m = pd.read_excel(path, sheet_name="股票6月", dtype='object', header=None)
s6m = s6m.iloc[:, 2]
s6m = s6m.tolist()
h1w = pd.read_excel(path, sheet_name="混合一周", dtype='object', header=None)
h1w = h1w.iloc[:, 2]
h1w = h1w.tolist()
h1m = pd.read_excel(path, sheet_name="混合1月", dtype='object', header=None)
h1m = h1m.iloc[:, 2]
h1m = h1m.tolist()
h3m = pd.read_excel(path, sheet_name="混合3月", dtype='object', header=None)
h3m = h3m.iloc[:, 2]
h3m = h3m.tolist()
h6m = pd.read_excel(path, sheet_name="混合6月", dtype='object', header=None)
h6m = h6m.iloc[:, 2]
h6m = h6m.tolist()

# 合并数据
rank = s1w+s1m+s3m+s6m+h1w+h1m+h3m+h6m
rank = list(set(rank))
rank = [str(i).zfill(6) for i in rank]

# 获取基金代码
html = urlopen('http://fund.eastmoney.com/allfund_com.html')
bs = BeautifulSoup(html.read(), 'html.parser')
nameList = bs.findAll('a', {'title': True, 'class': False})
e = []
for name in nameList:
    c = str(name.get_text())
    d = c[1:7]
    e.append(d)
guangfa = e[e.index('000037'):e.index('873021')]
fuguo = e[e.index('000029'):e.index('588380')]
jiaoyin = e[e.index('000710'):e.index('519787')]
yifangda = e[e.index('000009'):e.index('588080')]
huitianfu = e[e.index('000083'):e.index('560110')]
nanfang = e[e.index('000086'):e.index('588370')]
all_fundcodes = guangfa+fuguo+jiaoyin+yifangda+huitianfu+nanfang+rank
all_fundcodes = list(set(all_fundcodes))

# 获取基金数据
combinedresultdata = []
for fundcode in all_fundcodes:
    str3 = "http://fundf10.eastmoney.com/tsdata_" + fundcode + ".html"
    html = urlopen(str3)
    bs = BeautifulSoup(html.read(), 'html.parser')
    nameList2 = bs.findAll('td', {'class': 'num'})
    resultdata = []
    for name2 in nameList2:
        resultdata.append(name2.get_text())
    combinedresultdata.append(resultdata)
    time.sleep(0.05)

# 数据清洗
csvtitle = ['Year1Std', '2年标准差', '3年标准差', 'Year1Sharpe', '2年夏普比', '3年夏普比', '1年信息比率', '2年信息比率', '3年信息比率']
df = pd.DataFrame(columns=csvtitle, index=all_fundcodes, data=combinedresultdata)
df = df.drop(df[(df.Year1Sharpe == '--')].index)
df = df.drop(df[(df.Year1Sharpe.astype('float') < 1.3)].index)
df["Year1Std"] = pd.to_numeric(df["Year1Std"].str.replace('%', ''))
df = df.drop(df[(df.Year1Std.astype('float') < 9)].index)
df = df.sort_values(by='Year1Sharpe', ascending=False)

# 输出结果
df.to_csv("E:\\sharpofmarket202303231407.csv", encoding="utf_8_sig")
print(df)
