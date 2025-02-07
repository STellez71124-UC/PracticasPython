import numpy as np #Calculo de operaciones matematicas y factor aleatorio
import matplotlib.pyplot as plt #Creación de gráfica de Galton

canicas = 3000 #Cantidad de objetos
niveles = 12 #Cantidad de niveles
probabilidad = 0.5 #Probabilidad de ir a la izquierda
ruta=abs(1-probabilidad) #Probabilidad de ir a la derecha
resultado=np.empty(canicas) #Espacio para almacenar probabilidades

def grafica_galton(i): #Grafica de Galton
    plt.figure(facecolor='orange')
    plt.grid(True)
    plt.title('Simulación de la Máquina de Galton')
    plt.xlabel('Distribución de Canicas')
    plt.ylabel('Cantidad de Canicas')
    plt.hist(i)
    plt.show() #Muestra de grafica generada


def operacion_canicas():
    for x in range (canicas): #Rango de operacion en base a cantidad de objetos
        container = 0.0 #contenedor vacio de objetos
        for calculo in range (niveles): #Rango de operacion en base a niveles establecidos
            calculo = np.random.uniform(0.0,1.0) #Asignacion de numero aleatorio
            if (calculo > probabilidad and calculo < 1.0): #Colocacion en contenedores ubicados a la derecha
                container = container+1.0
        resultado[x] = container #Asignacion de contenedor utilizado

    return resultado
    
operacion_canicas() #Llamada a funcion matematica automatizada
grafica_galton(resultado) #Llamada a funcion grafica con resultados de funcion previamente utilizada