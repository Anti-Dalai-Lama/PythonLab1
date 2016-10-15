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

    #def check_symmetric_square(self):




matrix = [[1,4,6,4,7],
          [7,3,5,9,2],
          [0,0,5,4,3],
          [3,3,5,2,8],
          [4,6,4,3,2],
          [4,2,9,5,4],
          [1,1,6,8,3],
          [4,5,8,6,4],
          [5,7,4,2,1]]

mymatrix = Matrix(matrix)
mymatrix.get_pseudo_squares()

print(MatrixSquare(2,2,3).contains(MatrixSquare(3,3,3)))

