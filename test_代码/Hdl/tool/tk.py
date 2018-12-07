from tkinter import *
import Main

test = Tk()

# 设置title与尺寸
test.title('测试应用')
test.geometry('500x500')

# 设置顶部标签
Label(test, text='ZC - 测试专用', font=('Arial', 20)).pack(side=TOP)

# 退出按钮
Button(test, text='退出', bg='red', font=('Arial', 12), command=test.quit).pack(side=BOTTOM, pady=20)

# 设置应用布局
fr = Frame(test)
fr.pack()

# 设置应用布局--左布局
fr_L = Frame(fr)
Button(fr_L, text='后台自动化测试').pack(side=TOP)
fr_L.pack(side=LEFT, pady=10, ipadx=20)

# 设置应用布局--右布局
fr_R = Frame(fr)
but = Button(fr_R, text='站群自动化测试', command=lambda: set_list_data(Main.test()))
but.pack(side=TOP)
fr_R.pack(side=RIGHT, ipadx=20, pady=10)


# 传入列表并循环写入lb，供站群自动化测试Button调用
def set_list_data(lists=[]):
    for list in lists:
        lb.insert(END, list)


# 固定的文本展示   不可点击：text.config(state=DISABLED)
text = Text(test, height=2)
text.insert(1.0, '仅用于自动化脚本操作，如有问题，联系开发者：zc -- 18672026447')
text.config(state=DISABLED)
text.pack(side=BOTTOM)

# 单行文本框输入,点击按钮显示对应内容
entry = StringVar()
text_input = Entry(test, textvariable=entry)


# 文字小游戏
def test_game():
    t = entry.get()
    if t == '':
        entry.set('点我干嘛？')
    elif t == '点我干嘛？':
        entry.set('你再点我试试？')
    else:
        entry.set('你还点？')


gameButton = Button(test, text='点我！', command=test_game)
gameButton.pack(side=TOP, pady=3)
text_input.pack(side=TOP, pady=5)

# 创建列表框 + 滚动条布局
test_list = Frame(test)
test_list.pack(pady=10)
scrl_y = Scrollbar(test_list)
scrl_y.pack(side=RIGHT, fill=Y)
scrl_x = Scrollbar(test_list, orient=HORIZONTAL)
scrl_x.pack(side=BOTTOM, fill=X)
lb = Listbox(test_list, height=10, yscrollcommand=scrl_y.set, xscrollcommand=scrl_x.set)
scrl_y['command'] = lb.yview
scrl_x['command'] = lb.xview
lb.pack()

test.mainloop()
