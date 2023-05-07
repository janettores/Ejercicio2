def buscarsinbandera(num, lista):
    indice = 0
    valorRetorno = -1
    print(lista[indice].getNumViajero())
    while indice < len(lista) & (lista[indice].getNumViajero() != num):
        indice += 1
        print('Entro')
        valorRetorno = indice
    return valorRetorno
def menu_1(lista):
    num = int(input('Ingrese un numero de viajero:\n'))
    posicion = buscarsinbandera(num, lista)
    opcion = ''   #se inicializa en vacio porque debo hacer que exista por mas que esté vacío
    if posicion != -1:

        while opcion != '0':
            opcion = (input('\nA- Consultar cantidad de millas\nB-Acumular millas\nC-Canjear millas\n0-Finalizar\n'))
            if opcion.upper() == 'A':
                print(f'El viajero numero {lista[posicion].getNumViajero()} tiene una cantidad de millas: {lista[posicion].cantidadTotaldeMillas()}')

            elif opcion.upper() == 'B':
                cantMillas = int(input('Ingrese la cantidad de millas a acumular:'))
                print(f'la cantidad de millas que posee el viajero actualmente es: {lista[posicion].acumularMillas(cantMillas)}')

            elif opcion.upper() == 'C':
                millascanje= int(input('Ingrese la cantidad de millas a canjear:'))
                print(f'La cantidad de millas que posee el viajero actualmente es: {lista[posicion].canjearMillas(millascanje)}')

    else:
        print('No se encontro el viajero. Ingrese nuevamente\n')