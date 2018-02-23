'''
module for testing class triangle and all it's methods
'''
from triangle import *

triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
print('Is it possible to make triangle with given points?: ', triangle.is_triangle())
print('Triangle\'s perimeter: ', triangle.perimeter())
print('Triangle\'s area: ', triangle.area())