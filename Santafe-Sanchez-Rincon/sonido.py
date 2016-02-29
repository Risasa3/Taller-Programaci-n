#importar librerias que se requieren
import math
import matplotlib.pylab as plt

#Constructor de la Clase
class Onda1:
    #Arreglo
    array = []
    #Codigo de la clase para generar la senal
    def __init__(self, frec, time, bits, samplingrate, ampli):
        self.frecuencia = frec
        self.sampling = samplingrate
        self.samples = time * samplingrate
        self.amplitud = (2**bits)/2
        self.ampli=ampli
        self.bits = bits
        self.pi = math.pi
    #Metodo para generar los datos de la onda
    def generar(self):
        for i in range (0, self.samples):
            dato = self.amplitud*math.sin((2*self.pi*self.frecuencia*i)/self.sampling)
            valor = max(dato)
            amplitud1 = 20*math.log10(float(valor)/2**self.bits)
            r = ((valor)*(self.ampli-1))/amplitud1
            dato1 = r*math.sin((2*self.pi*self.frecuencia*i)/self.sampling)
            print dato1
            Onda1.array.append(dato1)
        return Onda1.array
    #Metodo para graficar
    def graficar(self, audio):
        plt.plot(audio, color="green", linewidth=1.0, linestyle="-")
        plt.show()

#constructor de la clase

class Onda2: # Autor: Laura Melisa Sanchez Trujillo

    #Arreglo
    triangulo = []
    #codigo de la clase para generar la senal
    def __init__(self, frec, time, bits, samplingrate, ampli):
        self.frecuencia=frec
        self.sampling = samplingrate
        self.samples = time * samplingrate
        self.amplitud = (2**bits)/100
        self.ampli = ampli
        self.bits = bits
        self.pi = math.pi
    #Metodo para generar los datos de la onda
    def generar(self):
        for m in range (0,self.samples,2):
            t = (8/(self.pi**2))*self.amplitud
            t1 = 0
            for k in range (1,100):
                triangular = (((-1)**((k-1)/2))/(k**2))*math.sin((2*self.pi*self.frecuencia*m*k)/self.sampling)
                t1 = t1 + triangular
            tt = t*t1
            valor = max(tt)
            amplitud1 = 20*math.log10(float(valor)/2**self.bits)
            g = ((valor)*(self.ampli-1))/amplitud1
            tt2 =  g*t1
            Onda2.triangulo.append(tt2)
        return Onda2.triangulo
    #Metodo para graficar
    def graficar(self, audio1):
        plt.plot(audio1, color="blue", linewidth=1.0, linestyle="-")
        plt.show()

#Constructor de la Clase

class Onda3: # Autor: Camila Santafe Beltran

    #Arreglo
    cuadrado = []
    #codigo de la clase para generar la senal
    def __init__(self, frec, time, bits, samplingrate, ampli):
        self.frecuencia=frec
        self.sampling = samplingrate
        self.samples = time * samplingrate
        self.amplitud = (2**bits)/100
        self.ampli = ampli
        self.bits = bits
        self.pi = math.pi
    #Metodo para generar los datos de la onda
    def generar(self):
        for s in range(0,self.samples,2):
            c = (4/self.pi)*self.amplitud
            c1 = 0
            for k in range (1,100):
                cuadro = (1/k)*math.sin((2*self.pi*self.frecuencia*s*k)/self.sampling)
                c1 = c1 + cuadro
            ct = c*c1
            valor = max(ct)
            amplitud1 = 20*math.log10(float(valor)/2**self.bits)
            m = ((valor)*(self.ampli-1))/amplitud1
            ct2 = m*c1
            Onda3.cuadrado.append(ct2)
        return Onda3.cuadrado
    def graficar(self, audio2):
        plt.plot(audio2, color="purple", linewidth=1.0, linestyle="-")
        plt.show()

#Constructor de la Clase

class Onda4: # Autor: Angie Paola Rincon Murcia

    #Arreglo
    sierra = []
    #codigo de la clase para generar la senal
    def __init__(self, frec, time, bits, samplingrate, ampli):
        self.frecuencia=frec
        self.sampling = samplingrate
        self.samples = time * samplingrate
        self.amplitud = (2**bits)/100
        self.ampli = ampli
        self.bits = bits
        self.pi = math.pi
    #Metodo para generar los datos de la onda
    def generar(self):
        for a in range(0,self.samples):
            s = (1/2-1/self.pi)*self.amplitud
            s1 = 0
            for k in range (1,100):
                serra = (1/k)*math.sin((2*self.pi*self.frecuencia*a*k)/self.sampling)
                s1 = s1 + serra
            st = s*s1
            valor = max(st)
            amplitud1 = 20*math.log10(float(valor)/2**self.bits)
            a = ((valor)*(amplitud1-1))/self.amplitud
            st2 = a*s1
            Onda4.sierra.append(st2)
        return Onda4.sierra
    #Metodo para graficar
    def graficar(self, audio3):
        plt.plot(audio3, color="red", linewidth=1.0, linestyle="-")
        plt.show()