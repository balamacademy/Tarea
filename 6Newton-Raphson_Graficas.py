import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def lata(x):
    return (2 * np.pi) * (x**2) + 500/x

def caja(x):
    return -1 * (((20 - (2 * x)) * (10 - (2 * x))) * (x))

def funcion1(x):
    return x**2 + 54/x

def funcion2(x):
    return x**3 + 2*x - 3

def funcion3(x):
    return x**4 + x**2 - 33

def funcion4(x):
    return 3*(x**4) - 8*(x**3) - 6*(x**2) + 12*x

def primera_derivada(x, f):
    delta = 0.0001
    return (f(x + delta) - f(x - delta)) / (2 * delta)

def segunda_derivada(x, f):
    delta = 0.0001
    return (f(x + delta) - 2 * f(x) + f(x - delta)) / (delta**2)

def metodo_newton(x, e, funcion):
    k = 0
    x_actual = x[k]
    x_derivada1 = primera_derivada(x_actual, funcion)
    x_derivada2 = segunda_derivada(x_actual, funcion)
    x_siguiente = x_actual - (x_derivada1 / x_derivada2)
    while abs(primera_derivada(x_siguiente, funcion)) > e:
        k += 1
        if k >= len(x):
            return x_siguiente
        x_actual = x[k]
        x_derivada1 = primera_derivada(x_actual, funcion)
        x_derivada2 = segunda_derivada(x_actual, funcion)
        x_siguiente = x_actual - (x_derivada1 / x_derivada2)
    return x_siguiente

def plot_function(ax, x_range, y_values, label, color):
    ax.plot(x_range, y_values, label=label, color=color)

def plot_points(ax, x_value, y_value, label, color):
    ax.scatter(x_value, y_value, label=label, color=color)

n_precisions = [0.5, 0.1, 0.01, 0.0001]

for n_precision in n_precisions:
    fig, axs = plt.subplots(2, 3, figsize=(15, 10))
    x_ranges = [np.arange(0.5, 8.5, 0.01),
                np.arange(2, 3.1, 0.01),
                np.arange(0.1, 10, 0.01),
                np.arange(0.1, 5, 0.01),
                np.arange(-2.5, 2.5, 0.01),
                np.arange(-1.5, 3, 0.01)]
    
    functions = [lata, caja, funcion1, funcion2, funcion3, funcion4]

    for i, (x_range, func) in enumerate(zip(x_ranges, functions)):
        min_point = metodo_newton(x_range, n_precision, func)
        y_values = func(x_range)

        row = i // 3
        col = i % 3

        ax = axs[row, col]

        plot_function(ax, x_range, y_values, func.__name__, 'blue')
        plot_points(ax, min_point, func(min_point), f'Min {func.__name__}', 'red')
        ax.set_title(f'{func.__name__} (n_precision = {n_precision})')

    plt.tight_layout()
    plt.show()

