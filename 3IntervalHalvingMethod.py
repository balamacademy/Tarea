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



def intervalMethod(x,error,funcion):
    a = x[0]
    b = x[-1]

    Xm = (a+b) / 2
    

    L = b - a

    bandera = 0



    while (bandera != 1):
        x1 = a + (L/4)
        x2 = b - (L/4)

        funcionX1 = funcion(x1)
        funcionX2 = funcion(x2)
        funcionXm = funcion(Xm)

        if funcionX1 < funcionXm:
            b = Xm
            Xm = x1
        else:
            if funcionX2 < funcionXm:
                a = Xm
                Xm = x2
            else:
                a = x1
                b = x2 

        L = b - a

        if abs(L) < error:
            # print(Xm)
            bandera = 1
        # else:
        #     print(x1)
        #     print(x2)
        #     print("\n"*3)
    return x1,x2



# x = np.arange(0,6,1)
# error = 10**-3



# precision
error = 0.7




x_lata = np.arange(0.5, 8.5)
resultados_lata = (intervalMethod(x_lata, error, lata))
print(resultados_lata)

x_caja = np.arange(2, 3.1,1)
resultados_caja = (intervalMethod(x_caja, error,caja))
print(resultados_caja)

x_funcion1 = np.arange(0.1, 11)
resultados_funcion1 = (intervalMethod(x_funcion1, error, funcion1))
print(resultados_funcion1)

x_funcion2 = np.arange(0.1, 5.1, 1)
resultados_funcion2 = (intervalMethod(x_funcion2, error, funcion2))
print(resultados_funcion2)

x_funcion3 = np.arange(-2.5, 2.6,1)
resultados_funcion3 = (intervalMethod(x_funcion3, error, funcion3))
print(resultados_funcion3)

x_funcion4 = np.arange(-1.5, 3,1)
resultados_funcion4 = (intervalMethod(x_funcion4, error, funcion4))
print(resultados_funcion4)
