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
    operacion = (x**2) + 3
    return operacion


# def bounding_phase(delta, f):
#     x_0 = 0.6

#     if f(x_0 - abs(delta)) > f(x_0) > f(x_0 + abs(delta)):
#         delta = abs(delta)
#     else:
#         if delta < 0:
#             delta = delta
#         else:
#             delta = -1 * delta

#     k = 0
#     condicion = True

#     while condicion:
#         x_anterior = x_0 
#         x_actual = x_0 + (2**k * delta)  
#         k += 1

#         if f(x_actual) < f(x_0):
#             x_0 = x_actual
#         else:
#             condicion = False

#     return x_anterior, x_actual  


def metodo_fase(punto_inicial, delta, funcion):
    punto_inicial = 0.6
    k = 0

    x1 = punto_inicial - abs(delta)  
    x2 = punto_inicial
    x3 = punto_inicial + abs(delta)

    fx1 = funcion(x1)
    fx2 = funcion(x2)
    fx3 = funcion(x3)

    if fx1 > fx2 > fx3:
        delta = abs(delta)
    else:
        if delta < 0:
            delta = delta
        else:
            delta = -1 * delta


    bandera = 0

    # x_anterior = x2
    # f_anterior = funcion(x_anterior)

    # x_nueva = x_anterior + (2**k) * delta
    # f_nueva = funcion(x_nueva)

    while (bandera != 1):

        x_anterior = x2
        f_anterior = funcion(x_anterior)
        x_nueva = x_anterior + ((2**k) * delta)
        f_nueva = funcion(x_nueva)
        k += 1

        if (f_nueva < f_anterior):
            x2 = x_nueva
        else:
            bandera = 1

        # if f_nueva < f_anterior:
            # k += 1
        #     x_anterior = x_nueva
        #     x_nueva = x_anterior + (2**k) * delta
            
        #     f_anterior = funcion(x_anterior)
        #     f_nueva = funcion(x_nueva)
        # else:
            # print(x_anterior)
            # print(x_nueva)
            # bandera=1
    return x_anterior, x_nueva


# punto_incial = 0.6


# precision
delta = 0.5 



x_lata = np.arange(1, 8)
resultados_lata = (metodo_fase(x_lata[0],delta, lata))
print("Resultados Lata: {}".format(resultados_lata))

x_caja = np.arange(2.1, 3.1,1)
resultados_caja = (metodo_fase(x_caja[0],delta, caja))
print("Resultados Caja: {}".format(resultados_caja))


x_funcion1 = np.arange(0.1, 11)
resultados_funcion1 = (metodo_fase(x_funcion1[0],delta, funcion1))
print("Resultados Funcion 1: {}".format(resultados_funcion1))


# x_funcion2 = np.arange(0.1, 5.1, 1)
# resultados_funcion2 = (metodo_fase(x_funcion2[0],delta, funcion2))
# print("Resultados Funcion 2: {}".format(resultados_funcion2))

x_funcion3 = np.arange(-2.5, 2.6,1)
resultados_funcion3 = (metodo_fase(x_funcion3[0],delta, funcion3))
print("Resultados Funcion 3: {}".format(resultados_funcion3))

x_funcion4 = np.arange(-1.5, 3,1)
resultados_funcion4 = (metodo_fase(x_funcion4[0],delta, funcion4))
print("Resultados Funcion 4: {}".format(resultados_funcion4))




# print("\n"*10)

# # x_funcion1 = np.arange(0.1, 11)
# delta2 = 0.5
# resul = (metodo_fase(0.6,delta2, funcion1))
# print(resul)


# print("\n"*10)