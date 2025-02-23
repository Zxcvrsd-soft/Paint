from tkinter import *

class PaintApp:
    def __init__(self, master):
        self.master = master
        self.color = 'black'  # Цвет кисти по умолчанию
        self.brush_size = 2   # Размер кисти по умолчанию
        self.x = None         # Координата X предыдущей точки
        self.y = None         # Координата Y предыдущей точки
        self.pen_down = False # Флаг, указывающий, нажата ли кнопка мыши

        # Создаем холст для рисования
        self.canvas = Canvas(self.master, width=800, height=600, bg='white')
        self.canvas.pack(fill=BOTH, expand=True)

        # Привязываем события мыши к методам
        self.canvas.bind('<Button-1>', self.on_pen_down)
        self.canvas.bind('<B1-Motion>', self.on_mouse_move)
        self.canvas.bind('<ButtonRelease-1>', self.on_pen_up)

    def on_pen_down(self, event):
        """Обработчик нажатия кнопки мыши"""
        self.pen_down = True
        self.x = event.x
        self.y = event.y

    def on_mouse_move(self, event):
        """Обработчик движения мыши"""
        if self.pen_down:
            self.draw_line(event.x, event.y)
            self.x = event.x
            self.y = event.y

    def on_pen_up(self, event):
        """Обработчик отпускания кнопки мыши"""
        self.pen_down = False

    def draw_line(self, x, y):
        """Рисует линию от последней позиции мыши до текущей"""
        self.canvas.create_line(self.x, self.y, x, y, fill=self.color, width=self.brush_size)

if __name__ == '__main__':
    root = Tk()
    root.title('Paint App')
    app = PaintApp(root)
    root.mainloop()