import numpy as np


def draw_square(x1, x2, y1, y2):
    return [
        np.array([[x1, y1, 0],
                  [x1, y2, 0],
                  [x2, y1, 0]]),
        np.array([[x1, y2, 0],
                  [x2, y2, 0],
                  [x2, y1, 0]])
    ]


def draw_bottom_left_triangle(x1, x2, y1, y2):
    return [
        np.array([[x1, y2, 0],
                  [x1, y1, 0],
                  [x2, y1, 0]])
    ]


def draw_bottom_right_triangle(x1, x2, y1, y2):
    return [
        np.array([[x1, y1, 0],
                  [x2, y1, 0],
                  [x2, y2, 0]])
    ]


def draw_top_left_triangle(x1, x2, y1, y2):
    raise NotImplementedError("Not implemented")


def draw_top_right_triangle(x1, x2, y1, y2):
    raise NotImplementedError("Not implemented")


def draw_triangle(x1, x2, y1, y2):
    if x2 > x1:
        if y2 > y1:
            return draw_bottom_right_triangle(x1, x2, y1, y2)
        else:
            return draw_bottom_left_triangle(x1, x2, y2, y1)
    else:
        if y2 > y1:
            return draw_top_right_triangle(x1, x2, y1, y2)
        else:
            return draw_top_left_triangle(x1, x2, y2, y1)
