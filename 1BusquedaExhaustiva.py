import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# x = np.arange(0.5, 8.5, 0.5)
def lata(x):
    operacion = -1 * ((2 * np.pi) * (x**2) + 500/x)
    return operacion

# x = np.arange(2, 3.1, 0.1)
def caja(x):
    operacion = ((20 - (2 * x)) * (10 - (2 * x))) * (x)
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
    operacion = (x**2) + 3
    return operacion

def deltas(a,b,n):
    return ((b - a) / n)



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
    while (b>=x3):
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


n_precision = 0.5


x_lata = np.arange(0.5, 8.5)
print(busqueda_exhaustiva(x_lata, lata,  n_precision))

x_caja = np.arange(2, 3.1)
print(busqueda_exhaustiva(x_caja, caja,  n_precision))


x_funcion1 = np.arange(0.1, 10)
print(busqueda_exhaustiva(x_funcion1, funcion1, n_precision))

x_funcion2 = np.arange(0.1, 5)
print(busqueda_exhaustiva(x_funcion2, funcion2, n_precision))


x_funcion3 = np.arange(-2.5, 2.5)
print(busqueda_exhaustiva(x_funcion3, funcion3, n_precision))


x_funcion4 = np.arange(-1.5, 3)
print(busqueda_exhaustiva(x_funcion4, funcion4,  n_precision))



