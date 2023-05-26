import schedule
import time

xbh, xbm, wxh, wxm = 17, 0, 11, 30

def time_remaining(target_hour, target_min):
    t = time.localtime()
    hours_remaining = target_hour - t.tm_hour - (1 if target_min <= t.tm_min else 0)
    minutes_remaining = target_min - t.tm_min if target_min > t.tm_min else 59 - t.tm_min + target_min
    seconds_remaining = 60 - t.tm_sec
    return hours_remaining, minutes_remaining, seconds_remaining

def off_count():
    h_remain, m_remain, s_remain = time_remaining(xbh, xbm)
    print(f"\n现在是北京时间 {time.strftime('%H点 %M分 %S秒')}")
    print(f"距离下班还有 {h_remain}小时 {m_remain}分 {s_remain}秒")

def nap_count():
    a_h, a_m, a_s = time_remaining(wxh, wxm)
    print(f"距离午休时间还有 {a_h}小时 {a_m}分 {a_s}秒")

def time_rule():
    t = time.localtime()
    if t.tm_hour < 17:
        off_count()
    if t.tm_hour < 11 or (t.tm_hour == 11 and t.tm_min < 30):
        nap_count()

schedule.every(1).seconds.do(time_rule)

while True:
    schedule.run_pending()
    time.sleep(1)
