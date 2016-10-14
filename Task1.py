"""31. Даны два множества точек на плоскости. Выбрать четыре различные точки первого множества так,
чтобы квадрат с вершинами в этих точках накрывал все точки второго множества и имел минимальную площадь."""

#https://habrahabr.ru/post/144571/ - rotate, intersection
#https://habrahabr.ru/post/144921/ - Graham algorithm

import math

class VectorOperations(object):
    @staticmethod
    def rotate(left, mid, right): #если точка r вектора rm лежит левее вектора ml, то z > 0 (в векторном произведении первый множитель лежит правее)
        return (mid[0]-left[0])*(right[1]-mid[1])-(mid[1]-left[1])*(right[0]-mid[0]) #векторное произведение a × b = {aybz - azby; azbx - axbz; axby - aybx} > 0 если поворот левый! (смотрим только z координату!))

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

    def __getitem__(self, key):
        return self.points[key]

    def __setitem__(self, key, value):
        self.points[key] = value

    def __len__(self):
        return len(self.points)

def point_inside_angle(point1, point2, point3, checkpoint): #can be on the line
    if VectorOperations.rotate(point2, point1, checkpoint) > 0 or VectorOperations.rotate(point2, point3, checkpoint) < 0:
        return False
    return True

def intersect(p1, p2, x1, x2):
    return VectorOperations.rotate(p1, p2, x1)*VectorOperations.rotate(p1, p2, x2) <=0 and VectorOperations.rotate(x1,x2,p1)*VectorOperations.rotate(x1,x2,p2)<=0 #имеют пересечение в крайней точке


def point_inside_polygon(point, polygon):
    startpoint = polygon[0]
    if point_inside_angle(polygon[-1], startpoint, polygon[1], point) and point != startpoint:
        r = 1
        l = len(polygon) - 1
        if len(polygon) > 3: #проверяем четырехугольники и больше
            while l - r > 1:
                q = (r+l)//2
                if VectorOperations.rotate(startpoint, polygon[q], point) > 0:
                    r = q
                else:
                    l = q
        return not intersect(startpoint, point, polygon[l], polygon[r])
    else:
        return False

def delete_excess_points(points, polygon):
    return filter(lambda x: point_inside_polygon(x, polygon), points)

def points_inside_polygon(points, polygon):
    flag = True
    for i in range(0, len(points)):
        flag = flag and point_inside_polygon(points[i], polygon)
    return flag

def vector_module(point1, point2):
    return int(math.sqrt(math.pow(point1[0] - point2[0],2) + math.pow(point1[1] - point2[1],2)) * 1000)

def get_lines_by_length_dict(points):
    dictionary = {}
    print(points)
    for i in range(0, len(points)-1):
        for j in range(i+1, len(points)):
            length = vector_module(points[j], points[i])
            if(length in dictionary):
                dictionary[length].append((points[j], points[i]))
            else:
                dictionary[length] = [(points[j], points[i])]

    dictionary.pop(min(dictionary.items(), key=lambda x: x[0])[0])
    return dictionary

def find_allowed_square(dictionary, polygon):
    while(len(dictionary) != 0):
        current = dictionary.pop(min(dictionary.items(), key=lambda x: x[0])[0])
        square = get_squares(current[1], polygon)
        if(square != False):
            return square


def get_squares(lines, polygon):
    for i in range(0, len(lines)-1):
        for j in range(i+1, len(lines)):
            if(intersect(lines[i][0], lines[i][1], lines[j][0], lines[j][1]) and diagonals_create_square(lines[i], lines[j])):
                if(points_inside_polygon((lines[i][0],lines[j][1],lines[i][1],lines[j][0]), polygon)):
                    return (lines[i][0],lines[j][1],lines[i][1],lines[j][0])
    return False

def diagonals_create_square(line1, line2):
    return vector_module(line1[0],line2[0]) == vector_module(line1[0],line2[1]) == vector_module(line1[1],line2[0]) == vector_module(line1[1],line2[1])




points = [(1, 2), (2,1),(2,3),(2, 4), (3,4),(4,2),(5,3),(5, 8),(5,5), (4, 8), (8, 3),(6,4), (6, 1)]

polygon = Polygon(points)



get_lines_by_length_dict([(4,2),(5,3),(1,3),(0,0),(4,8)])

# get_squares([((1,1),(4,4)), ((1,4),(4,1)), ((4,4),(1,7)), ((4,7),(1,4)),
#                            ((4,4),(7,7)), ((2,3),(5,0))])