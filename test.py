# conding = UTF-8
from tkinter import *

class CanvasDemo:
        def __init__(self):
            window = Tk()
            window.title = ("Canvas Demo")# define the name of window

            #在窗口画布
            self.canvas = Canvas(window, width = 200, height = 100, bg = "white")
            self.canvas.pack()#将小部件放进主窗口中

            #创建frame框架，窗口window为这个框架额父容器
            frame = Frame(window)
            frame.pack()
            #frame框架作为Button的父容器
            btRectangle = Button(frame, text = "rectangle", command = self.displayRect())
            btOval = Button(frame, text = "Oval", command = self.displayOval)
            btArc = Button(frame, text = "Arc", command = self.displayArc)
            btPolygon = Button(frame, text = "Polygon", command = self.displayPolygon)
            btLine = Button(frame, text = "Line", command = self.displayLine)
            btString = Button(frame, text = "String", command = self.displayString)
            btClear = Button(frame, text = "Clear", command = self.displayClear)

            #Button 在画布上的布局
            btRectangle.grid(row = 1, column = 1)
            btOval.grid(row = 1, column = 2)
            btArc.grid(row = 1, column = 3)
            btPolygon.grid(row = 1, column = 4)
            btLine.grid(row = 1, column = 5)
            btString.grid(row = 1, column = 6)
            btClear.grid(row = 1, column = 7)

            #创建时间循环直到关闭主窗口
            window.mainloop()

        def displayRect(self):
            self.canvas.create_rectangle(10, 10, 190, 90, tags = "rect")

        def displayOval(self):
            self.canvas.create_oval(10, 10, 190, 90, fill = "red", tags = "oval")

        def displayArc(self):
            self.canvas.create_arc(10, 10, 190, 90, start = 0, extent = 90, width = 8, fill = "red", \
                                   tags = "arc")
        def displayPolygon(self):
            self.canvas.create_polygon(10, 10, 190, 90, 10, 90, tags = "polygon")

        def displayLine(self):
            self.canvas.create_line(10, 10, 190, 90, fill = "red", tags = "line")
            self.canvas.create_line(10, 10, 190, 90, width = 9, arrow = "first", activefill = "blue", tags = "line")

        def displayString(self):
            self.canvas.create_text(60, 40, text = "hi, I am string", font = "time 10 bold underline", tags = "string")

        def displayClear(self):
            self.canvas.delete("rect", "oval", "arc", "polygon", "line", "string")

CanvasDemo()