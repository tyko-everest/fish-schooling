""" Two-dimensional Vector class
Components default to zero unless otherwise specified on creation
"""
import math

class Vector2D:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __add__(self, v2):
        return Vector2D(self.x + v2.x, self.y + v2.y)

    def __sub__(self, v2):
        return Vector2D(self.x - v2.x, self.y - v2.y)

    def __mul__(self, t):
        return Vector2D(self.x * t, self.y * t)

    __rmul__ = __mul__

    def __truediv__(self, t):
        return Vector2D(self.x / t, self.y / t)

    def __floordiv__(self, t):
        return Vector2D(self.x // t, self.y // t)

    def __str__(self):
        return "[%s, %s]" % (self.x, self.y)

    def dot(self, v2):
        return self.x * v2.x + self.y * v2.y

    def magnitude(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def angle(self):
        return math.atan2(self.y, self.x)

    def cartesianDistance(self, v2):
        return ((v2.y - self.y) ** 2 + (v2.x - self.x) ** 2) ** 0.5

    # TODO handle magnitude of zero
    def angleBetween(self, v2):
        return math.acos(self.dot(v2) / (self.magnitude() * v2.magnitude()))


