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



def GoldenSectionSearch(x):
    error = 1e-3
    phi = (1 + np.sqrt(5)) / 2  # Proporción dorada
    # print(phi)


    a = x[0]
    b = x[-1]
    L = b - a
    k = 1

    while L > error:
        # Calcular los puntos w1 y w2 utilizando la proporción dorada
        w1 = b - (b - a) / phi
        w2 = a + (b - a) / phi
        
        funcionW1 = funcion1(w1)
        funcionW2 = funcion1(w2)

        if funcionW1 < funcionW2:
            b = w2
        else:
            a = w1

        # L = longitud del intervalo
        L = b - a
        

        k += 1
    return a



x_lata = np.arange(0.5, 8,0.5)
resultados_lata = (GoldenSectionSearch(x_lata))
print(resultados_lata)

x_caja = np.arange(2.1, 3.1,1)
resultados_caja = (GoldenSectionSearch(x_caja))
print(resultados_caja)

x_funcion1 = np.arange(0.1, 11)
resultados_funcion1 = (GoldenSectionSearch(x_funcion1))
print(resultados_funcion1)

x_funcion2 = np.arange(0.1, 5.1, 1)
resultados_funcion2 = (GoldenSectionSearch(x_funcion2))
print(resultados_funcion2)

x_funcion3 = np.arange(-2.5, 2.6,1)
resultados_funcion3 = (GoldenSectionSearch(x_funcion3))
print(resultados_funcion3)

x_funcion4 = np.arange(-1.5, 3,1)
resultados_funcion4 = (GoldenSectionSearch(x_funcion4))
print(resultados_funcion4)
