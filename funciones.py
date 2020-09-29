import numpy as np
import matplotlib.pyplot as plt   

#comando para ver la grafica por separado: %matplotlib auto 

def grafica(x, funcion, titulo):
    plt.plot(x, funcion, "r")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.title(titulo, fontsize = 20, color = "blue")
    plt.grid(color='k', linestyle='-', linewidth=1)
    plt.show()
    

def escalon(x):
    a = []
    for i in range(len(x)):
        if x[i] >= 0:
            a.append(1)
        else:
            a.append(0)
    return a

def tramos(x):
    a = []
    for i in range(len(x)):
        if x[i] >= 1:
            a.append(1)
        elif x[i] <= 0:
            a.append(0)
        else:
            a.append(x[i])
    return a
        
def sigmoidal(x):
    return (np.e**(1*x))/(np.e**(1*x)+1)

def signo(x):
    a = []
    for i in range(len(x)):
        if x[i] == 0:
            a.append(0)
        elif x[i] > 0:
            a.append(1)
        else:
            a.append(-1)
    return a

def hiperbolica(x):
    return np.tanh(x)

def lineal(x):
    return 1*x

def gaussiana(x):
    return 1/np.e**(1*x**2)

def sinusoidal(x):
    return 1*np.sin(1*x+1)


x = np.linspace(-1, 1, 1000)

grafica(x, escalon(x), "Funcion escalon")

        
x = np.linspace(-2, 3, 1000)

grafica(x, tramos(x), "Funcion lineal a tramos")

        
x = np.linspace(-6, 6, 100)

grafica(x, sigmoidal(x), "Funcion sigmoidal")

        
x = np.linspace(-2, 2, 1000)

grafica(x, signo(x), "Funcion signo")

        
x = np.linspace(-4, 4, 100)

grafica(x, hiperbolica(x), "Funcion tangente hiperbolica")


x = np.linspace(0, 10, 10)

grafica(x, lineal(x), "Funcion lineal")


x = np.linspace(-5, 5, 100)

grafica(x, gaussiana(x), "Funcion gaussiana")


x = np.linspace(0, 10, 100)

grafica(x, sinusoidal(x), "Funcion sinusoidal")
