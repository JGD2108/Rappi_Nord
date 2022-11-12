from rappinord.restaurantes import Cafe, Terrase
from rappinord.dunord import Dunord
import sqlite3
class User(Cafe,Terrase):
    def __init__(self, nombre: str, id: int, tel: int, carrito:list, total:float) -> None:
        self.nombre = nombre
        self.id = id
        self.tel = tel
        self.carrito=[]
        self.total=total
        
    def pedido(self):
        """
        Esta funcion va a calcular según el restaurante cuanto es el total de lo que desea el usuario
        """
        Total=0
        Carrito=[]
        print("Escoja el menú del restaurante a pedir: ")
        answer= input("1. Cafe, 2. Terrase")
        x=[]
        while(answer!="1" and answer!="2"):
            print("escoja 1 o 2")
            answer= input("1. Cafe '\t' 2. Terrase")
        if answer=="1":
            print("Digite stop cuando desee parar")
            while True:
                item=input("Item:").title()
                if item in Cafe.menuC:
                    Total+=Cafe.menuC[item]
                    x.append(item)
                elif(item=="Stop"):
                    break
            print(f"Su total es: {Total}")
            Carrito.append(x)
            Carrito.append(Total)
            for a in Carrito:
                print (a)
        elif(answer=="2"):
            print("Digite stop cuando desee parar")
            while True:
                item=input("Item:").title()
                if item in Terrase.menuT:
                    Total+=Terrase.menuT[item]
                    x.append(item)
                elif(item=="Stop"):
                    break
            print(f"Su total es: {Total}")
            Carrito.append(x)

            for a in Carrito:
                print (a)
        self.total=Total
        self.carrito=Carrito
        return self.carrito, self.total

    def pago(self): 
        """
        Decidimos meter en la lista del carrito con que metodo van a pagar para ver
        Con que metodo desea pagar
        """
        print("Digite con que desea pagar")
        while True:
            opc=input("1. Datafono \t 2. Efectivo: " )
            if opc=="1" or opc=="2":
                break
        if opc=="1":
            print(f"Su total es de: {self.total}")
            self.carrito.append("Datafono")
        else:
            print(f"Su total es de: {self.total}")
            self.carrito.append("Efectivo")
        print(self.carrito)
        return self.carrito
    
    def Ubicacion(self):
        """
        Esta Función le pedira al usuario que digite 
        su ubicación
        """
        location = input("Digite su ubicación")
        return location

    def Pedido(self):
        """
        Esta función va a formalizar el pedido, 
        lo insertará en la base de datos pedidos
        """
        conection= sqlite3.connect("Domiciliario.db")
        pedido = conection.cursor()
        data =[(self.nombre, User.proceso(), self.total, User.Ubicacion(), self.tel)]
        pedido.executemany("INSERT INTO Pedidos VALUES(?,?,?,?,?)", data)
        conection.commit()
        conection.close()

    def proceso():
        User.pedido(User)

    def __repr__(self) -> str:
        pass