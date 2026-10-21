import tkinter as tk
from src.models.animation_model import AnimationModel
from src.models.fractal_model import FractalModel
from src.renderers.renderer import Renderer
from src.widgets.controls import ControlsWidget


class MainApp:

  def __init__(self, root):
    self.root = root
    self.root.title("Проектный практикум: Лабораторные работы")
    self.root.geometry("800x750")

    # Переключатель режимов лаб
    mode_frame = tk.Frame(root)
    mode_frame.pack(pady=5)
    tk.Button(
        mode_frame,
        text="Лаба 1: Фрактал",
        command=lambda: self.set_mode("fractal"),
        font=("Arial", 10, "bold"),
    ).pack(side=tk.LEFT, padx=5)
    tk.Button(
        mode_frame,
        text="Лаба 2: Анимация круга",
        command=lambda: self.set_mode("animation"),
        font=("Arial", 10, "bold"),
    ).pack(side=tk.LEFT, padx=5)

    # Холст
    self.canvas = tk.Canvas(root, width=700, height=500, bg="#222222")
    self.canvas.pack(pady=10)
    self.renderer = Renderer(self.canvas)

    # Элементы управления
    self.controls = ControlsWidget(
        root, self.on_slider_update, self.toggle_pause, self.reset_app
    )

    # Горячие клавиши
    self.root.bind("<space>", lambda e: self.toggle_pause())
    self.root.bind("<r>", lambda e: self.reset_app())

    self.mode = "fractal"
    self.t = 0.0
    self.is_paused = False

    self.run_current_mode()

  def set_mode(self, mode):
    self.mode = mode
    if mode == "fractal":
      self.canvas.config(bg="#222222")
    else:
      self.canvas.config(bg="#e0e0e0")
    self.reset_app()

  def on_slider_update(self, val):
    if self.mode == "fractal":
      self.redraw_fractal()

  def toggle_pause(self):
    self.is_paused = not self.is_paused

  def reset_app(self):
    self.t = 0.0
    self.is_paused = False
    if self.mode == "fractal":
      self.controls.set_angle(30)
      self.redraw_fractal()

  def redraw_fractal(self):
    self.renderer.clear()
    angle = self.controls.get_angle()
    lines = FractalModel.calculate_branches(350, 480, 120, 0, 9, angle)
    self.renderer.draw_lines(lines)

  def run_current_mode(self):
    if self.mode == "fractal":
      self.redraw_fractal()
    elif self.mode == "animation" and not self.is_paused:
      self.renderer.clear()
      points = AnimationModel.calculate_circle_to_triangle_points(
          350, 250, 120, self.t
      )
      self.renderer.draw_polygon(points)
      self.t += 0.05

    # Цикл обновления для анимации
    self.root.after(30, self.run_current_mode)