#!/bin/env python

from motools import Vector

vec1 = Vector([1,2,3])
vec2 = Vector([1,2,3])
vec3 = Vector([3,2,1])

print('Vector 1: {}'.format(vec1))
print('Vector 2: {}'.format(vec2))
print('Vector 3: {}'.format(vec3))

print('expect true')
print(vec1 == vec2)
print('expect false')
print(vec1 == vec3)

print('expect true')
print(vec2 == vec1)
print('expect false')
print(vec2 == vec3)

print('expect false')
print(vec3 == vec1)
print('expect false')
print(vec3 == vec2)

print('Vector Addition')
print(vec1 + vec2)

print('Vector Subtraction')
print(vec3 - vec1)

print('Vector Multiplication')
print(vec3 * vec3)

