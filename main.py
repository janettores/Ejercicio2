# Ejercicio 2

import csv
from Viajero import ViajeroFrecuente
from Menu import menu_1

if __name__ == '__main__':
    listaviajeros = []
    archivo = open('Viajeros.csv', 'r')
    reader = csv.reader(archivo, delimiter=',')
    for fila in reader:
        unviajero = ViajeroFrecuente(int(fila[0]), fila[1], fila[2], fila[3], int(fila[4]))
        listaviajeros.append(unviajero)
        print(unviajero)    #una forma de mostrar el objeto con los datos del archivo
    archivo.close()
    menu_1(listaviajeros)    #lista ya generada con las filas del archivo

    #for i in listaViajeros:  # otra forma de mostrar, muestra la lista cargada
      #listaViajeros[i]