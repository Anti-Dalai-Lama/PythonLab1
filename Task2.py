"""42. На плоскости дано n точек. Определите коэффициенты прямой y=kx+b, проходящей через первую и одну из
оставшихся точек так, чтобы все n точек лежали по одну сторону от этой прямой, и, быть может, на самой прямой."""

import math

class VectorOperations(object):
    @staticmethod
    def rotate(left, mid, right):
        return (mid[0]-left[0])*(right[1]-mid[1])-(mid[1]-left[1])*(right[0]-mid[0])

class Polygon(object):
    def __init__(self,points):
        minpoint = min(points, key=lambda x: x[1])
        points.remove(minpoint)
        points.sort(
            key=lambda x: ((-1) * (x[0] - minpoint[0]) + (0) * (x[1] - minpoint[1])) / math.sqrt(
                math.pow((x[0] - minpoint[0]), 2) + math.pow((x[1] - minpoint[1]), 2)))
        points.insert(0,minpoint)

        res = [points[0], points[1]]
        for i in range(2,len(points)):
            while VectorOperations.rotate(res[-2], res[-1], points[i]) < 0:
                del res[-1]
            res.append(points[i])
        self.points = res

class LinearSystemOfEquations:
    def __init__(self, index1, index2):
        self.index1 = index1
        self.index2 = index2

    def solve(self):
        determinant = self.index1[0] - self.index2[0]
        k = (self.index1[1] - self.index2[1]) / determinant
        b = (self.index1[0] * self.index2[1] - self.index2[0] * self.index1[1]) / determinant
        return (k, b)

def solve_task(points, p):
    polygon = Polygon(points)
    index = polygon.points.index(p)
    return [LinearSystemOfEquations(points[index], points[index-1]).solve(), LinearSystemOfEquations(points[index], points[index+1]).solve()]

points = [(1, 2), (2,1),(2,3),(2, 4), (3,4),(4,2),(5,3),(5, 8),(5,5), (4, 8), (8, 3),(6,4), (6, 1)]
print(solve_task(points,(2,1)))