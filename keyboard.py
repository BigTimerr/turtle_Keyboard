import turtle as t


"""
@Author：ruetrash
@Time：2021-11-24

本文使用turtle库，实现了一个自动绘制87键键盘的程序.
本次程序不完善，只编写87键部分键位
"""

list1 = ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12"]
list2 = ["`~", "1!", "2@", "3#", "4$", "5%", "6^", "7&", "8*", "9(", "0)", "-_", "=+"]
list3 = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "p", "{ [)", "] }"]
list4 = ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";:", "'\""]
list5 = ["Z", "X", "C", "V", "B", "N", "M", ",<", ".>", "/?", ]
list6 = ["Ctrl", "Win", "Alt", "Alt", "win", "Fn", "Ctrl"]


# 得到当前光标所在位置
def getpos():
    pos = t.pos()
    return pos


# 将小乌龟跳转到哪个像素点
def gotoxy(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


# 将小乌龟跳转到哪个像素点,并且将修改后的x的值返回
def gotoxyAndReturnx(x, y, i):
    t.penup()
    x = x + i
    t.goto(x, y)
    t.pendown()
    return x


# 画一个正方形（40*40）的键
def drawKey(x, y, str):
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.penup()
    t.goto(x + 10, y - 20)
    t.write(str)
    t.goto(x, y)
    t.pendown()


# 画一个大小不规则的键，Str是键的名称，length是键的长度
def drawKeyOfLarge(x, y, str, length):
    t.forward(length)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.penup()
    t.goto(x + 10, y - 20)
    t.write(str)
    t.goto(x, y)
    t.pendown()

# 画F键，因为f键中间有空隙  所以单写了一个函数，也可以把list1中间加上空格，也是一样的效果
def drawFKeys(x, y):
    flag = 1
    for i in list1:
        drawKey(x, y, i)
        x = gotoxyAndReturnx(x, y, 40)
        if flag % 4 == 0:
            x = gotoxyAndReturnx(x, y, 40)
        flag += 1


def drawFirstLine(x, y):
    for i in list2:
        drawKey(x, y, i)
        x = gotoxyAndReturnx(x, y, 40)
    drawKeyOfLarge(x, y, "Backspace", 120)


def drawSecondLine(x, y):
    drawKeyOfLarge(x, y, "Tab", 60)
    x = gotoxyAndReturnx(x, y, 60)
    for i in list3:
        drawKey(x, y, i)
        x = gotoxyAndReturnx(x, y, 40)
    drawKeyOfLarge(x, y, "\\ |", 100)


def drawThirdLine(x, y):
    drawKeyOfLarge(x, y, "Caps", 80)
    x = gotoxyAndReturnx(x, y, 80)
    for i in list4:
        drawKey(x, y, i)
        x = gotoxyAndReturnx(x, y, 40)
    drawKeyOfLarge(x, y, "Enter", 120)


def drawFourLine(x, y):
    drawKeyOfLarge(x, y, "Shift", 100)
    x = gotoxyAndReturnx(x, y, 100)
    for i in list5:
        drawKey(x, y, i)
        x = gotoxyAndReturnx(x, y, 40)
    drawKeyOfLarge(x, y, "Shift", 140)


def drawFiveLine(x, y):
    flag = 1
    for i in list6:
        if flag == 4:
            drawKeyOfLarge(x, y, "Space", 290)
            x = gotoxyAndReturnx(x, y, 290)
        drawKeyOfLarge(x, y, i, 50)
        x = gotoxyAndReturnx(x, y, 50)
        flag += 1


# 设置窗口大小
t.screensize(1600, 800, "white")
t.screensize()  # 返回默认大小(400, 300)
t.setup(1600, 1000)

#设置小乌龟移动速度
t.speed(10)

# 将小乌龟移动到窗口左上角
t.penup()
t.fd(-750)
t.left(90)
t.forward(450)
t.right(90)
t.pendown()

# 绘制键盘背景
t.forward(1000)
t.right(90)
t.forward(400)
t.right(90)
t.forward(1000)
t.right(90)
t.forward(400)
t.right(90)
# (-750.00,450.00)

# 绘制esc键
gotoxy(-720, 420)
drawKey(-720, 420, "Esc")

# 绘制f键
gotoxy(-640, 420)
drawFKeys(-640, 420)

# 绘制键盘第一行
gotoxy(-720, 360)
drawFirstLine(-720, 360)

# 绘制第二行
gotoxy(-720, 320)
drawSecondLine(-720, 320)

# 第三行
gotoxy(-720, 280)
drawThirdLine(-720, 280)

# 第四行
gotoxy(-720, 240)
drawFourLine(-720, 240)

# 第五行
gotoxy(-720, 200)
drawFiveLine(-720, 200)

# 绘制完成后，点击退出
t.exitonclick()
