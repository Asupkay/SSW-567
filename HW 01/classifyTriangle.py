import math
from numbers import Number

def classifyTriangle(a, b, c):
    if(not isinstance(a, Number) or not isinstance(b, Number) or not isinstance(c, Number) or a + b <= c or a + c <= b or b + c <= a):
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
        assert classifyTriangle(6, 8, 10) == 'Right'
        assert classifyTriangle(24, 26, 10) == 'Right'

    def test_Equilateral(self):
        assert classifyTriangle(1,1,1) == 'Equilateral'
        assert classifyTriangle(100,100,100) == 'Equilateral'
        assert classifyTriangle(0,0,0) != 'Equilateral'

    def test_Isoceles(self):
        assert classifyTriangle(10,10,10) != 'Isoceles'
        assert classifyTriangle(5, 5, 3) == 'Isoceles'

    def test_Scalene(self):
        assert classifyTriangle(13,9,14) == 'Scalene'
        assert classifyTriangle(7.7, 5, 9) == 'Scalene'

    def test_NotATriangle(self):
        assert classifyTriangle(False, 1, 1) == 'NotATriangle'
        assert classifyTriangle(100, 1, 1) == 'NotATriangle'
        assert classifyTriangle(-1, -1, -1) == 'NotATriangle'
        assert classifyTriangle(0, 0, 0) == 'NotATriangle'

runClassifyTriangle(3,4,5)
runClassifyTriangle(6, 8, 10)
runClassifyTriangle(24, 26, 10)
runClassifyTriangle(1,1,1)
runClassifyTriangle(100,100,100)
runClassifyTriangle(0,0,0)
runClassifyTriangle(10,10,10)
runClassifyTriangle(5, 5, 3)
runClassifyTriangle(13,9,14)
runClassifyTriangle(7.7, 5, 9)
runClassifyTriangle(100, 1, 1)
runClassifyTriangle(-1, -1, -1)
runClassifyTriangle(0, 0, 0)

