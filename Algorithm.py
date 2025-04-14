import numpy as np
from scipy.special import comb
import matplotlib.pyplot as plt

#Curva de bezier
def senos(frecuencias, amplitudes, fs = 1000):
    t = np.linspace(0, 0.5, int(0.5 * fs))  # de 0 a 2 segundos
    senal = np.zeros_like(t)
    
    for f, a in zip(frecuencias, amplitudes):
        senal += a * np.sin(2 * np.pi * f * t )

    return senal

def curva_bezier(puntos_control, n_puntos=100):
    n = len(puntos_control) - 1  
    t = np.linspace(0, 1, n_puntos)  
    curva = np.zeros((n_puntos, 2))  
    
    for i, (px, py) in enumerate(puntos_control):


        polinomio_bernstein = comb(n, i) * (t ** i) * ((1 - t) ** (n - i))
        

        curva[:, 0] += polinomio_bernstein * px
        curva[:, 1] += polinomio_bernstein * py
    
    return curva

def main():
    print("Intento de generar curvas de Bezier en vbase a klos puntos ingresados")

    n = int(input("Cantidad de puntos de la curva de bezier--> "))

    puntos = []

    for i in range(n):
        x = float(input(f"Coordenada x-->")) # Agrega los puntos a una lista
        y = float(input(f"coordenada y -->"))
        puntos.append((x,y))
    
    curva = curva_bezier(puntos)
    senal = senos([1, 3, 5], 
                  [1.0, 0.5, 0.3])
    #Graficamos

    puntos = np.array(puntos)
    plt.plot(curva[:,0], curva[:,1], label = "Intento de curva")
    plt.plot(senal)
    plt.scatter(puntos[:,0], puntos[:,1], color = "black", label = "puntos ingresados")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()
