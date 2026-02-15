import sys
from typing import Tuple

class Point2D:
    def __init__(self, x0:int, y0:int):
        self._rx = x0
        self._ry = y0

    def move(self, dx:int, dy:int) -> Tuple[int, int]:
        return (self._rx + dx, self._ry + dy)
    
    def __str__(self)-> tuple:
        return f"({self._rx}, {self._ry})"
    
    def __eq__(self, other):
        return (self._rx, self._ry) == (other._rx, other._ry) 
    
if __name__ == '__main__':

    x = int(sys.argv[1])
    y = int(sys.argv[2])

    point = Point2D(x,y)
    point1 = Point2D(x, y)

    print(point.move(2,3))
    print(point)
    print(point == point1)
    print(point is point1)