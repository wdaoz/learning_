import time

def start_focus_timer(duration):
    print("开始专注")
    time.sleep(duration * 60)
    print("时间到！专注结束")

if __name__ == "__main__":
    duration = int(input("请输入专注时长（分钟）："))
    start_focus_timer(duration)
