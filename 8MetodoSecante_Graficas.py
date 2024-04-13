
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# x = np.arange(0.5, 8.5, 0.5)
def lata(x):
    operacion = ((2 * np.pi) * (x**2) + 500/x)
    return operacion

# x = np.arange(2, 3.1, 0.1)
def caja(x):
    operacion =(20 - 2 * x) * (10 - 2 * x) * (x)
    return operacion

# Valores entre 0 o igual a 10
def funcion1(x):
    operacion = (x**2) + (54/x)
    return operacion

# Valores entre 0 o igual a 5
def funcion2(x):
    operacion = (x**3) + (2*x) - 3
    return operacion

# Valores entre -2.5 o igual a 2.5
def funcion3(x):
    operacion = (x**4) + (x**2) - 33
    return operacion

# Valores entre -1.5 o igual a 3
def funcion4(x):
    operacion = (3*(x**4)) - (8*(x**3)) - (6*(x**2)) + (12*x) 
    return operacion


def prueba(x):
    return (x**2)




def primeraderivadanumerica(x_actual,f):
    delta=0.0001
    numerador= f(x_actual + delta) - f (x_actual - delta) 
    return numerador / (2 * delta)

def segundaderivadanumerica(x_actual,f):
    delta=0.0001
    numerado= f(x_actual + delta) - (2 * f (x_actual + f(x_actual- delta))) 
    return numerado / (delta**2)
def calculozensecante(x2,x1,f):
    numerador=primeraderivadanumerica(x2,f)
    denominador=((primeraderivadanumerica(x2,f) - primeraderivadanumerica (x1,f)))/(x2-x1)
    op=numerador/denominador
    return x2 - op







def metodo_secante(x,e,f):

    a_orginal = x[0]
    b_original = x[-1]


    a = np.random.uniform(a_orginal, b_original)
    b = np.random.uniform(a_orginal, b_original)
    while(primeraderivadanumerica(a,f) > 0):
        a = np.random.uniform(a_orginal, b_original)
    
    while (primeraderivadanumerica(b,f) < 0): 
        b = np.random.uniform(a_orginal, b_original)
    x1=a
    x2=b
    z = calculozensecante(x2,x1,f)
    while(primeraderivadanumerica(z,f) > e): 
        if primeraderivadanumerica(z,f) < 0: 
            x1=z
            z=0
            z = calculozensecante(x2,x1,f)
        if primeraderivadanumerica(z,f) > 0: 
            x2=z
            z=0
            z = calculozensecante(x2,x1,f)
    return x1 , x2











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
    # x_funcion2 = np.arange(0.1, 5, 0.01)
    x_funcion3 = np.arange(-2.5, 2.5, 0.01)
    x_funcion4 = np.arange(-1.5, 3, 0.01)

    # Ejecutar la búsqueda exhaustiva y obtener los puntos mínimos para cada función
    min_lata = metodo_secante(x_lata, n_precision, lata)
    min_caja = metodo_secante(x_caja,n_precision, caja)
    min_funcion1 = metodo_secante(x_funcion1, n_precision, funcion1)
    # min_funcion2 = metodo_biseccion(x_funcion2, n_precision, funcion2)
    min_funcion3 = metodo_secante(x_funcion3, n_precision, funcion3)
    min_funcion4 = metodo_secante(x_funcion4, n_precision, funcion4)

    # Calcular los valores de las funciones en los rangos dados
    y_lata = lata(x_lata)
    y_caja = caja(x_caja)
    y_funcion1 = funcion1(x_funcion1)
    # y_funcion2 = funcion2(x_funcion2)
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

    # plot_function(axs[1, 0], x_funcion2, y_funcion2, 'Función 2', 'purple')g

    plot_function(axs[1, 1], x_funcion3, y_funcion3, 'Función 3', 'brown')
    plot_points(axs[1, 1], [min_funcion3[0], min_funcion3[1]], [funcion3(min_funcion3[0]), funcion3(min_funcion3[1])], 'Min Función 3', 'red')
    axs[1, 1].set_title(f'Función 3 (n_precision = {n_precision})')

    plot_function(axs[1, 2], x_funcion4, y_funcion4, 'Función 4', 'pink')
    plot_points(axs[1, 2], [min_funcion4[0], min_funcion4[1]], [funcion4(min_funcion4[0]), funcion4(min_funcion4[1])], 'Min Función 4', 'red')
    axs[1, 2].set_title(f'Función 4 (n_precision = {n_precision})')

    plt.tight_layout()
    plt.show()