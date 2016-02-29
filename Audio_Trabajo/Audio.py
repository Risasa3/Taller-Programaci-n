#importar librerias necesarias
import math
import wave
import struct

#Variables iniciales

n = 16 # Profundidad en bits

Samplingrate = 44100 # Frecuencia de Muestreo

RangoDinamico = 20*math.log10(2**n) #Rango Dinamico

#Abrir archivo de audio
Archivo = wave.open ("/Users/angierincon/Downloads/American_Horror_Story__Murder_House_Title_Credits_Intro.wav", "rb" )

t1 = 1/Samplingrate
print("Audio: American Horror Story Murder House Title Credits Intro")
#Se obtiene el tamano del archivo
tamano = Archivo.getnframes()
print("Tamano:")
print (tamano)
tiempo = tamano/Samplingrate
print ("Tiempo:")
print(tiempo)

#Sumatoria de los cuadrados de cada valor
for i in range (1, tamano):
    Sumatoria1 = 1
    DatosArray = Archivo.readframes(1)
    Datos = struct.unpack("<i", DatosArray)
    Sumatoria = ((int(Datos[0])**2)*t1)
    Sumatoria1 = Sumatoria1 + i

    # Nivel continuio equivalente
    r =((1/tiempo)*(Sumatoria1))/2**n
    leq = 20*math.log10(r)
    print (leq)

#Valor Pico
Valorpico =	max(DatosArray)
ValorpicodBFS =	20*math.log10(float(Valorpico)/(2**n))
print(ValorpicodBFS)

#Valor RMS
ValorRms = math.sqrt(Sumatoria/tamano)
ValordBFS =	20*math.log10(ValorRms/RangoDinamico)
print (ValordBFS)

