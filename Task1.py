"""31. Даны два множества точек на плоскости. Выбрать четыре различные точки первого множества так,
чтобы квадрат с вершинами в этих точках накрывал все точки второго множества и имел минимальную площадь."""

points = [(1, 2), (2,1),(2,3),(2, 4), (3,4),(4,2),(5,3),(5, 8),(5,5), (4, 8), (8, 3),(6,4), (6, 1)]

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

def point_inside_angle(point1, point2, point3, checkpoint):
    if rotate(point2, point1, checkpoint) < 0 or rotate(point2, point3, checkpoint) > 0:
        return False
    return True

def intersect(p1, p2, x1, x2):
    return rotate(p1, p2, x1)*rotate(p1, p2, x2) <=0 and rotate(x1,x2,p1)*rotate(x1,x2,p2)<0 #имеют или не имеют пересечение в крайней точке


def check_inside_polygon(point, polygon):
    if point_inside_angle(polygon[0], polygon[1], polygon[2], point):
        l = 1
        r = len(polygon) - 1
        if len(polygon) > 3:
            while r-l > 1:
                q = (r+l)/2
                if rotate(polygon[0], polygon[q], point) > 0:
                    r = q
                else:
                    l = q
        return not intersect(polygon[0], point, polygon[l], polygon[r])
    else:
        return False


create_polygon(points)
print(intersect((2,1),(8,3),(5,3),(8,3)))
