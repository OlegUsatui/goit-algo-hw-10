import numpy as np
from scipy.integrate import quad


def f(x):
    return x ** 2

a = 0
b = 2

n = 10000

x_rand = np.random.uniform(a, b, n)
y_rand = np.random.uniform(0, f(b), n)

count_under_curve = np.sum(y_rand <= f(x_rand))

integral_estimate = (count_under_curve / n) * (b - a) * f(b)

exact_integral, _ = quad(f, a, b)

print("Оцінка інтеграла методом Монте-Карло:", integral_estimate)
print("Точне значення інтеграла за допомогою quad:", exact_integral)
