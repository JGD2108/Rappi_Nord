from restaurantes import Cafe, Terrase
from domicilios import Domicilios
import sqlite3

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
        ## Creación de los objetos 
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
            opc1= input("1. Eliminar Elemento, 2. Añadir Elemento")
            if opc1=="1":
                print("Recuerde que este es el menu:")
                print(self.cafe.menuC)
                Cambio = input("Digite el elemento a eliminar").title()
                Dunord.Eliminarsql(Dunord, 1, Cambio)
                for key in self.cafe.menuC:
                    if Cambio in key:
                        del self.cafe.menuC[key] ##Eliminar el cambio solicitado
                        break
                print("Así queda el Menu")
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
                Dunord.AñadirSql(self,1,data)
                print("Así queda el menu")
                print(self.cafe.menuC)
        else:
            opc1= input("1. Eliminar Elmento, 2. Añadir Elemento")
            if opc1=="1":
                print("Recuerde el menu")
                print(self.terrase.menuT)
                Cambio = input("Digite el elemento a eliminar").title()
                Dunord.Eliminarsql(Dunord, 2, Cambio)
                for key in self.terrase.menuT:
                    if Cambio in key:
                        del self.terrase.menuT[key] ##Eliminar el cambio solicitado
                        break
                print("Así queda el menu")
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
                Dunord.AñadirSql(Dunord,2,data)
                self.terrase.menuT.update(new)
        return self.cafe.menuC, self.terrase.menuT
    
        
    def Eliminarsql(self, opc:int, string:str):
        """
        Esta función ejecuta los comando necesarios para eliminar 
        un dato en específico de una fila de la base de datos
        """
        cafe = sqlite3.connect("Cafe_menu.db")
        terrase = sqlite3.connect("Terrase_menu.db")
        c = cafe.cursor()
        t = terrase.cursor()
        if opc==1:
            c.execute('''SELECT * from MENU''')
            c.execute("DELETE FROM MENU WHERE item = ?", [string])
            cafe.commit()
        elif opc==2:
            t.execute('''SELECT * from menu''')
            t.execute("DELETE FROM MENU WHERE item=?", [string])
            terrase.commit()

    def AñadirSql(self,opc:int, data):
        """
        Esta Función ejecuta los comando para añadir
        un nuevo producto a la base de datos
        """
        cafe = sqlite3.connect("Cafe_menu.db")
        terrase = sqlite3.connect("Terrase_menu.db")
        c = cafe.cursor()
        t = terrase.cursor()
        if opc==1:
            c.executemany(" INSERT INTO menu VALUES(?,?)",data)
            cafe.commit()
        elif opc==2:
            t.executemany(" INSERT INTO menu VALUES(?,?)",data)
            terrase.commit()

    def disponibilidadR():
        pass


    def Escoger_Domiciliario(self):
        pass


    def proceso():
        print("Que desea realizar administrador?")
        try:
            opc= input("Escoja 1. Modificar Menu.")
        except ValueError:
            print("Escoja un numero")