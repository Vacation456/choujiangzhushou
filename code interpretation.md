# 点名助手

```python
import pandas as pd
import tkinter as tk
from tkinter import ttk
import random
from threading import Thread
import time


class LotteryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("随机点名")
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

```

# 代码解释

```shell
这段代码是一个简单的基于Tkinter的GUI应用程序，用于随机点名。让我逐步解释它：

导入必要的库：

pandas：用于处理Excel文件中的数据。
tkinter：Python的标准GUI库。
Thread：用于实现多线程。
time：用于暂停线程一段时间。
LotteryApp 类：

__init__ 方法：初始化应用程序的界面和数据。它加载一个名为"名单.xlsx"的Excel文件，其中包含学生的学号和姓名信息，并创建了应用程序的界面。
setup_ui 方法：设置应用程序的用户界面，包括标签和按钮。
start 方法：开始随机点名。它创建一个新线程来调用 update 方法。
stop 方法：停止随机点名，将 running 标志设置为 False。
update 方法：在运行时不断更新界面，每次随机选择一个学生并显示其学号和姓名。
main 函数：

创建一个 Tkinter 应用程序实例。
创建 LotteryApp 实例并将其传递给 Tkinter 应用程序。
开始 Tkinter 的事件循环。
if __name__ == "__main__":：

如果这个脚本被直接执行，则调用 main 函数。
要使用这个应用程序，您需要确保有一个名为"名单.xlsx"的Excel文件，其中包含至少两列，一列是学生的学号，另一列是学生的姓名。然后运行这个脚本，即可启动随机点名应用程序的界面。

```

# 代码注释版

```python
import pandas as pd  # 导入pandas库用于数据处理
import tkinter as tk  # 导入tkinter库用于GUI编程
from tkinter import ttk  # 导入ttk模块中的组件
import random  # 导入random库用于生成随机数
from threading import Thread  # 导入Thread类用于多线程编程
import time  # 导入time库用于时间相关操作


class LotteryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("随机点名")  # 设置窗口标题
        self.root.geometry("400x200")  # 设置窗口大小

        self.students = pd.read_excel("名单.xlsx")  # 从Excel文件中读取学生名单数据
        self.running = False  # 标志位，用于标识抽奖是否正在进行

        self.setup_ui()  # 初始化界面布局

    def setup_ui(self):
        self.info_frame = ttk.Frame(self.root)  # 创建信息展示框架
        self.info_frame.pack(pady=20)  # 放置信息展示框架并设置垂直间距

        self.student_id_label = ttk.Label(self.info_frame, text="学号:", font=("Arial", 16))  # 创建学号标签
        self.student_id_label.pack()  # 放置学号标签

        self.name_label = ttk.Label(self.info_frame, text="姓名:", font=("Arial", 16))  # 创建姓名标签
        self.name_label.pack()  # 放置姓名标签

        self.buttons_frame = ttk.Frame(self.root)  # 创建按钮框架
        self.buttons_frame.pack(pady=20)  # 放置按钮框架并设置垂直间距

        self.start_button = ttk.Button(self.buttons_frame, text="开始", command=self.start)  # 创建开始按钮
        self.start_button.pack(side=tk.LEFT, padx=10)  # 放置开始按钮并设置水平间距

        self.stop_button = ttk.Button(self.buttons_frame, text="停止", command=self.stop)  # 创建停止按钮
        self.stop_button.pack(side=tk.RIGHT, padx=10)  # 放置停止按钮并设置水平间距

    def start(self):
        if not self.running:  # 如果抽奖没有在进行
            self.running = True  # 将抽奖标志位设置为True
            self.thread = Thread(target=self.update)  # 创建新线程用于执行抽奖更新
            self.thread.start()  # 启动新线程

    def stop(self):
        self.running = False  # 将抽奖标志位设置为False，停止抽奖

    def update(self):
        while self.running:  # 当抽奖在进行中时
            # 随机选择一个学生
            winner = self.students.sample(n=1).iloc[0]  # 从学生名单中随机抽取一个学生
            student_id = winner['学号']  # 获取学号
            name = winner['姓名']  # 获取姓名

            # 更新标签显示信息
            self.student_id_label.config(text=f"学号: {student_id}")  # 更新学号标签
            self.name_label.config(text=f"姓名: {name}")  # 更新姓名标签

            time.sleep(0.1)  # 短暂等待，以便用户可以看到不同的名字


def main():
    root = tk.Tk()  # 创建根窗口
    app = LotteryApp(root)  # 创建抽奖应用实例
    root.mainloop()  # 进入主事件循环


if __name__ == "__main__":
    main()

```

