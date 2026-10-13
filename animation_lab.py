import math
import tkinter as tk


class CircleAnimationApp:

  def __init__(self, root):
    self.root = root
    self.root.title("Лабораторная 2: Анимация круга")
    self.root.geometry("800, 700")

    title_label = tk.Label(
        root, text="Анимация: Превращение круга в треугольник", font=("Arial", 16, "bold")
    )
    title_label.pack(pady=10)

    self.canvas = tk.Canvas(root, width=700, height=500, bg="#e0e0e0")
    self.canvas.pack(pady=10)

    # Панель управления
    control_frame = tk.Frame(root)
    control_frame.pack(pady=5)

    self.is_paused = False
    self.pause_btn = tk.Button(
        control_frame, text="Пауза (Space)", command=self.toggle_pause, font=("Arial", 10)
    )
    self.pause_btn.pack(side=tk.LEFT, padx=5)

    reset_btn = tk.Button(
        control_frame, text="Сброс (R)", command=self.reset_animation, font=("Arial", 10)
    )
    reset_btn.pack(side=tk.LEFT, padx=5)

    self.root.bind("<space>", lambda event: self.toggle_pause())
    self.root.bind("<r>", lambda event: self.reset_animation())

    # Параметры анимации
    self.t = 0.0
    self.animate()

  def toggle_pause(self):
    self.is_paused = not self.is_paused

  def reset_animation(self):
    self.t = 0.0

  def animate(self):
    if not self.is_paused:
      self.canvas.delete("all")
      
      center_x, center_y = 350, 250
      base_radius = 120
      num_points = 200

      points = []
      # Параметрическая формула перехода окружности в треугольник с использованием полярных координат
      for i in range(num_points):
        theta = 2 * math.pi * i / num_points
        
        # Модуляция радиуса через косинус для создания формы треугольника
        # Коэффициент трансформации меняется плавно со временем благодаря синусу
        deformation = 0.25 * math.sin(self.t) * math.cos(3 * theta)
        r = base_radius * (1 + deformation)

        x = center_x + r * math.cos(theta)
        y = center_y + r * math.sin(theta)
        points.append((x, y))

      # Рисуем сглаженный контур фигуры
      flat_points = [coord for pt in points for coord in pt]
      self.canvas.create_polygon(
          flat_points, outline="black", fill="white", width=3, smooth=True
      )

      # Подпись статуса
      status = "Пауза" if self.is_paused else "Воспроизведение"
      self.canvas.create_text(
          60, 20, text=f"Статус: {status}", font=("Arial", 10), fill="black"
      )

      # Увеличиваем шаг времени для плавности
      self.t += 0.05

    # Обновление кадра каждые 30 миллисекунд
    self.root.after(30, self.animate)


if __name__ == "__main__":
  root = tk.Tk()
  app = CircleAnimationApp(root)
  root.mainloop()