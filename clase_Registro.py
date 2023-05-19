import csv
import os
import datetime

class Registro:
    __temperatura = 0
    __humedad = 0
    __presion = 0

    def __init__(self,temp,humedad,presion):
        self.__temperatura = temp
        self.__humedad = humedad
        self.__presion = presion
    
    def getTemperatura(self):
        return self.__temperatura
    def getHumedad(self):
        return self.__humedad
    def getPresion(self):
        return self.__presion

class ManejadorRegistro:
    __listaregistro = []
    def __init__(self):
        self.__listaregistro =[[None for columna in range(2)]for fila in range(2)]
    def cargaarchivo (self):
        archivo=('Ejercicio 3\Datos3.csv')
        for fila in range(2):
            for columna in range(2):
                print ("Ingrese datos del día "+str(fila+1))
                print ("Ingrese datos de la hora "+ str(datetime.time(columna)))
                temp=float(input("Ingrese la temperatura actual "))
                humed=float(input("Ingrese la humedad actual "))
                pres=float(input("Ingrese la presión actual "))
                registroaux=Registro(temp,humed,pres)
                self.__listaregistro[fila][columna]=registroaux
                os.system('cls')
            i=0
        os.system('cls')
        with open (archivo, 'w', newline='') as archivo_csv:
                escritor_csv = csv.writer(archivo_csv, delimiter=';')
                for fila in self.__listaregistro:
                    j=0
                    for columna in fila:
                        escritor_csv.writerow([i+1,datetime.time(j),columna.getTemperatura(),columna.getHumedad(),columna.getPresion()])
                        j+=1
                    i+=1

    def mayormenor (self):
        mayortemp=0.0
        diahoramaytemp=[0,'']
        menortemp=999.9
        diahoramentemp=[0,'']
        mayorhum=0.0
        diahoramayhum=[0,'']
        menorhum=999.9
        diahoramenhum=[0,'']
        mayorpres=0.0
        diahoramaypres=[0,'']
        menorpres=999.9
        diahoramenpres=[0,'']
        d=0
        for fila in self.__listaregistro:
            i=0
            for columna in fila:
                if columna.getTemperatura()>mayortemp:
                    mayortemp=columna.getTemperatura()
                    diahoramaytemp=[d+1,datetime.time(i)]
                if columna.getTemperatura()<menortemp:
                    menortemp=columna.getTemperatura()
                    diahoramentemp=[d+1,datetime.time(i)]
                if columna.getHumedad()>mayorhum:
                    mayorhum=columna.getHumedad()
                    diahoramayhum=[d+1,datetime.time(i)]
                if columna.getHumedad()<menorhum:
                    menorhum=columna.getHumedad()
                    diahoramenhum=[d+1,datetime.time(i)]
                if columna.getPresion()>mayorpres:
                    mayorpres=columna.getPresion()
                    diahoramaypres=[d+1,datetime.time(i)]
                if columna.getPresion()<menorpres:
                    menorpres=columna.getPresion()
                    diahoramenpres=[d+1,datetime.time(i)]
                i+=1
            d+=1
        print ('Mayor temperatura: \nDia: '+str(diahoramaytemp[0]),"Hora:",diahoramaytemp[1])
        print ('Menor temperatura: \nDia: '+str(diahoramentemp[0]),"Hora:",diahoramentemp[1])

        print ('Mayor humedad: \nDia: '+str(diahoramayhum[0]),"Hora:",diahoramayhum[1])
        print ('Menor humedad: \nDia: '+str(diahoramenhum[0]),"Hora:",diahoramenhum[1])

        print ('Mayor presión: \nDia: '+str(diahoramaypres[0]),"Hora:",diahoramaypres[1])
        print ('Menor presión: \nDia: '+str(diahoramenpres[0]),"Hora:",diahoramenpres[1])
        aux=input()

    def temppromedio(self):
        promtemp=[0.0]*24
        d=0
        for fila in self.__listaregistro:
            i=0
            for columna in fila:
                promtemp[i]+=columna.getTemperatura()
                i+=1
            d+=1
        j=0
        for hora in promtemp:
            print ('El promedio de la hora',datetime.time(j),'del mes es: \n'+str((hora/d)))
            j+=1
        aux=input()

    def listarvalores (self):
        dia=int(input("Ingrese el día: "))
        resultado=self.__listaregistro[dia-1]
        for indice, instancia in enumerate(resultado):
            print ("Hora       Temperatura     Humedad     Presion")
            print(datetime.time(indice),"       ",instancia.getTemperatura(),"       ",instancia.getHumedad(),"      ",instancia.getPresion())
        aux=input()