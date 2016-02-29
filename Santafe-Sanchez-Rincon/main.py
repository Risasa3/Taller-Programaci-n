#Importar librerias que son requeridas

from sonido import Onda1, Onda2, Onda3, Onda4
from Audio import audio1, audio2, audio3, audio4

def main():

    #Datos de entrada
    opc = input("Que funcion desea graficar:\n 1. Onda Sinusoidal \n 2. Onda Triangular \n 3. Onda Cuadrada \n 4. Onda Sierra \n 5. Salir \n")
    tono = input("ingrese la frecuencia que desea generar: ")
    duracion = input("ingrese el tiempo de duracion del audio: ")
    bitsample = input("ingrese la profundidad en bits del audio: ")
    frecuenciademuestreo = input("ingrese la frecuencia de muestreo: ")
    amplitud1 = input("Ingrese la amplitud de la onda")
    nombre = raw_input("Ingrese el nombre del archivo a generar: ")

    #Despliegue del menu

    if opc == 1:

        #Objeto de instancia clase Onda1 que genera datos
        Onda = Onda1(tono, duracion, bitsample, frecuenciademuestreo, amplitud1)
        #Genera arreglo de datos
        dato = Onda.generar()
        #Genera el audio del arreglo
        audio = audio1(frecuenciademuestreo, bitsample, nombre)
        audio.generar(dato)
        #Grafica
        Onda.graficar(dato)

    elif opc == 2: # Autor: Laura Melisa Sanchez Trujillo

        #Objeto de instancia clase Onda2 que genera datos
        Onda = Onda2(tono, duracion, bitsample, frecuenciademuestreo, amplitud1)
        #Genera arreglo de datos t1
        t1 = Onda.generar()
        #Genera el audio del arreglo
        audio = audio2(frecuenciademuestreo, bitsample, nombre)
        audio.generar(t1)
        #Grafica
        Onda.graficar(t1)

    elif opc == 3: # Autor: Camila Santafe Beltran

        #Objeto de instancia clase Onda3 que genera datos
        Onda = Onda3(tono, duracion, bitsample, frecuenciademuestreo, amplitud1)
        #Genera arreglo de datos c1
        c1 = Onda.generar()
        #Genera el audio del arreglo
        audio = audio3(frecuenciademuestreo, bitsample, nombre)
        audio.generar(c1)
        #Grafica
        Onda.graficar(c1)

    elif opc == 4: # Autor: Angie Paola Rincon Murcia

        #Objeto de instancia clase Onda4 que genera datos
        Onda = Onda4(tono, duracion, bitsample, frecuenciademuestreo, amplitud1)
        #Genera arreglo de datos s1
        s1 = Onda.generar()
        #Genera el audio del arreglo
        audio = audio4(frecuenciademuestreo, bitsample, nombre)
        audio.generar(s1)
        #Grafica
        Onda.graficar(s1)
    else:
        print "Salir"

if __name__=="__main__":
    main()
