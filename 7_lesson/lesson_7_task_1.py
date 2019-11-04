class Matrix:

    def __init__(self, list_1, list_2, list_3, list_4):
        self.list_1 = list_1
        self.list_2 = list_2
        self.list_3 = list_3
        self.list_4 = list_4


    def __add__(self, other):
        return Matrix([sum(i) for i in zip(*(self.list_1, other.list_1))],
                      [sum(i) for i in zip(*(self.list_2, other.list_2))],
                      [sum(i) for i in zip(*(self.list_3, other.list_3))],
                      [sum(i) for i in zip(*(self.list_4, other.list_4))])

    def __str__(self):
        return f'Сумма двух матриц\n({self.list_1},\n {self.list_2},\n' \
               f' {self.list_3},\n {self.list_4}) '

matrix_1 = Matrix([11, 9, 8, 7], [4, 4, 16, 4],
                  [2, 16, 12, 11], [19, 13, 18, 5])
matrix_2 = Matrix([12, 8, 14, 19], [12, 1, 17, 12],
                  [15, 9, 0, 12], [6, 10, 16, 18])
print(matrix_1 + matrix_2)



"""
import random
class Matrix:
    def __init__(self, matrix_1, matrix_2):
        self.matrix_1 = matrix_1
        self.matrix_2 = matrix_2
    def matrix_view_1(self):
        for i in range(4):
            print(self.matrix_1[i])
    def matrix_view_2(self):
        for i in range(4):
            print(self.matrix_2[i])
N= 4
M = 4
rows_matrix = Matrix(([[random.randrange(0, 20) for y in range(M)] for x in range(N)]),
                       ([[random.randrange(0, 20) for el in range(M)] for op in range(N)]))
print('Перваая матрица.')
rows_matrix.matrix_view_1()
print('Вторая матрица.')
rows_matrix.matrix_view_2()
"""