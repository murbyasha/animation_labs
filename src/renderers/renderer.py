class Renderer:

  def __init__(self, canvas):
    self.canvas = canvas

  def clear(self):
    self.canvas.delete("all")

  def draw_lines(self, lines_data):
    for line in lines_data:
      x1, y1, x2, y2, width = line
      self.canvas.create_line(x1, y1, x2, y2, fill="white", width=width)

  def draw_polygon(self, points):
    flat_points = [coord for pt in points for coord in pt]
    self.canvas.create_polygon(
        flat_points, outline="black", fill="white", width=3, smooth=True
    )