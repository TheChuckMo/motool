# based on code provided by Udacity while taking Linear Algebra course


class Vector(object):
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


    def __str__(self):
        return '{}'.format(str(self.coordinates))


    def __eq__(self, v):
        return self.coordinates == v.coordinates


    def __add__(self, v):
        res = [x+y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(res)


    def __sub__(self, v):
        res = [x-y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(res)


    def __mul__(self, v):
        res = [x*y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(res)


    def addint(self, n):
        res = [x+n for x in self.coordinates]
        return Vector(res)

    def subint(self, n):
        res = [x-n for x in self.coordinates]
        return Vector(res)

    def scale(self, n):
        res = [x*n for x in self.coordinates]
        return Vector(res)


