# Вычислите выражение
import numpy as np

a = 1.21
b = 0.371
y = np.tan(np.power(a + b, 2)) - np.power(a + 1.5, 1 / 3) + a * np.power(b, 5) - b / np.log(np.power(a, 2))
print(y)


