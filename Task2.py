"""42. На плоскости дано n точек. Определите коэффициенты прямой y=kx+b, проходящей через первую и одну из
оставшихся точек так, чтобы все n точек лежали по одну сторону от этой прямой, и, быть может, на самой прямой."""

import math


def rotate(left, mid, right):
    return (mid[0]-left[0])*(right[1]-mid[1])-(mid[1]-left[1])*(right[0]-mid[0])

def create_polygon(points):
    print(points)
    minpoint = min(points, key=lambda x: x[1])
    points.remove(minpoint)

    print(minpoint)
    print(points)
    points.sort(
        key=lambda x: ((-1) * (x[0] - minpoint[0]) + (0) * (x[1] - minpoint[1])) / math.sqrt(
            math.pow((x[0] - minpoint[0]), 2) + math.pow((x[1] - minpoint[1]), 2)))
    print(points)
    points.insert(0,minpoint)

    res = [points[0], points[1]]
    for i in range(2,len(points)):
        while rotate(res[-2], res[-1], points[i]) < 0:
            del res[-1]
        res.append(points[i])
    print(res)
    return res

def solve_linear_equations_system(p1, p2):
    determinant = p1[0] - p2[0]
    x =  (p1[1] - p2[1])/determinant
    y = (p1[0]*p2[1] - p2[0]*p1[1])/determinant
    return (x,y)

def solve_task(points, p):
    points = create_polygon(points)
    index = points.index(p)
    return (solve_linear_equations_system(points[index], points[index-1]), solve_linear_equations_system(points[index], points[index+1]))


points = [(1, 2), (2,1),(2,3),(2, 4), (3,4),(4,2),(5,3),(5, 8),(5,5), (4, 8), (8, 3),(6,4), (6, 1)]

print(solve_task(points,(2,1)))