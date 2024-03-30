import pandas as pd
import tkinter as tk
from tkinter import ttk
import random
from threading import Thread
import time


class LotteryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("随机抽奖")
        self.root.geometry("400x200")  # 增大窗口尺寸

        self.students = pd.read_excel("名单.xlsx")
        self.running = False

        self.setup_ui()

    def setup_ui(self):
        self.info_frame = ttk.Frame(self.root)
        self.info_frame.pack(pady=20)

        self.student_id_label = ttk.Label(self.info_frame, text="学号:", font=("Arial", 16))
        self.student_id_label.pack()

        self.name_label = ttk.Label(self.info_frame, text="姓名:", font=("Arial", 16))
        self.name_label.pack()

        self.buttons_frame = ttk.Frame(self.root)
        self.buttons_frame.pack(pady=20)

        self.start_button = ttk.Button(self.buttons_frame, text="开始", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = ttk.Button(self.buttons_frame, text="停止", command=self.stop)
        self.stop_button.pack(side=tk.RIGHT, padx=10)

    def start(self):
        if not self.running:
            self.running = True
            self.thread = Thread(target=self.update)
            self.thread.start()

    def stop(self):
        self.running = False

    def update(self):
        while self.running:
            # 随机选择一个学生
            winner = self.students.sample(n=1).iloc[0]
            student_id = winner['学号']
            name = winner['姓名']

            # 更新标签显示信息
            self.student_id_label.config(text=f"学号: {student_id}")
            self.name_label.config(text=f"姓名: {name}")

            time.sleep(0.1)  # 短暂等待，以便用户可以看到不同的名字


def main():
    root = tk.Tk()
    app = LotteryApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
