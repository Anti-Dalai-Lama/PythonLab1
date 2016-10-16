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
    pseudo_squares = list()

    def __init__(self, matrix):
        self.matrix = matrix
        self.width = len(matrix[0])
        self.height = len(matrix)

    def get_pseudo_squares(self):
        for i in range(0, self.height - 1):  # без прохода последней строки
            for j in range(0, self.width - 1):  # без прохода последнего столбца
                if (self.matrix[i][j + 1] == self.matrix[i + 1][j]):
                    sq = MatrixSquare(i, j, 2)
                    i1 = i
                    j1 = j
                    while (self.matrix[i1][j1 + 1] == self.matrix[i1 + 1][j1] and i1 < self.height - 2 and j1 < self.width - 2):
                        i1 += 1
                        j1 += 1
                        sq.side += 1
                    #добавить проверку на то, является ли матрица вписанной в другую?
                    self.pseudo_squares.append(sq)

    def print_pseudo_sq(self):
        for el in self.pseudo_squares:
            print(el)

    # def check_symmetric_square(self, matrix_square):
    #     for i in range(matrix_square.row + 1, matrix_square.row + matrix_square.side):
    #         for j in range(matrix_square.col, matrix_square.col + matrix_square.side):
    #             #check mirror elements




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
mymatrix.get_pseudo_squares()
mymatrix.print_pseudo_sq()

print(MatrixSquare(2,2,3).contains(MatrixSquare(3,3,3)))

