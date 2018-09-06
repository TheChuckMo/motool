'''Vector math module'''


class Vector(object):
    '''Vector object'''

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
        '''vector equality'''
        return self.coordinates == v.coordinates

    def __add__(self, v):
        '''vector addition'''
        return Vector([x+y for x, y in zip(self.coordinates, v.coordinates)])

    def __sub__(self, v):
        '''vector subtraction'''
        return Vector([x-y for x, y in zip(self.coordinates, v.coordinates)])

    def __mul__(self, v):
        '''vector multiplication'''
        return Vector([x*y for x, y in zip(self.coordinates, v.coordinates)])

    def increment(self, n=1):
        '''add integar to each coordinate'''
        return Vector([x+n for x in self.coordinates])

    def decrement(self, n=1):
        '''subtract integar from each coordinate'''
        return Vector([x-n for x in self.coordinates])

    def scalar(self, n):
        '''multiply each coordinate by integar'''
        return Vector([x*n for x in self.coordinates])
