# -*- encoding: utf-8 -*-

from datetime import datetime, timedelta
import time
import random


def random_time_cmd(n:int, dtfrom:datetime):
    dtlist : list[datetime] = []
    random.seed(datetime.now().microsecond)
    sec_delta = dtfrom
    for i in range(n):
        sec_delta = sec_delta + timedelta(seconds=random.randint(0,40))
        dtlist.append(sec_delta)
    return dtlist



if __name__ == '__main__':
    daytime = datetime.strptime("2025-09-08 14:04:54", "%Y-%m-%d %H:%M:%S")
    random_time = random_time_cmd(10, daytime)
    for dt in random_time:
        print(f"{dt.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"\t{dt.strftime('%Y%m%d%H%M%S')}")
        print(f"\t{dt.month}/{dt.day}/{dt.strftime("%Y %H:%M:%S")}")
    # print(f"当前时间：{time.time()}")
    # print(f"当前时间：{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
    # random.seed(time.time())
    # print(random.randint(0, 30))
    # now = datetime.now()
    # print(f"today is {now.strftime('%Y-%m-%d %H:%M:%S%p')}")
    # daytime = datetime.strptime("2025-09-18 14:04:54", "%Y-%m-%d %H:%M:%S")
    # print(f"daytime is {daytime.strftime('%Y-%m-%d %H:%M:%S%p')}")
    # daytimex = daytime + timedelta(seconds=random.randint(1, 50))
    # print(f"daytime is {daytimex.strftime('%Y-%m-%d %H:%M:%S%p')}")


