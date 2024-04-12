import numpy as np
import matplotlib.pyplot as plt

# el -1 hace que cambie el sentido del probelma

def lata(x):
    operacion = ((2 * np.pi) * (x**2) + 500/x)
    return operacion


def caja(x):
    return -1*(((20 - (2 * x)) * (10 - (2 * x))) * (x))


def funcion1(x):
    return (x**2) + (54/x)


def funcion2(x):
    return (x**3) + (2*x) - 3


def funcion3(x):
    return (x**4) + (x**2) - 33


def funcion4(x):
    return (3*(x**4)) - (8*(x**3)) - (6*(x**2)) + (12*x)


def busqueda_exhaustiva(x, funcion, i):
    a = x[0]
    b = x[-1]
    n = int((2 * (b - a)) / i)
    delta = ((b - a) / n)
    x1 = a
    x2 = x1 + delta
    x3 = x2 + delta
    fx1 = funcion(x1)
    fx2 = funcion(x2)
    fx3 = funcion(x3)
    while (b >= x3):
        if fx1 >= fx2 and fx2 <= fx3:
            return x1, x3
        else:
            x1 = x2
            x2 = x3
            x3 = x3 + delta
            fx1 = funcion(x1)
            fx2 = funcion(x2)
            fx3 = funcion(x3)
    return x1, x3


def plot_function(ax, x_range, y_values, label, color):
    ax.plot(x_range, y_values, label=label, color=color)


def plot_points(ax, x_values, y_values, label, color):
    ax.scatter(x_values, y_values, label=label, color=color)


n_precisions = [0.5, 0.1, 0.01, 0.0001]

for n_precision in n_precisions:
    # Definición de los rangos para cada función
    x_lata = np.arange(0.5, 8.5, 0.01)
    x_caja = np.arange(2, 3.1, 0.01)
    x_funcion1 = np.arange(0.1, 10, 0.01)
    x_funcion2 = np.arange(0.1, 5, 0.01)
    x_funcion3 = np.arange(-2.5, 2.5, 0.01)
    x_funcion4 = np.arange(-1.5, 3, 0.01)

    # Ejecutar la búsqueda exhaustiva y obtener los puntos mínimos para cada función
    min_lata = busqueda_exhaustiva(x_lata, lata, n_precision)
    min_caja = busqueda_exhaustiva(x_caja, caja, n_precision)
    min_funcion1 = busqueda_exhaustiva(x_funcion1, funcion1, n_precision)
    min_funcion2 = busqueda_exhaustiva(x_funcion2, funcion2, n_precision)
    min_funcion3 = busqueda_exhaustiva(x_funcion3, funcion3, n_precision)
    min_funcion4 = busqueda_exhaustiva(x_funcion4, funcion4, n_precision)

    # Calcular los valores de las funciones en los rangos dados
    y_lata = lata(x_lata)
    y_caja = caja(x_caja)
    y_funcion1 = funcion1(x_funcion1)
    y_funcion2 = funcion2(x_funcion2)
    y_funcion3 = funcion3(x_funcion3)
    y_funcion4 = funcion4(x_funcion4)

    # Graficar
    fig, axs = plt.subplots(2, 3, figsize=(15, 10))

    plot_function(axs[0, 0], x_lata, y_lata, 'Lata', 'blue')
    plot_points(axs[0, 0], [min_lata[0], min_lata[1]], [lata(min_lata[0]), lata(min_lata[1])], 'Min Lata', 'red')
    axs[0, 0].set_title(f'Lata (n_precision = {n_precision})')

    plot_function(axs[0, 1], x_caja, y_caja, 'Caja', 'green')
    plot_points(axs[0, 1], [min_caja[0], min_caja[1]], [caja(min_caja[0]), caja(min_caja[1])], 'Min Caja', 'red')
    axs[0, 1].set_title(f'Caja (n_precision = {n_precision})')

    plot_function(axs[0, 2], x_funcion1, y_funcion1, 'Función 1', 'orange')
    plot_points(axs[0, 2], [min_funcion1[0], min_funcion1[1]], [funcion1(min_funcion1[0]), funcion1(min_funcion1[1])], 'Min Función 1', 'red')
    axs[0, 2].set_title(f'Función 1 (n_precision = {n_precision})')

    plot_function(axs[1, 0], x_funcion2, y_funcion2, 'Función 2', 'purple')
    plot_points(axs[1, 0], [min_funcion2[0], min_funcion2[1]], [funcion2(min_funcion2[0]), funcion2(min_funcion2[1])], 'Min Función 2', 'red')
    axs[1, 0].set_title(f'Función 2 (n_precision = {n_precision})')

    plot_function(axs[1, 1], x_funcion3, y_funcion3, 'Función 3', 'brown')
    plot_points(axs[1, 1], [min_funcion3[0], min_funcion3[1]], [funcion3(min_funcion3[0]), funcion3(min_funcion3[1])], 'Min Función 3', 'red')
    axs[1, 1].set_title(f'Función 3 (n_precision = {n_precision})')

    plot_function(axs[1, 2], x_funcion4, y_funcion4, 'Función 4', 'pink')
    plot_points(axs[1, 2], [min_funcion4[0], min_funcion4[1]], [funcion4(min_funcion4[0]), funcion4(min_funcion4[1])], 'Min Función 4', 'red')
    axs[1, 2].set_title(f'Función 4 (n_precision = {n_precision})')

    plt.tight_layout()
    plt.show()
