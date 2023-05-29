# 导入所需的库
import schedule
import time

# 设置下班时间（17:00）和午休时间（11:30）
xbh, xbm, wxh, wxm = 17, 0, 11, 30

# 计算距离目标时间还有多少小时、分钟和秒
def time_remaining(target_hour, target_min):
    t = time.localtime()
    hours_remaining = target_hour - t.tm_hour - (1 if target_min <= t.tm_min else 0)
    minutes_remaining = target_min - t.tm_min if target_min > t.tm_min else 59 - t.tm_min + target_min
    seconds_remaining = 60 - t.tm_sec
    return hours_remaining, minutes_remaining, seconds_remaining

# 计算并显示距离下班还有多久
def off_count():
    h_remain, m_remain, s_remain = time_remaining(xbh, xbm)
    print(f"\n现在是北京时间 {time.strftime('%H点 %M分 %S秒')}")
    print(f"距离下班还有 {h_remain}小时 {m_remain}分 {s_remain}秒")

# 计算并显示距离午休时间还有多久
def nap_count():
    a_h, a_m, a_s = time_remaining(wxh, wxm)
    print(f"距离午休时间还有 {a_h}小时 {a_m}分 {a_s}秒")

# 根据当前时间决定显示距离下班还是距离午休的时间
def time_rule():
    t = time.localtime()
    if t.tm_hour < 17:
        off_count()
    if t.tm_hour < 11 or (t.tm_hour == 11 and t.tm_min < 30):
        nap_count()

# 每隔1秒执行一次 time_rule 函数
schedule.every(1).seconds.do(time_rule)

# 无限循环，执行计划任务
while True:
    schedule.run_pending()
    time.sleep(1)
