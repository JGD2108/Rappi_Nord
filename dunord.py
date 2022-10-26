from restaurantes import Cafe, Terrase
from domicilios import Domicilios
import sqlite3
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
        self.cafe= Cafe(Cafe.menuC)
        self.terrase = Terrase(Terrase.menuT)
        while True:
            print("Que menu desea cambiar?")
            opc= input("1. Cafe \t 2. Terrase: ")
            if opc=="1" or opc=="2":
                break
            else:
                print("Escoja una opcion valida")
        if opc=="1":
            cafe = sqlite3.connect("Cafe_menu.db")
            c = cafe.cursor() 
            opc1= input("1. Eliminar Elemento, 2. Añadir Elemento")
            if opc1=="1":
                print(self.cafe.menuC)
                Cambio = input("Digite el elemento a eliminar").title()
                c.execute('''SELECT * from MENU''')
                c.execute("DELETE FROM MENU WHERE item = ?", [Cambio])
                cafe.commit()
                for key in self.cafe.menuC:
                    if Cambio in key:
                        del self.cafe.menuC[key] ##Eliminar el cambio solicitado
                        break
                print(self.cafe.menuC) ## self.cafe.menuC por que no funciona? 
            else: 
                Cambio = input("Digite el elemento a añadir").title()
                try:
                    precio = input("Digite el precio del elemento")
                except ValueError:
                    print("Digite un numero valido")
                precio = float(precio)
                new = {Cambio: precio}
                self.cafe.menuC.update(new)
                data = [(Cambio,precio)]
                print(data)
                c.executemany("INSERT INTO MENU VALUES(?, ?)",data)
                cafe.commit()
                print(self.cafe.menuC)
        else:
            print(self.terrase.menuT)
            terrase = sqlite3.connect("Terrase_menu.db")
            c = terrase.cursor() 
            opc1= input("1. Eliminar Elmento, 2. Añadir Elemento")
            if opc1=="1":
                print(self.terrase.menuT)
                Cambio = input("Digite el elemento a eliminar").title()
                c.execute('''SELECT * from menu''')
                c.execute("DELETE FROM menu WHERE item = ?", [Cambio])
                terrase.commit()
                for key in self.terrase.menuT:
                    if Cambio in key:
                        del self.terrase.menuT[key] ##Eliminar el cambio solicitado
                        break
                print(self.terrase.menuT)
            else:
                Cambio = input("Digite el elemento a añadir").title()
                try:
                    precio = input("Digite el precio del elemento")
                except ValueError:
                    print("Digite un numero valido")
                precio = float(precio)
                new = {Cambio: precio}
                data = [(Cambio,precio)]
                c.executemany(" INSERT INTO menu VALUES(?,?)",data)
                terrase.commit()
                self.terrase.menuT.update(new)
        return self.cafe.menuC, self.terrase.menuT
    

        
        


    def disponibilidadR():
        pass

## En escoger domiciliario va de parametro domicilios para poder escoger el domiciliario y ver su disponibilidad

    def Escoger_Domiciliario():
        
        pass


    def proceso():
        print("Que desea realizar administrador?")
        try:
            opc= input("Escoja 1. Modificar Menu.")
        except ValueError:
            print("Escoja un numero")