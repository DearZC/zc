from tkinter import *

test = Tk()

test.title('张晨测试')
test.geometry('500x500')

a = Label(test, text = '测试', bg = 'red', font = ('Arial', 12), width = 5, height = 2)
a.pack(side = BOTTOM)

Label(test, text = '校训', font = ('Arial', 20)).pack(side = TOP)
fr = Frame(test)

fr_L = Frame(fr)
Label(fr_L, text = '博学', font = ('Arial', 15)).pack(side = TOP)
Label(fr_L, text = '厚德', font = ('Arial', 15)).pack(side = TOP)
fr_L.pack(side = LEFT)

fr_R = Frame(fr)
Label(fr_R, text = '敬业', font = ('Arial', 15)).pack(side = TOP)
Label(fr_R, text = '乐群', font = ('Arial', 15)).pack(side = TOP)
fr_R.pack(side = RIGHT)

fr.pack()

var = StringVar()
test_Entry = Entry(test, textvariable = var)
var.set('请输入测试内容')
test_Entry.pack()

text = Text(test)
text.insert(1.0, 'zc\n')
text.insert(2.0, 'test\n')
text.pack()


Button(test, text = '确认', command = ).pack(side = BOTTOM)

test.mainloop()
