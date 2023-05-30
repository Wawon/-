import baostock as bs
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator


matplotlib.rc("font", family='KaiTi')

"""baostock example"""
lg = bs.login()
rs = bs.query_history_k_data_plus("sz.399300", "date,close", start_date='2016-06-01', frequency="d")
data_list = []
while rs.next():
    data_list.append(rs.get_row_data())
df = pd.DataFrame(data_list, columns=rs.fields)

"""Short-term Averages Auxiliary Lines"""
n = 20  # 短均线的span
short_arithmetic_average = df["close"].rolling(n).mean()
short_weighted_average = df["close"].ewm(span=n, adjust=False).mean()

"""Final Short-term Averages"""
final_short_average = short_weighted_average.copy()
for i in range(len(short_arithmetic_average)):
    final_short_average[i] = short_weighted_average[i] * 2 - short_arithmetic_average[i]

"""Long-term Averages Auxiliary Lines"""
m = 150
long_arithmetic_average = df["close"].rolling(m).mean()
long_weighted_average = df["close"].ewm(span=m, adjust=False).mean()

"""Final Long-term Averages"""
final_long_average = long_arithmetic_average.copy()
for i in range(len(long_arithmetic_average)):
    final_long_average[i] = long_weighted_average[i] * 2 - long_arithmetic_average[i]


"""Deviation Line"""
m = 3000  # m是图形在y轴的上移量
deviation = final_short_average - final_long_average + m
deviation_mean = deviation.mean()
deviation_max = deviation.max()
deviation_min = deviation.min()
up_bound = deviation_max * 0.35 + deviation_mean * 0.65
low_bound = deviation_mean * 0.65 + deviation_min * 0.35

"""Charting"""
fig = plt.figure()  # 创建图形
ax = plt.axes()  # 创建维度
plt.style.use('classic')
df["close"] = pd.to_numeric(df["close"], errors='coerce')
x = df.date
y = df.close
x_major_locator = MultipleLocator(30)  # x轴刻度间距
ax.xaxis.set_major_locator(x_major_locator)
plt.xticks(rotation=45)  # x轴刻度文字旋转
plt.tick_params(labelsize=9)  # x轴刻度文字大小
matplotlib.rc("font", family='KaiTi')
ax.plot(x, y, color='black', linestyle='-',label='收盘价')
ax.plot(x, deviation, color='blue', linestyle='-',label='偏离度')
ax.plot(x, final_long_average, color='purple', linestyle='-',label='长均线')
ax.plot(x, final_short_average, color='orange', linestyle='-',label='短均线')
# ax.axhline(up_bound, color='blue', linestyle=':')
ax.axhline(m, color='blue', linestyle='-.')
# ax.axhline(low_bound, color='blue', linestyle=':')
matplotlib.rc("font", family='KaiTi')
plt.legend(loc='best')
plt.title("沪深300-两均线偏离度")
plt.axis('tight')
matplotlib.rc("font", family='KaiTi')
plt.show()

bs.logout()
