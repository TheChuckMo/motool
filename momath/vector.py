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
            raise ValueError('The coordinates must not be empty')

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
        """vector addition

        addition = sum the corresponding coordinates in the vectors
        """
        return Vector([x+y for x, y in zip(self.coordinates, v.coordinates)])

    def __sub__(self, v):
        """vector subtraction"""
        return Vector([x-y for x, y in zip(self.coordinates, v.coordinates)])

    def __mul__(self, v):
        """multiply each coordinate with the corresponding return the list"""
        return [x*y for x, y in zip(self.coordinates, v.coordinates)]

    def dot(self, v):
        """Inner/Dot product

        dot product = The sum of (the list of ints from multiply coordinates in each position)
        """
        return sum(self * v)

    def inner_angle(self, v):
        """inner angle

        inner angle = the dot product of vectors over the magnitude of vectors multiplied

        returns tuple of (acos, degrees)
        """
        n = acos(self.dot(v)/(self.magnitude*v.magnitude))
        d = degrees(n)
        return tuple([n, d])

    @property
    def magnitude(self):
        """size or distance of vector


        magnitude = The square root of (the sum of all (squared coordinates)) in the vector
        """
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


