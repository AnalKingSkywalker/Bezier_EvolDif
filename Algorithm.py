import numpy as np
from scipy.special import comb
import matplotlib.pyplot as plt
"""
?? Falta normaliza la curva de los senos
?? Falta checar bien lo del polinomio de bezier por que el profe me dijo que me estaba complicando :c
?? Falta checar bien el algoritmo de optimizacion y las restricciones, propongo x_1 < x_2 <  ... < x_n
?? Falta presionar al sebas para que le avance con la simulacion
!! la arana esta mundando no puedo obtener las trayectorias reales hasta dentro de 3 semanas aproxs

"""
#Curva de bezier
def senos(frecuencias, amplitudes, muestras=1000):
    t = np.linspace(0, 1, muestras)  # Tiempo de 0 a 1 segundo
    senal = np.zeros_like(t)

    for f, a in zip(frecuencias, amplitudes):
        senal += a * np.sin(2 * np.pi * f * t)

    return senal


def curva_bezier(puntos_control, n_puntos=1000):
    n = len(puntos_control) - 1
    t = np.linspace(0, 1, n_puntos)
    curva = np.zeros((n_puntos, 2))

    for i, (px, py) in enumerate(puntos_control):
        bernstein = comb(n, i) * (t ** i) * ((1 - t) ** (n - i))
        curva[:, 0] += bernstein * px
        curva[:, 1] += bernstein * py

    return curva


def error_entre_curvas(curva_bezier, senal):
   #Error caudratico
    y_bezier = curva_bezier[:, 1]  
    if len(y_bezier) != len(senal):
        raise ValueError("longuitud de curcas diferentes")
    
    mse = np.mean((y_bezier - senal) ** 2)
    return mse

def main():

    print("Intento de generar curvas de Bezier en base a los puntos ingresados")
    n = int(input("Cantidad de puntos de la curva de bezier--> "))
    puntos = []
    for i in range(n):
        x = float(input(f"Coordenada x--> "))
        y = float(input(f"coordenada y --> "))
        puntos.append((x, y))

    muestras = 1000
    curva = curva_bezier(puntos, n_puntos=muestras)
    senal = senos([1, 2, 3], [1.0, 0.5, 0.1], muestras=muestras)

    error = error_entre_curvas(curva, senal)
    print(f"Error cuadrático medio: {error:.6f}")

    puntos = np.array(puntos)
    plt.plot(curva[:, 0], curva[:, 1], label="Curva de Bézier")
    plt.plot(np.linspace(curva[:,0].min(), curva[:,0].max(), len(senal)), senal, 
             color="black", label="Señal seno")
    plt.scatter(puntos[:, 0], puntos[:, 1], color="red", label="Puntos de control")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()

#0 0 137 10 330 0.1 500 0