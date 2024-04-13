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




def metodo_biseccion(a_orginal, b_original, e, funcion):


    a = np.random.uniform(a_orginal, b_original)
    b = np.random.uniform(a_orginal, b_original)







    # a por a nueva
    # b por b nueva
    while(primeraderivadanumerica(a, funcion) > 0):
        a = np.random.uniform(a_orginal, b_original)
    
    while (primeraderivadanumerica(b, funcion) < 0): 
        b = np.random.uniform(a_orginal, b_original)
    
    x1=a
    x2=b
    z = ((x2+x1)/2)
    
    while(primeraderivadanumerica(z, funcion) > e):
        if primeraderivadanumerica(z, funcion) < 0: 
            x1 = z
            z = 0
            z = int((x2+x1)/2)

        elif primeraderivadanumerica(z,funcion) > 0: 
            x2 = z
            z = 0
            z = ((x2+x1)/2)
    
    return x1 , x2












