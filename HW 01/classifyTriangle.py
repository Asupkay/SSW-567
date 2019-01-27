import math
import pytest

def classifyTriangle(a, b, c):
    if(a + b <= c or a + c <= b or b + c <= a):
        return 'NotATriangle'
    if(a == b and a == c):
        return 'Equilateral'
    if((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
        return 'Isoceles'

    aPow = math.pow(a, 2)
    bPow = math.pow(b, 2)
    cPow = math.pow(c, 2)
    if(aPow + bPow == cPow or aPow + cPow == bPow or bPow + cPow == aPow):
        return 'Right'
    if(a != b and b != c):
        return 'Scalene'


def runClassifyTriangle(a, b, c):
    print('classifyTriangle(' + str(a) + ',' + str(b) + ',' + str(c) + ')=' + classifyTriangle(a,b,c)) 

class TestTriangles(object):
    def test_Right(self):
        assert classifyTriangle(3,4,5) == 'Right'

    def test_Equilateral(self):
        assert classifyTriangle(1,1,1) == 'Equilateral'

    def test_Isoceles(self):
        assert classifyTriangle(10,10,10) != 'Isoceles'
        assert classifyTriangle(5, 5, 3) == 'Isoceles'

    def test_Scalene(self):
        assert classifyTriangle(13,9,14) == 'Scalene'

    def test_NotATriangle(self):
        assert classifyTriangle(100, 1, 1) == 'NotATriangle'
