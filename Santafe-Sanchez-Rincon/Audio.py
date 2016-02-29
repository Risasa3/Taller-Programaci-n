#importar librerias que se requieren
import wave
import struct

#Constructor de la Clase
class audio1:

    #Codigo de la clase para generar el audio
    def __init__(self, frecuencia, bits, nombre):
        self.frecuencia = frecuencia
        self.bits = bits
        self.nombre = nombre
    #Metodo para generar audio
    def generar(self, datos):
        output = wave.open(self.nombre, 'w')
        P_Bits = self.bits/8
        output.setparams((1, P_Bits, self.frecuencia, 0, 'NONE', 'not compressed'))
        #Arreglo
        seno = []
        for i in range(0, len(datos)):

                packed_seno = struct.pack('<h', datos[i])

                seno.append(packed_seno)


        value_str = ''.join(seno)
        output.writeframes(value_str)
        output.close()

#Constructor de la Clase

class audio2: #autor: Laura Melisa Sanchez Trujillo

    #Codigo de la clase para generar el audio
    def __init__(self, frecuencia, bits, nombre):
        self.frecuencia = frecuencia
        self.bits = bits
        self.nombre = nombre
    #Metodo para generar audio
    def generar(self,datos):
        output = wave.open(self.nombre,"w")
        P_Bits = self.bits/8
        output.setparams((1, P_Bits, self.frecuencia, 0, 'NONE', 'not compressed'))
        #Arreglo
        triangulo = []
        for i in range (0, len(datos)):

            packed_triangulo = struct.pack('<h', datos[i])

            triangulo.append(packed_triangulo)

        value_str = ' '.join(triangulo)
        output.writeframes(value_str)
        output.close()

#Constructor de la Clase

class audio3: # Autor: Camila Santafe Beltran

    #Codigo de la clase para generar el audio
    def __init__(self, frecuencia, bits, nombre):
        self.frecuencia = frecuencia
        self.bits = bits
        self.nombre = nombre
    #Metodo para generar audio
    def generar(self,datos):
        output = wave.open(self.nombre,"w")
        P_Bits = self.bits/8
        output.setparams((1, P_Bits, self.frecuencia, 0, 'NONE', 'not compressed'))
        #Arreglo
        cuadrado = []
        for i in range (0, len(datos)):

            packed_cuadrado = struct.pack('<h', datos[i])

            cuadrado.append(packed_cuadrado)

        value_str = ' '.join(cuadrado)
        output.writeframes(value_str)
        output.close()

#Constructor de la Clase

class audio4: # Autor: Angie Paola Rincon Murcia

    #Codigo de la clase para generar el audio
    def __init__(self, frecuencia, bits, nombre):
        self.frecuencia = frecuencia
        self.bits = bits
        self.nombre = nombre
    #Metodo para generar audio
    def generar(self,datos):
        output = wave.open(self.nombre,"w")
        P_Bits = self.bits/8
        output.setparams((1, P_Bits, self.frecuencia, 0, 'NONE', 'not compressed'))
        #Arreglo
        sierra = []
        for i in range (0, len(datos)):

            packed_sierra = struct.pack('<h', datos[i])

            sierra.append(packed_sierra)

        value_str = ' '.join(sierra)
        output.writeframes(value_str)
        output.close()

