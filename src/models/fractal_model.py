import math


class FractalModel:

  @staticmethod
  def calculate_branches(x, y, length, angle, depth, branch_angle):
    if depth == 0 or length < 2:
      return []

    rad = math.radians(angle)
    x_end = x + length * math.sin(rad)
    y_end = y - length * math.cos(rad)

    current_line = (x, y, x_end, y_end, max(1, depth // 2))

    # Рекурсивно вычисляем левую и правую ветки
    left_branches = FractalModel.calculate_branches(
        x_end, y_end, length * 0.7, angle + branch_angle, depth - 1, branch_angle
    )
    right_branches = FractalModel.calculate_branches(
        x_end, y_end, length * 0.7, angle - branch_angle, depth - 1, branch_angle
    )

    return [current_line] + left_branches + right_branches