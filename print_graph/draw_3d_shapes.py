import numpy as np


class Shape(object):
    def __init__(self, x1, x2, y1, y2, z1, z2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._z1 = z1
        self._z2 = z2


class Cube(Shape):
    def top_face(self):
        return [
            # good
            np.array([[self._x1, self._y2, self._z1],
                      [self._x1, self._y2, self._z2],
                      [self._x2, self._y2, self._z1]]),
            np.array([[self._x1, self._y2, self._z2],
                      [self._x2, self._y2, self._z2],
                      [self._x2, self._y2, self._z1]])
        ]

    def bottom_face(self):
        return [
            # good
            np.array([[self._x1, self._y1, self._z1],
                      [self._x2, self._y1, self._z2],
                      [self._x1, self._y1, self._z2]]),
            np.array([[self._x2, self._y1, self._z2],
                      [self._x1, self._y1, self._z1],
                      [self._x2, self._y1, self._z1]])
        ]

    def back_left_face(self):
        return [
            # good
            np.array([[self._x1, self._y1, self._z2],
                      [self._x2, self._y2, self._z2],
                      [self._x1, self._y2, self._z2]]),
            np.array([[self._x2, self._y2, self._z2],
                      [self._x1, self._y1, self._z2],
                      [self._x2, self._y1, self._z2]])
        ]

    def back_right_face(self):
        return [
            # good
            np.array([[self._x2, self._y2, self._z2],
                      [self._x2, self._y1, self._z2],
                      [self._x2, self._y2, self._z1]]),
            np.array([[self._x2, self._y1, self._z2],
                      [self._x2, self._y1, self._z1],
                      [self._x2, self._y2, self._z1]])
        ]

    def front_left_face(self):
        return [
            # good
            np.array([[self._x1, self._y1, self._z2],
                      [self._x1, self._y2, self._z2],
                      [self._x1, self._y1, self._z1]]),
            np.array([[self._x1, self._y1, self._z1],
                      [self._x1, self._y2, self._z2],
                      [self._x1, self._y2, self._z1]])
        ]

    def front_right_face(self):
        return [
            # good
            np.array([[self._x1, self._y1, self._z1],
                      [self._x1, self._y2, self._z1],
                      [self._x2, self._y2, self._z1]]),
            np.array([[self._x2, self._y2, self._z1],
                      [self._x2, self._y1, self._z1],
                      [self._x1, self._y1, self._z1]])
        ]

    def draw(self):
        return


class Pyramid(Shape):
    def __init__(self, *args):
        super(Pyramid, self).__init__(*args)
        if self._y1 > self._y2:
            self._y1, self._y2 = self._y2, self._y1
            self._x3 = self._x1
        else:
            self._x3 = self._x2

    def bottom(self):
        return [
            # good
            np.array([[self._x1, self._y1, self._z1],
                      [self._x2, self._y1, self._z1],
                      [self._x1, self._y1, self._z2]]),
            np.array([[self._x2, self._y1, self._z1],
                      [self._x2, self._y1, self._z2],
                      [self._x1, self._y1, self._z2]])
        ]

    def front_face(self):
        return [
            # good
            np.array([[self._x1, self._y1, self._z1],
                      [self._x3, self._y2, self._z1],
                      [self._x2, self._y1, self._z1]])
        ]

    def back_face(self):
        return [
            # good
            np.array([[self._x1, self._y1, self._z2],
                      [self._x2, self._y1, self._z2],
                      [self._x3, self._y2, self._z2]])
        ]

    def left_side(self):
        return [
            # good
            np.array([[self._x1, self._y1, self._z1],
                      [self._x1, self._y1, self._z2],
                      [self._x3, self._y2, self._z2]]),
            np.array([[self._x3, self._y2, self._z2],
                      [self._x3, self._y2, self._z1],
                      [self._x1, self._y1, self._z1]])
        ]

    def right_side(self):
        return [
            # good
            np.array([[self._x2, self._y1, self._z2],
                      [self._x2, self._y1, self._z1],
                      [self._x3, self._y2, self._z2]]),
            np.array([[self._x3, self._y2, self._z2],
                      [self._x2, self._y1, self._z1],
                      [self._x3, self._y2, self._z1]])
        ]


class Pyramid2(Shape):
    def __init__(self, x1, x2, y1, y2, yf1, yf2, z1, z2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._yf1 = yf1
        self._yf2 = yf2
        self._z1 = z1
        self._z2 = z2

        if self._y1 > self._y2:
            self._y1, self._y2 = self._y2, self._y1
            self._x3 = self._x1
        else:
            self._x3 = self._x2

        if self._yf1 > self._yf2:
            self._yf1, self._yf2 = self._yf2, self._yf1
            self._xf3 = self._x1
        else:
            self._xf3 = self._x2

    def bottom(self):
        return [
            # good
            np.array([[self._x1, self._y1, self._z1],
                      [self._x2, self._y1, self._z1],
                      [self._x1, self._yf1, self._z2]]),
            np.array([[self._x2, self._y1, self._z1],
                      [self._x2, self._yf1, self._z2],
                      [self._x1, self._yf1, self._z2]])
        ]

    def front_face(self):
        return [
            # good
            np.array([[self._x1, self._y1, self._z1],
                      [self._x3, self._y2, self._z1],
                      [self._x2, self._y1, self._z1]])
        ]

    def back_face(self):
        return [
            # good
            np.array([[self._x1, self._yf1, self._z2],
                      [self._x2, self._yf1, self._z2],
                      [self._x3, self._yf2, self._z2]])
        ]

    def left_side(self):
        return [
            # bad
            np.array([[self._x1, self._y1, self._z1],
                      [self._x1, self._yf1, self._z2],
                      [self._x3, self._y2, self._z1]]),
            np.array([[self._x3, self._y2, self._z1],
                      [self._x3, self._yf2, self._z2],
                      [self._x1, self._yf1, self._z2]])
            # np.array([[self._x1, self._y1, self._z1],
            #           [self._x1, self._yf1, self._z2],
            #           [self._x3, self._yf2, self._z2]]),
            # np.array([[self._x3, self._yf2, self._z2],
            #           [self._x3, self._y2, self._z1],
            #           [self._x1, self._y1, self._z1]])
        ]

    def right_side(self):
        return [
            # good
            np.array([[self._x2, self._yf1, self._z2],
                      [self._x2, self._y1, self._z1],
                      [self._x3, self._yf2, self._z2]]),
            np.array([[self._x3, self._yf2, self._z2],
                      [self._x2, self._y1, self._z1],
                      [self._x3, self._y2, self._z1]])
        ]


def join_points(x1, x2, y11, y12, y21, y22, z1, z2):
    return [
        np.array([[x1, y11, z1],
                  [x2, y12, z1],
                  [x1, y21, z2]]),
        np.array([[x2, y12, z1],
                  [x2, y22, z2],
                  [x1, y21, z2]])
    ]
