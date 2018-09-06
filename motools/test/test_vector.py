'''TestVector()'''

import pytest

from motools import Vector


class TestVector(object):
    '''Vector() Tests'''

    vector2a = Vector((4, 5))
    vector2b = Vector((7, 9))
    vector2c = Vector((4, 5))
    scalar2 = 6.78

    vector3a = Vector((6, 3, 5))
    vector3b = Vector((3, 1, 2))
    vector3c = Vector((6, 3, 5))
    scalar3 = 7.41

    def test_equality(self):
        '''Test vector equality'''

        assert self.vector2a == self.vector2c
        assert self.vector3a == self.vector3c

        assert self.vector2a != self.vector2b
        assert self.vector3a != self.vector3b

    def test_addition(self):
        '''Test vector addition'''

        addvector1 = self.vector2a + self.vector2b
        assert addvector1 == Vector([11, 14])

        addvector2 = self.vector2a + self.vector2b + self.vector2c
        assert addvector2 == Vector([15, 19])

        addvector3 = self.vector3a + self.vector3b
        assert addvector3 == Vector([9, 4, 7])

        addvector4 = self.vector3a + self.vector3b + self.vector3c
        assert addvector4 == Vector([15, 7, 12])

    def test_subtraction(self):
        '''Test vector subtraction'''

        subvector1 = self.vector2a - self.vector2b
        assert subvector1 == Vector([-3, -4])

        subvector2 = self.vector2a - self.vector2b - self.vector2c
        assert subvector2 == Vector([-7, -9])

        subvector3 = self.vector3a - self.vector3b
        assert subvector3 == Vector([3, 2, 3])

        subvector4 = self.vector3a - self.vector3b - self.vector3c
        assert subvector4 == Vector([-3, -1, -2])

    def test_scalar_multiplication(self):
        '''Test vector multiplication'''

        mulvector1 = self.vector2a * self.vector2b
        assert mulvector1 == Vector([28, 45])

        mulvector2 = self.vector2a * self.vector2b * self.vector2c
        assert mulvector2 == Vector([112, 225])

        mulvector3 = self.vector3a * self.vector3b
        assert mulvector3 == Vector([18, 3, 10])

        mulvector4 = self.vector3a * self.vector3b * self.vector3c
        assert mulvector4 == Vector([108, 9, 50])
