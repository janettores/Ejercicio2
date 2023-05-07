class ViajeroFrecuente:
    __num_viajero = 0
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas_acum = 0

    def __init__(self, num_viajero=0, dni='', nombre='', apellido='', millas_acum=0):
        self.__num_viajero = num_viajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas_acum

    def __str__(self) -> str:
        return f'[Numero de viajero: {self.__num_viajero}, DNI: {self.__dni}, Nombre: {self.__nombre}, Apellido: {self.__apellido}, Millas acumuladas: {self.__millas_acum}]'

    def getNumViajero(self):
        return self.__num_viajero

    def cantidadTotaldeMillas(self):   #get devuelve (se asemeja a lectura en el archivo)
        return self.__millas_acum

    def acumularMillas(self, millas):    #set modifica (se asemeja a escritura en el archivo)
        self.__millas_acum += millas
        if millas <= self.__millas_acum:
            return self.__millas_acum
        else: print('\nError en la operación. Ingrese nuevamente\n')

    def canjearMillas (self, millas):   #set modifica
        self.__millas_acum -= millas
        return self.__millas_acum
