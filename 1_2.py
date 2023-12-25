'''Найти оценки уравнения регрессии, используя метод наименьших квадратов и матричную форму записи уравнений'''
import numpy as np

def print_two_matrix(matrix1, matrix2):
    for item in range(len(matrix1)):
        print(str(matrix1[item]) + "|" + str(matrix2[item]))


# consatenate() соединяет массивы вдоль указанной оси.
# ones() возвращает новый массив, заполненный единицами.
X = np.concatenate((np.ones((1, 12), dtype=int),
                    np.random.randint(24, 24 + 12, (1, 12), dtype=int),
                    np.random.randint(60, 82, (1, 12), dtype=int)),
                   axis=0).transpose()
Y = np.random.uniform(13.5, 18.6, (12, 1))
# np.linalg.inv - обратная матрица
A = (np.linalg.inv(X.transpose().dot(X))).dot(X.transpose().dot(Y))
print("Вектор оценок матрицы А: \n" + str(A))

y = A[0] + A[1] * X.transpose()[1] + A[2] * X.transpose()[2]
print_two_matrix(y, Y)

# transpose() меняет оси в обратном порядке или перемещает оси массива в указанные положения.
# dot() вычисляет скалярное произведение двух массивов
