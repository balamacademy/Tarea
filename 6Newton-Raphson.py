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









def primera_derivada(x, f):
    delta=0.0001
    return ( (f(x) + delta) - (f(x)-delta) ) / (2 * delta)

def segunda_derivada(x, f):
    delta=0.0001
    return ( (f(x) + delta) - (2*f(x)) + (f(x)-delta) )/ delta




def newton_raphson(x,e,f):
    k=1
    x_actual=x[k]
    xderiv=primera_derivada(x_actual,f)
    xderiv2=segunda_derivada(x_actual,f)
    xsig= x_actual  - (xderiv/xderiv2)
    while (primera_derivada(xsig,f) > e):
        k+=1
        if k >= len(x):
            return xsig
        x_actual=x[k]
        xderiv=primera_derivada(x_actual,f)
        xderiv2=segunda_derivada(x_actual,f)
        xsig= x_actual  - (xderiv/xderiv2)
        
    return xsig







def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    """
    Implementación del método de Newton-Raphson para encontrar la raíz de una función.

    Args:
    f: Función cuya raíz se quiere encontrar.
    df: Derivada de la función f.
    x0: Valor inicial para iniciar las iteraciones.
    tol: Tolerancia, criterio de convergencia.
    max_iter: Número máximo de iteraciones permitidas.

    Returns:
    x: La aproximación de la raíz.
    """
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x
        dfx = df(x)
        if dfx == 0:
            raise ValueError("La derivada se hizo cero.")
        x = x - fx / dfx
    raise ValueError("El método no convergió después de {} iteraciones.".format(max_iter))

# Ejemplo de uso
if __name__ == "__main__":
    import math

    # Definición de la función y su derivada
    def f(x):
        return x**2 - 4

    def df(x):
        return 2 * x

    # Valor inicial
    x0 = 3

    # Llamada al método de Newton-Raphson
    raiz = newton_raphson(f, df, x0)

    print("La raíz encontrada es:", raiz)
