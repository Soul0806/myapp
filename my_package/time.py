import time

class MyTime:
    def __init__(self):
        self.localtime = time.localtime() # 取得 struct_time 格式的時間
        
    def get_strftime(self):
        return time.strftime("%y-%m-%d, %H:%M:%S", self.localtime) # 依指定格式輸出
