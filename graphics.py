from tkinter import Tk, Canvas


def createCanvas(width, height, title):
    window = Tk()
    window.title(title)
    canvas = Canvas(window, width=width, height=height)
    canvas.pack()
    return canvas

def clear(canvas, object="all"):
    canvas.delete(object)

def drawLine(canvas, x1, y1, x2, y2, color="black"):
    return canvas.create_line(x1, y1, x2, y2, fill=color)


if __name__ == "__main__":
    canvas = createCanvas(500, 500)
    input("continue ?")
    line = drawLine(canvas, 0, 0, 500, 500, "red")
    input("continue ?")
    clear(canvas, line)
    input("quit ?")