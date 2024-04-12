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


def minimo(a, b):
    if a < b:
        return a
    else:
        return b



def fibonacci(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b



def fibonacciSearch(x, funcion):
    a = x[0]
    b = x[-1]

    L = b - a

    n = 7
    k = 2

    bandera = 0

    # paso 2
    while (bandera != 1):
        i = n - k + 2
        Fi = fibonacci(i)

        j = n + 2
        Fj = fibonacci(j)

        L_K = (Fi/Fj) * L

        x1 = a + L_K
        x2 = b - L_K


        funcionX1 = funcion(x1)
        funcionX2 = funcion(x2)


        if funcionX1 > funcionX2:
            a = x1

        elif funcionX1 < funcionX2:
            b = x2

        elif funcionX1 == funcionX2:
            a = x1
            b = x2


        if k == n:
            bandera = 1
        else:
            k += 1

    # return x1, x2
    # if funcion(x1) < funcion(x2):
    #     return x1
    # else:
    #     return x2
    return a,b


# x = np.arange(0,6,1)
# print(fibonacciSearch(x, funcion1))


x_lata = np.arange(0.5, 8,0.5)
resultados_lata = (fibonacciSearch(x_lata, lata))
print(resultados_lata)

x_caja = np.arange(2, 3.1)
resultados_caja = (fibonacciSearch(x_caja, caja))
print(resultados_caja)

x_funcion1 = np.arange(0.1, 11)
resultados_funcion1 = (fibonacciSearch(x_funcion1, funcion1))
print(resultados_funcion1)

x_funcion2 = np.arange(0.1, 5.1, 1)
resultados_funcion2 = (fibonacciSearch(x_funcion2, funcion2))
print(resultados_funcion2)

x_funcion3 = np.arange(-2.5, 2.6,1)
resultados_funcion3 = (fibonacciSearch(x_funcion3, funcion3))
print(resultados_funcion3)

x_funcion4 = np.arange(-1.5, 3,1)
resultados_funcion4 = (fibonacciSearch(x_funcion4, funcion4))
print(resultados_funcion4)
