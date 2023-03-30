class Matrix:
    def __init__(self, rows, cols, data):
        self.rows = rows
        self.cols = cols
        self.data = data
        
    def __str__(self):
        return '\n'.join([' '.join([str(self.data[i][j]) for j in range(self.cols)]) for i in range(self.rows)])
    
    def get_minor(self, row, col):
        data = [[self.data[i][j] for j in range(self.cols) if j != col] for i in range(self.rows) if i != row]
        return Matrix(self.rows-1, self.cols-1, data)
    
    def sarrus(self):
        if self.rows != self.cols:
            raise ValueError('La matriz debe ser cuadrada')
        if self.rows == 2:
            return self.data[0][0]*self.data[1][1] - self.data[1][0]*self.data[0][1]
        elif self.rows == 3:
            return (self.data[0][0]*self.data[1][1]*self.data[2][2] +
                    self.data[0][1]*self.data[1][2]*self.data[2][0] +
                    self.data[0][2]*self.data[1][0]*self.data[2][1] -
                    self.data[2][0]*self.data[1][1]*self.data[0][2] -
                    self.data[2][1]*self.data[1][2]*self.data[0][0] -
                    self.data[2][2]*self.data[1][0]*self.data[0][1])
        else:
            res = 0
            signo = 1
            for j in range(self.cols):
                minor = self.get_minor(0, j)
                res += signo*self.data[0][j]*minor.sarrus()
                signo *= -1
            return res

data = [[1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]]

m = Matrix(5, 5, data)
print(m.sarrus())  # resultado: 0

