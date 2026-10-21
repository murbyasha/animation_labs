import tkinter as tk


class ControlsWidget:

  def __init__(self, parent, on_slider_change, on_pause, on_reset):
    self.frame = tk.Frame(parent)
    self.frame.pack(pady=5)

    # Слайдер для угла фрактала
    tk.Label(self.frame, text="Угол ветвления:", font=("Arial", 11)).pack(
        side=tk.LEFT, padx=5
    )
    self.angle_slider = tk.Scale(
        self.frame,
        from_=0,
        to=90,
        orient=tk.HORIZONTAL,
        length=200,
        command=on_slider_change,
    )
    self.angle_slider.set(30)
    self.angle_slider.pack(side=tk.LEFT, padx=5)

    # Кнопки паузы и сброса
    self.pause_btn = tk.Button(
        self.frame, text="Пауза (Space)", command=on_pause, font=("Arial", 10)
    )
    self.pause_btn.pack(side=tk.LEFT, padx=5)

    self.reset_btn = tk.Button(
        self.frame, text="Сброс (R)", command=on_reset, font=("Arial", 10)
    )
    self.reset_btn.pack(side=tk.LEFT, padx=5)

  def get_angle(self):
    return self.angle_slider.get()

  def set_angle(self, val):
    self.angle_slider.set(val)