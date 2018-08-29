#!/bin/env python

from motools import Vector

vec1 = Vector([1,2,3])
vec2 = Vector([1,2,3])
vec3 = Vector([3,2,1])

print('Vector Addition')
vec1 = Vector([8.218,-9.341])
vec2 = Vector([-1.129,2.111])
new_vec = vec1 + vec2
print('{} + {}'.format(vec1, vec2))
print('New Vector: {}'.format(new_vec))

print('Vector Subtraction')
vec1 = Vector([7.119,8.215])
vec2 = Vector([-8.223,0.878])
new_vec = vec1 - vec2
print('{} - {}'.format(vec1, vec2))
print('New Vector: {}'.format(new_vec))

print('Vector Scalar Multiply')
vec1 = Vector([1.671,-1.012,-0.318])
scalar = 7.41
new_vec = vec1.scale(scalar)
print('{} * {}'.format(scalar, vec1))
print('New Vector: {}'.format(new_vec))

