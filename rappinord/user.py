from rappinord.restaurantes import Cafe, Terrase
import sqlite3
class User(Cafe,Terrase):
    def __init__(self, nombre: str, id: int, tel: int, carrito: list, total: int, ubicacion: str) -> None:
        self.nombre = nombre
        self.id = id
        self.tel = tel
        self.carrito = carrito
        self.total = total
        self.ubicacion = ubicacion
        
    def pedido(self):
        """
        Esta funcion va a calcular según el restaurante cuanto es el total de lo que desea el usuario
        """
        Total=0
        Carrito=[]
        print("Escoja el menú del restaurante a pedir: ")
        answer= input("1. Cafe; 2. Terrase: ")
        x=[]
        while(answer!="1" and answer!="2"):
            print("escoja 1 o 2")
            answer= input("1. Cafe; 2. Terrase: ")
        if answer=="1":
            print("Digite stop cuando desee parar")
            while True:
                item=input("Item: ").title()
                if item in Cafe.menuC:
                    Total+=Cafe.menuC[item]
                    x.append(item)
                elif(item=="Stop"):
                    break
            Carrito.append(x)
        elif(answer=="2"):
            print("Digite stop cuando desee parar")
            while True:
                item=input("Item: ").title()
                if item in Terrase.menuT:
                    Total+=Terrase.menuT[item]
                    x.append(item)
                elif(item=="Stop"):
                    break
            Carrito.append(x)
            
        Ubicacion = input("Digite su ubicación detallada: ")
        for a in Carrito:
            print (a)
        print(f"Su total es: {Total}")

        caracter = ", "
        self.total = Total
        self.carrito = caracter.join(map(str, Carrito))
        print(self.carrito)
        self.ubicacion = Ubicacion


    def pago(self): 
        """
        Decidimos meter en la lista del carrito con que metodo van a pagar para ver
        Con que metodo desea pagar
        """
        print("Digite con que desea pagar: ")
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

    def Pedido(self):
        """
        Esta función va a formalizar el pedido, 
        lo insertará en la base de datos pedidos
        """
        conection= sqlite3.connect("Domiciliario.db")
        pedido = conection.cursor()
        data =[(self.nombre, self.carrito, self.total, self.ubicacion, self.tel)]
        pedido.executemany("INSERT INTO Pedidos VALUES(?,?,?,?,?)", data)
        conection.commit()
        conection.close()

    def proceso():
        User.pedido(User)

    def __repr__(self) -> str:
        pass