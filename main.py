import tkinter

# constants
WIDTH_OF_CANVAS = 600
HEIGHT_OF_CANVAS = 400
COLOR_OF_CANVAS = 'green'
SIZE_OF_ROOT_WINDOW = '600x400'
DELAY = 80
x = 0
y = 0
dx = 10
dy = 5


def update_of_canvas():
    global x, y, dx, dy
    canvas.delete("all")
    canvas.create_oval(x, y, x + 20, y + 20, fill='red', outline='black')
    x = x + dx
    y = y + dy
    print(x)
    canvas.pack()
    canvas.after(DELAY, update_of_canvas)


root_window = tkinter.Tk()
root_window.title("Полет шаров")
root_window.geometry(SIZE_OF_ROOT_WINDOW)
canvas = tkinter.Canvas(root_window, width=WIDTH_OF_CANVAS, height=HEIGHT_OF_CANVAS, bg=COLOR_OF_CANVAS)
update_of_canvas()
root_window.mainloop()
