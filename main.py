import math
import tkinter as tk


class FractalApp:

  def __init__(self, root):
    self.root = root
    self.root.title("Лабораторная 1: Простой фрактал")
    self.root.geometry("800, 700")

    # Заголовок
    title_label = tk.Label(
        root, text="Фрактальное дерево", font=("Arial", 16, "bold")
    )
    title_label.pack(pady=10)

    # Холст для рисования
    self.canvas = tk.Canvas(root, width=700, height=500, bg="#222222")
    self.canvas.pack(pady=10)

    # Слайдер для угла ветвления
    slider_frame = tk.Frame(root)
    slider_frame.pack(pady=5)

    tk.Label(slider_frame, text="Угол ветвления:", font=("Arial", 12)).pack(
        side=tk.LEFT, padx=5
    )
    self.angle_slider = tk.Scale(
        slider_frame, from_=0, to=90, orient=tk.HORIZONTAL, length=300, command=self.update_fractal
    )
    self.angle_slider.set(30)  # Начальный угол
    self.angle_slider.pack(side=tk.LEFT, padx=5)

    # Кнопка сброса
    reset_btn = tk.Button(
        root, text="Сбросить (R)", command=self.reset_params, font=("Arial", 10)
    )
    reset_btn.pack(pady=5)

    # Биндим клавиши управления
    self.root.bind("<r>", lambda event: self.reset_params())

    # Первичная отрисовка
    self.draw_fractal()

  def draw_branch(self, x, y, length, angle, depth):
    if depth == 0 or length < 2:
      return

    # Вычисляем координаты конца ветки
    rad = math.radians(angle)
    x_end = x + length * math.sin(rad)
    y_end = y - length * math.cos(rad)

    # Рисуем линию
    self.canvas.create_line(x, y, x_end, y_end, fill="white", width=max(1, depth // 2))

    # Получаем значение угла со слайдера
    branch_angle = self.angle_slider.get()

    # Рекурсивный вызов для двух новых веток
    self.draw_branch(x_end, y_end, length * 0.7, angle + branch_angle, depth - 1)
    self.draw_branch(x_end, y_end, length * 0.7, angle - branch_angle, depth - 1)

  def draw_fractal(self):
    self.canvas.delete("all")
    # Стартовая точка: низ центра холста, длина ствола 120, угол 0 (вверх), 9 итераций
    self.draw_branch(350, 480, 120, 0, 9)

  def update_fractal(self, val):
    self.draw_fractal()

  def reset_params(self):
    self.angle_slider.set(30)
    self.draw_fractal()


if __name__ == "__main__":
  root = tk.Tk()
  app = FractalApp(root)
  root.mainloop()