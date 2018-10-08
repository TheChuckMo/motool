#!/bin/env python

from momath import Vector

vector2a = Vector([4, 5])
vector2b = Vector([7, 9])
vector2c = Vector([4, 5])
scalar2 = 6.78

vector3a = Vector([6, 3, 5])
vector3b = Vector([3, 1, 2])
vector3c = Vector([6, 3, 5])
scalar3 = 7.41

print('Vector Addition')
add2vector = vector2a + vector2b
print(' :{} + {} = {}'.format(vector2a, vector2b, add2vector))
add3vector = vector3a + vector3b
print(' :{} + {} = {}'.format(vector3a, vector3b, add3vector))

print('Vector Subtraction')
sub2vector = vector2a - vector2b
print(' :{} - {} = {}'.format(vector2a, vector2b, sub2vector))
sub3vector = vector3a - vector3b
print(' :{} - {} = {}'.format(vector3a, vector3b, sub3vector))

print('Vector Scalar Multiplcation')
scale2vector = vector2c.scalar(scalar2)
print(' :{} * {} = {}'.format(scalar2, vector2c, scale2vector))
scale3vector = vector3c.scalar(scalar3)
print(' :{} * {} = {}'.format(scalar3, vector3c, scale3vector))

print('Vector Magnitude')
print(' :{} = {}'.format(vector2a, vector2a.magnitude))
print(' :{} = {}'.format(vector3a, vector3a.magnitude))

print('Vector Normalized')
print(' :{} = {}'.format(vector2b, vector2b.normalized))
print(' :{} = {}'.format(vector3b, vector3b.normalized))

print('Vector/Vector Angle')
print(' :({},{}) = {}'.format(vector2c, vector2a, vector2c.inner_angle(vector2a)))
