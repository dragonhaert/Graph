import tkinter


class GUI:
    def __init__(self, title, w, h):
        self.title = title
        self.width = w
        self.height = h
        self.root = tkinter.Tk()
        self.root.title(title)
        self.frame = tkinter.Frame(self.root, width=w, height=h)
        self.frame.pack()
        self.canvas = tkinter.Canvas(self.frame, width=w, height=h)
        self.canvas.pack()

    def update(self):
        self.root.update()
        self.root.update_idletasks()

    def clear(self):
        self.canvas.delete('ALL')

    def ellipse(self, x, y, w, h, color='black'):
        self.canvas.create_oval(x, y, x+w, y+h, fill=color)

    def rect(self, x, y, w, h, color='black'):
        self.canvas.create_rectangle(x, y, w, h, fill=color)

    def line(self, x1, y1, x2, y2, color='black', width=1):
        self.canvas.create_line(x1, y1, x2, y2, fill=color, width=width)


window = GUI('Graph', 600, 600)
