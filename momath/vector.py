"""Vector math module"""
from math import sqrt, pow, acos, degrees


class Vector(object):
    """Vector object"""

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __repr__(self):
        return 'Vector({})'.format(list(self.coordinates))

    def __str__(self):
        return '{}'.format(list(self.coordinates))

    def __eq__(self, v):
        """vector equality"""
        return self.coordinates == v.coordinates

    def __add__(self, v):
        """vector addition"""
        return Vector([x+y for x, y in zip(self.coordinates, v.coordinates)])

    def __sub__(self, v):
        """vector subtraction"""
        return Vector([x-y for x, y in zip(self.coordinates, v.coordinates)])

    def inner_product(self, v):
        """Inner/Dot product"""
        return sum([x*y for x, y in zip(self.coordinates, v.coordinates)])

    def inner_angle(self, v):
        """inner angle"""
        n = acos(self.inner_product(v)/(self.magnitude*v.magnitude))
        d = degrees(n)
        return tuple([n, d])

    @property
    def magnitude(self):
        """size or distance of vector"""
        n = sum([pow(x, 2) for x in self.coordinates])
        return sqrt(n)

    @property
    def normalized(self):
        """normalized vector"""
        try:
            return self.scalar(1/self.magnitude)

        except ZeroDivisionError:
            raise Exception('Vector is zero')

    def scalar(self, n):
        """multiply each coordinate by integar"""
        return Vector([x*n for x in self.coordinates])


