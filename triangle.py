import point
from math import *

class Triangle:
    #Class for triangle with 3 points

    def __init__(self, p1, p2, p3):
        # Initialises variables
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def line(self):
        '''
        Finds the length of the line between two points
        Returns list with 3 float numb(p1-p2 len, p2-p3 len, p3-p1 len)
        '''
        len_lst = []
        len_lst.append(sqrt(pow(self.p2.x - self.p1.x, 2) + pow(self.p2.y - self.p1.y, 2)))
        len_lst.append(sqrt(pow(self.p3.x - self.p2.x, 2) + pow(self.p3.y - self.p2.y, 2)))
        len_lst.append(sqrt(pow(self.p1.x - self.p3.x, 2) + pow(self.p1.y - self.p3.y, 2)))
        return len_lst

    def is_triangle(self):
        '''
        takes a list of lengths and looks if the statement:
            "sum of lengths of two lines must be always bigger then the third one"
        is correct
        if correct: return True
        if not: return False
        '''
        lines = self.line()
        if lines[0] > lines[1] + lines[2] or lines[1] > lines[0] + lines[2] or lines[2] > lines[1] + lines[0]:
            return False
        else:
            return True

    def perimeter(self):
        '''
        takes a list of lengths
        returns sum of all elements in it: perimeter
        '''
        lines = self.line()
        return sum(lines)

    def area(self):
        '''
        finds area of the triangle and returns it as float
        Heron's formula
        '''
        lines = self.line()
        hp = (self.perimeter() / 2) #hp - half perimeter
        area = sqrt(hp * (hp - lines[0]) * (hp - lines[1]) * (hp - lines[2]))
        return area

