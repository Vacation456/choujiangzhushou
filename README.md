# 抽奖

## test



```python
import tkinter
import random

def load_names_from_file(filename):
    with open(filename, "r") as file:
        names = file.readlines()
        # 去除每个姓名末尾的换行符
        names = [name.strip() for name in names]
    return names

def random_name():
    if names:
        name = random.choice(names)
        name_label.config(text="随机点名：" + name)
    else:
        name_label.config(text="名单为空")

MyWin = tkinter.Tk()
MyWin.title('随机点名程序')
MyWin.geometry("300x150")

names = load_names_from_file("names.txt")  # 从文件加载姓名列表

name_label = tkinter.Label(MyWin, text="随机点名：")
name_label.pack(pady=20)

random_button = tkinter.Button(MyWin, text="随机点名", command=random_name)
random_button.pack()

MyWin.mainloop()
```

![image-20240330131801280](C:\Users\Vacat\AppData\Roaming\Typora\typora-user-images\image-20240330131801280.png)

这是一个链接 [Markdown语法](https://markdown.com.cn "最好的markdown教程")

### sdfgfh

