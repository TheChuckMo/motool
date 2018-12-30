"""TestVector()"""

from momath import Vector


class TestVector(object):
    '''Vector() Tests'''

    # def test_normalized(self, values):
    #     """"""
    #     assert values.get('vector2a').normalized == ''

    def test_equality(self, vector_values):
        '''Test vector equality'''

        v2e1 = Vector(vector_values.get('vectors').get('v2a'))
        v2e2 = Vector(vector_values.get('vectors').get('v2a'))
        v2e3 = Vector(vector_values.get('vectors').get('v2b'))

        v3e1 = Vector(vector_values.get('vectors').get('v3a'))
        v3e2 = Vector(vector_values.get('vectors').get('v3a'))
        v3e3 = Vector(vector_values.get('vectors').get('v3b'))

        assert v2e1 == v2e2
        assert v3e1 == v3e2

        assert v2e1 != v2e3
        assert v3e1 != v3e3

    def test_addition(self, vector_values):
        """Test vector addition"""

        v2e1 = Vector(vector_values.get('vectors').get('v2a'))
        v2e2 = Vector(vector_values.get('vectors').get('v2b'))

        v3e1 = Vector(vector_values.get('vectors').get('v3a'))
        v3e2 = Vector(vector_values.get('vectors').get('v3b'))

        assert (v2e1 + v2e2) == Vector(vector_values.get('answers').get('v2').get('addition'))

        assert (v3e1 + v3e2) == Vector(vector_values.get('answers').get('v3').get('addition'))

    def test_subtraction(self, vector_values):
        """test vector subtraction"""

        v2e1 = Vector(vector_values.get('vectors').get('v2a'))
        v2e2 = Vector(vector_values.get('vectors').get('v2b'))

        v3e1 = Vector(vector_values.get('vectors').get('v3a'))
        v3e2 = Vector(vector_values.get('vectors').get('v3b'))

        assert (v2e1 - v2e2) == Vector(vector_values.get('answers').get('v2').get('subtraction'))

        assert (v3e1 - v3e2) == Vector(vector_values.get('answers').get('v3').get('subtraction'))

    def test_magnitude(self, vector_values):
        """test magnitude"""

        v2e1 = Vector(vector_values.get('vectors').get('v2a'))

        v3e1 = Vector(vector_values.get('vectors').get('v3a'))

        assert v2e1.magnitude == vector_values.get('answers').get('v2').get('magnitude')

        assert v3e1.magnitude == vector_values.get('answers').get('v3').get('magnitude')

    def test_normalized(self, vector_values):
        """test magnitude"""

        v2e1 = Vector(vector_values.get('vectors').get('v2a'))

        v3e1 = Vector(vector_values.get('vectors').get('v3a'))

        assert v2e1.normalized == Vector(vector_values.get('answers').get('v2').get('normalized'))

        assert v3e1.normalized == Vector(vector_values.get('answers').get('v3').get('normalized'))

    def test_dot(self, vector_values):

        v2e1 = Vector(vector_values.get('vectors').get('v2a'))
        v2e2 = Vector(vector_values.get('vectors').get('v2b'))

        v3e1 = Vector(vector_values.get('vectors').get('v3a'))
        v3e2 = Vector(vector_values.get('vectors').get('v3b'))

        assert v2e1.dot(v2e2) == vector_values.get('answers').get('v2').get('dot')
        assert v3e1.dot(v3e2) == vector_values.get('answers').get('v3').get('dot')

    def test_inner_angle(self, vector_values):

        v2e1 = Vector(vector_values.get('vectors').get('v2a'))
        v2e2 = Vector(vector_values.get('vectors').get('v2b'))

        v3e1 = Vector(vector_values.get('vectors').get('v3a'))
        v3e2 = Vector(vector_values.get('vectors').get('v3b'))

        assert v2e1.inner_angle(v2e2)[1] == vector_values.get('answers').get('v2').get('inner_angle')
        assert v3e1.inner_angle(v3e2)[1] == vector_values.get('answers').get('v3').get('inner_angle')

    def test_scalar(self, vector_values):
        """test magnitude"""

        v2e1 = Vector(vector_values.get('vectors').get('v2a'))

        v3e1 = Vector(vector_values.get('vectors').get('v3a'))

        scalar = vector_values.get('scalar')

        assert v2e1.scalar(scalar) == Vector(vector_values.get('answers').get('v2').get('scalar'))

        assert v3e1.scalar(scalar) == Vector(vector_values.get('answers').get('v3').get('scalar'))
