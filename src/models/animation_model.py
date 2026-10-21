import math


class AnimationModel:

  @staticmethod
  def calculate_circle_to_triangle_points(
      center_x, center_y, base_radius, t, num_points=200
  ):
    points = []
    for i in range(num_points):
      theta = 2 * math.pi * i / num_points
      # Формула деформации через полярные координаты
      deformation = 0.25 * math.sin(t) * math.cos(3 * theta)
      r = base_radius * (1 + deformation)

      x = center_x + r * math.cos(theta)
      y = center_y + r * math.sin(theta)
      points.append((x, y))
    return points