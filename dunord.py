from restaurantes import Cafe, Terrase
from domicilios import Domicilios
##comit

class Dunord():
    def __init__(self, terrase: Terrase, domicilios: Domicilios, cafe: Cafe) -> None:
        self.cafe = cafe
        self.terrase = terrase
        self.domicilios = domicilios

## A modificar menu se le pasan como atributo los objetos de terrase y cafe

    def modificarMenu(self):
        """
        Como sabemos que el menu es un diccionario utilizamos del, update etc..
        """
        while True:
            print("Que menu desea cambiar?")
            opc= input("1. Cafe \t 2. Terrase: ")
            if opc=="1" or opc=="2":
                break
            else:
                print("Escoja una opcion valida")
        if opc=="1":
            opc1= input("1. Eliminar Elmento, 2. Añadir Elemento")
            if opc1=="1":
                Cambio = input("Digite el elemento a eliminar").title()
                for key in Cafe.menuC:
                    if Cambio in key:
                        print(Cafe.menuC)
                        del Cafe.menuC[key] ##Eliminar el cambio solicitado
                        break
                print(Cafe.menuC) ## self.cafe.menuC por que no funciona? 
            else: 
                Cambio = input("Digite el elemento a añadir").title()
                try:
                    precio = input("Digite el precio del elemento")
                except ValueError:
                    print("Digite un numero valido")
                precio = float(precio)
                new = {Cambio: precio}
                Cafe.menuC.update(new)

                print(Cafe.menuC)
        else:
            opc1= input("1. Eliminar Elmento, 2. Añadir Elemento")
            if opc1=="1":
                Cambio = input("Digite el elemento a eliminar").title()
                for key in Terrase.menuT:
                    if Cambio in key:
                        print(Terrase.menuT)
                        del Terrase.menuT[key] ##Eliminar el cambio solicitado
                        break
                print(Terrase.menuT)
 



    def disponibilidadR():
        pass

## En escoger domiciliario va de parametro domicilios para poder escoger el domiciliario y ver su disponibilidad

    def Escoger_Domiciliario():
        pass
Dunord.modificarMenu(Dunord)