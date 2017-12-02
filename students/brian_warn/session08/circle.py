#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python
# circle.py
from math import pi


class Circle:

    def __init__(self, radius):
        self.radius = radius
        # self.diameter = radius * 2 <-- moved to its own property

    @property
    def diameter(self):
        return self.radius * 2


# now change the diameter and have the radius change

    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2

# now calculate the area of the circle.

    @property
    def area(self):
        return pi * self.radius**2

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __str__(self):
        return "Circle with radius: {}".format(self.radius)

    def __add__(self, c):
        a = (pi * self.radius**2) + (pi * c.radius**2)
        return a

    def __gt__(self, other):
        return (pi * self.radius**2) > (pi * other.radius**2)

    def __lt__(self, other):
        return (pi * self.radius**2) < (pi * other.radius**2)

    def __eq__(self, other):
        return (pi * self.radius**2) == (pi * other.radius**2)
