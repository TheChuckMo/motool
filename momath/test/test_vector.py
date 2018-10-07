"""TestVector()"""

import pytest

from momath import Vector


@pytest.fixture
def values():
    '''values dictionary'''

    _values = dict()

    _values['vector2a'] = Vector((4, 5))
    _values['vector2b'] = Vector((7, 9))
    _values['vector2c'] = Vector((4, 5))
    _values['scalar2'] = 6.78

    _values['vector3a'] = Vector((6, 3, 5))
    _values['vector3b'] = Vector((3, 1, 2))
    _values['vector3c'] = Vector((6, 3, 5))
    _values['scalar3'] = 7.41

    _values['addvector1'] = Vector([11, 14])
    _values['addvector2'] = Vector([15, 19])
    _values['addvector3'] = Vector([9, 4, 7])
    _values['addvector4'] = Vector([15, 7, 12])

    _values['subvector1'] = Vector([-3, -4])
    _values['subvector2'] = Vector([-7, -9])
    _values['subvector3'] = Vector([3, 2, 3])
    _values['subvector4'] = Vector([-3, -1, -2])

    _values['mulvector1'] = Vector([28, 45])
    _values['mulvector2'] = Vector([112, 225])
    _values['mulvector3'] = Vector([18, 3, 10])
    _values['mulvector4'] = Vector([108, 9, 50])

    _values['incvector1'] = Vector([6, 7])
    _values['incvector2'] = Vector([9, 10])
    _values['incvector3'] = Vector([8, 5, 7])
    _values['incvector4'] = Vector([11, 8, 10])

    _values['decvector1'] = Vector([2, 3])
    _values['decvector2'] = Vector([-1, 0])
    _values['decvector3'] = Vector([4, 1, 3])
    _values['decvector4'] = Vector([1, -2, 0])

    return _values


class TestVector(object):
    '''Vector() Tests'''

    def test_equality(self, values):
        '''Test vector equality'''

        assert values.get('vector2a') == values.get('vector2c')
        assert values.get('vector3a') == values.get('vector3c')

        assert values.get('vector2a') != values.get('vector2b')
        assert values.get('vector3a') != values.get('vector3b')

    def test_addition(self, values):
        '''Test vector addition'''

        addvector1 = values.get('vector2a') + values.get('vector2b')
        assert addvector1 == values.get('addvector1')

        addvector2 = values.get('vector2a') + values.get('vector2b') + values.get('vector2c')
        assert addvector2 == values.get('addvector2')

        addvector3 = values.get('vector3a') + values.get('vector3b')
        assert addvector3 == values.get('addvector3')

        addvector4 = values.get('vector3a') + values.get('vector3b') + values.get('vector3c')
        assert addvector4 == values.get('addvector4')

    def test_subtraction(self, values):
        '''Test vector subtraction'''

        subvector1 = values.get('vector2a') - values.get('vector2b')
        assert subvector1 == values.get('subvector1')

        subvector2 = values.get('vector2a') - values.get('vector2b') - values.get('vector2c')
        assert subvector2 == values.get('subvector2')

        subvector3 = values.get('vector3a') - values.get('vector3b')
        assert subvector3 == values.get('subvector3')

        subvector4 = values.get('vector3a') - values.get('vector3b') - values.get('vector3c')
        assert subvector4 == values.get('subvector4')

    def test_scalar_multiplication(self, values):
        '''Test vector multiplication'''

        mulvector1 = values.get('vector2a') * values.get('vector2b')
        assert mulvector1 == values.get('mulvector1')

        mulvector2 = values.get('vector2a') * values.get('vector2b') * values.get('vector2c')
        assert mulvector2 == values.get('mulvector2')

        mulvector3 = values.get('vector3a') * values.get('vector3b')
        assert mulvector3 == values.get('mulvector3')

        mulvector4 = values.get('vector3a') * values.get('vector3b') * values.get('vector3c')
        assert mulvector4 == values.get('mulvector4')

    def test_increment(self, values):
        '''test increment vector by integar'''

        assert values.get('vector2a').increment(2) == values.get('incvector1')
        assert values.get('vector2a').increment(5) == values.get('incvector2')

        assert values.get('vector3a').increment(2) == values.get('incvector3')
        assert values.get('vector3a').increment(5) == values.get('incvector4')

    def test_decrement(self, values):
        '''test decrement vector by integar'''

        assert values.get('vector2a').decrement(2) == values.get('decvector1')
        assert values.get('vector2a').decrement(5) == values.get('decvector2')

        assert values.get('vector3a').decrement(2) == values.get('decvector3')
        assert values.get('vector3a').decrement(5) == values.get('decvector4')
