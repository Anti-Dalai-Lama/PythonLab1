"""73. В прямоугольной матрице выявить все квадратные подматрицы, симметричные относительно главной диагонали."""

class MatrixSquare(object):
    def __init__(self, row, col, side):
        self.row = row
        self.col = col
        self.side = side

    def contains(self, matrix_square):
        if(matrix_square.row >= self.row and matrix_square.col >= self.col and (matrix_square.row + matrix_square.side - 1) <= (self.row + self.side - 1) and (matrix_square.col + matrix_square.side - 1) <= (self.col + self.side - 1)):
            return True
        return False

    def __str__(self):
        return "Square row = " + str(self.row) + " col = " + str(self.col) + " side = " + str(self.side)


class Matrix(object):
    squares = list()

    def __init__(self, matrix):
        self.matrix = matrix
        self.width = len(matrix[0])
        self.height = len(matrix)

    def get_squares(self):
        for i in range(0, self.height - 1):  # без прохода последней строки
            for j in range(0, self.width - 1):  # без прохода последнего столбца
                if (self.matrix[i][j + 1] == self.matrix[i + 1][j]):
                    sq = MatrixSquare(i, j, 2)
                    i1 = i + 2
                    j1 = j + 2
                    while (i1 < self.height and j1 < self.width ):
                        sideup = True
                        for k in range(1, sq.side + 1):
                            if(self.matrix[i1][j1-k] != self.matrix[i1 - k][j1]):
                                sideup = False
                        if(sideup):
                            i1 += 1
                            j1 += 1
                            sq.side += 1
                        else:
                            break
                    #добавить проверку на то, является ли матрица вписанной в другую?
                    contained_flag = False
                    for square in self.squares:
                        if(square.side > sq.side and square.contains(sq)):
                            contained_flag = True
                            break
                    if(not contained_flag):
                        self.squares.append(sq)

    def print_sq(self):
        for el in self.squares:
            print(el)


matrix = [[5,0,7,9,1,2],
          [0,0,4,3,2,7],
          [8,3,1,2,8,1],
          [1,6,4,7,1,5],
          [0,9,5,5,3,7],
          [4,8,1,1,2,4],
          [1,3,0,5,6,3],
          [9,7,5,6,3,1],
          [8,3,6,3,1,8]]

mymatrix = Matrix(matrix)
mymatrix.get_squares()
mymatrix.print_sq()


