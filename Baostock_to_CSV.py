import baostock as bs
import pandas as pd
import time, sys

while True:
    lg = bs.login()
    print ('login respond error_code:' +lg.error_code)
    print ('login respond error_msg:' +lg.error_msg)

    rs = bs.query_history_k_data_plus("sh.000001",
        "date,code,open,high,low,close",
        start_date='2017-12-06', frequency="d")
    print('query_history_k_data_plus respond error_code:'+rs.error_code)
    print('query_history_k_data_plus respond error_msg:'+rs.error_msg)

    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)
    # 结果集输出到csv文件
    result.to_csv("E:\\5y_history_Index_k_data.csv", index=False)
    print(result)

    bs.logout()
    time.sleep(43200)
