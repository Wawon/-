import pandas as pd
import datetime

"""构造完整文件路径"""
pathhead = r"c:\Users\PC220614-01\Documents\WeChat Files\wxid_lexgpzplf7dv22\FileStorage\File"
now = datetime.datetime.now()
pathdate = now.strftime("\%Y-%m")
# 收到新月报了就把文件名复制到下面这行，下面这行的文件名前面要加捺斜线
filename = "\XX.xlsx"
fullpath = pathhead+pathdate+filename

"""期现业务数据抓取"""
qx = pd.read_excel(fullpath, sheet_name="商品现货贸易MR003", header=0)
mr003a = round((qx.iloc[-1, 1])/100000000, 2)  # 现货采购额
mr003b = round((qx.iloc[-1, 4])/100000000, 2)  # 现货销售额

"""场外衍生品业务数据抓取"""
# 当期参与交易客户数
NumberofCustomers = pd.read_excel(fullpath, sheet_name="期现业务服务产业客户情况MR007", header=0)
mr007 = NumberofCustomers.iloc[-6, -1]
# 月份的构造
now = datetime.datetime.now()
OldMonth1 = now - datetime.timedelta(days=30)
lastmonth = OldMonth1.strftime("%Y年%m月")
# 商品衍生品数据抓取
Commodity_Derivatives = pd.read_excel(fullpath, sheet_name="商品衍生品交易MR008-009", header=0)
mr008a = Commodity_Derivatives.iloc[9, 3]  # 期权类本月新增名义本金
mr008b = Commodity_Derivatives.iloc[10, 3]  # 远期类本月新增名义本金
mr008 = round((mr008a+mr008b)/100000000, 2)  # 商品类本月新增名义本金小计（亿元）
# 金融衍生品数据抓取
Financial_Derivatives = pd.read_excel(fullpath, sheet_name="金融衍生品交易MR010-011", header=0)
mr010a = Financial_Derivatives.iloc[12, 4]  # 互换类本月新增名义本金
mr010b = Financial_Derivatives.iloc[17, 4]  # 期权类本月新增名义本金
mr010 = round((mr010a + mr010b)/100000000, 2)  # 金融类本月新增名义本金小计（亿元）

"""做市业务数据抓取"""
# 期货做市
Futures_MarketMaking = pd.read_excel(fullpath, sheet_name="期货做市业务MR013", header=0)
mr013a = round(Futures_MarketMaking.iloc[-1, 1]/10000, 2)  # 期货做市成交量
mr013b = round(Futures_MarketMaking.iloc[-1, 2]/100000000, 2)  # 期货做市成交额
# 期权做市
Options_MarketMaking = pd.read_excel(fullpath, sheet_name="场内期权做市业务MR014", header=0)
mr014a = round((Options_MarketMaking.iloc[-1, 1] + Options_MarketMaking.iloc[-1, 3])/10000, 2)  # 期权成交手数（万）
mr014b = round((Options_MarketMaking.iloc[-1, 2] + Options_MarketMaking.iloc[-1, 4])/100000000, 2) # 期权成交额（亿）

"""数值范围自动审核"""
if not (7 < mr003a < 20 and 4 < mr003b < 20):
    print("mr003检测到异常数据，请人工核对")
if not 90 < mr007 < 533:
    print("mr007检测到异常数据，请人工核对")
if not 35 < mr008 < 120:
    print("mr008检测到异常数据，请人工核对")
if not 7 < mr010 < 46:
    print("mr010检测到异常数据，请人工核对")
if not 151 < mr013a < 700:
    print("mr013a检测到异常数据，请人工核对")
if not 726 < mr013b < 3500:
    print("mr013b检测到异常数据，请人工核对")
if not 165 < mr014a < 1000:
    print("mr014a检测到异常数据，请人工核对")
if not 16 < mr014b < 60:
    print("mr014b检测到异常数据，请人工核对")

"""布局变更检测"""
if not qx.iloc[-1, 0] == "合计" and qx.iloc[7, 1] == "本月现货采购金额":
    print("MR003布局已变更，请更改程序中的位置参数")
if not NumberofCustomers.iloc[11, 0] == "当期参与交易的客户数量":
    print("MR007布局已变更，请更改程序中的位置参数")
if not Commodity_Derivatives.iloc[9, 1] == "期权类":
    print("MR008布局已变更，请更改程序中的位置参数")
if not Financial_Derivatives.iloc[17, 2] == "合计":
    print("MR010布局已变更，请更改程序中的位置参数")
if not Futures_MarketMaking.iloc[66, 0] == "小计":
    print("MR013布局已变更，请更改程序中的位置参数")
if not Options_MarketMaking.iloc[49, 0] == "合计":
    print("MR014布局已变更，请更改程序中的位置参数")
    print(Options_MarketMaking.iloc[49, 0])

"""最终输出"""
print(f"（一）期现业务：{lastmonth},公司期现业务现货采购额{mr003a}亿元,销售额{mr003b}亿元,当期参与交易客户数{mr007}家。")
print(f"（二）场外衍生品业务：商品衍生品新增名义本金{mr008}亿元，金融衍生品名义新增名义本金{mr010}亿元。")
print(f"（三）做市业务：期货做市成交量{mr013a}万手，成交额{mr013b}亿元；期权做市成交量{mr014a}万手，成交额{mr014b}亿元。")
