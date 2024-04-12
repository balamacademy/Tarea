import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# x = np.arange(0.5, 8.5, 0.5)
def lata(x):
    operacion = 2 * np.pi * (x**2)
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


def GoldenSectionSearch(funcion, a, b, epsilon):
    
    golden = 0.618
    inv_golden = 1 - golden

    x1 = a + inv_golden * (b - a)
    x2 = a + golden * (b - a)

    f_x1 = funcion(x1)
    f_x2 = funcion(x2)

    while b - a > epsilon:
        
        if f_x1 < f_x2:
            b = x2
            x2 = x1
            x1 = a + inv_golden * (b - a)
            f_x2 = f_x1
            f_x1 = funcion(x1)
        else:
            a = x1
            x1 = x2
            x2 = a + golden * (b - a)
            f_x1 = f_x2
            f_x2 = funcion(x2)

    return (a, b)