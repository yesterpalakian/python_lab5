'''
Построить графики следующих функций, изменения и диапазон
аргумента задать самостоятельно:
'''

from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)

X, Y = np.meshgrid(x, y)


def f1(x, y):
    return np.power(x, 0.25) + np.power(y, 0.25)


def f2(x, y):
    return np.power(x, 2) - np.power(y, 2)


def f3(x, y):
    return 2 * x + 3 * y


def f4(x, y):
    return np.power(x, 2) + np.power(y, 2)


def f5(x, y):
    return 2 + 2 * x + 2 * y - np.power(x, 2) - np.power(y, 2)


Z1 = f1(X, Y)
Z2 = f2(X, Y)
Z3 = f3(X, Y)
Z4 = f4(X, Y)
Z5 = f5(X, Y)


fig = plt.figure(figsize=(12, 10))

# График функции z = x^0.25 + y^0.25
ax1 = fig.add_subplot(231, projection='3d')
ax1.plot_surface(X, Y, Z1, cmap='viridis')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')
ax1.set_title('z = x^0.25 + y^0.25')

# График функции z = x^2 - y^2
ax2 = fig.add_subplot(232, projection='3d')
ax2.plot_surface(X, Y, Z2, cmap='viridis')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')
ax2.set_title('z = x^2 - y^2')

# График функции z = 2x + 3y
ax3 = fig.add_subplot(233, projection='3d')
ax3.plot_surface(X, Y, Z3, cmap='viridis')
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_zlabel('z')
ax3.set_title('z = 2x + 3y')

# График функции z = x^2 + y^2
ax4 = fig.add_subplot(234, projection='3d')
ax4.plot_surface(X, Y, Z4, cmap='viridis')
ax4.set_xlabel('x')
ax4.set_ylabel('y')
ax4.set_zlabel('z')
ax4.set_title('z = x^2 + y^2')

# График функции z = 2 + 2x + 2y - x^2 - y^2
ax5 = fig.add_subplot(235, projection='3d')
ax5.plot_surface(X, Y, Z5, cmap='viridis')
ax5.set_xlabel('x')
ax5.set_ylabel('y')
ax5.set_zlabel('z')
ax5.set_title('z = 2 + 2x + 2y - x^2 - y^2')


plt.tight_layout()
plt.show()
