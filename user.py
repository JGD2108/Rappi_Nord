from restaurantes import Cafe, Terrase
class User(Cafe,Terrase):
    def __init__(self, nombre: str, id: int, ubicacion: str, tel: int, carrito:list, total:float) -> None:
        self.nombre = nombre
        self.id = id
        self.ubicacion = ubicacion
        self.tel = tel
        self.carrito=[]
        self.total=total
        
    def pedido(self):
        Total=0
        Carrito=[]
        print("Escoja el restaurante a escoger")
        answer= input("1. Cafe, 2. Terrase")
        while(answer!="1" and answer!="2"):
            print("escoja 1 o 2")
            answer= input("1. Cafe '\t' 2. Terrase")
        if answer=="1":
            print("Digite stop cuando desee parar")
            while True:
                item=input("Item:").title()
                if item in Cafe.menuC:
                    Total+=Cafe.menuC[item]
                    Carrito.append(item)
                elif(item=="Stop"):
                    break
            print(f"Su total es: {Total}")
        elif(answer=="2"):
            print("Digite stop cuando desee parar")
            while True:
                item=input("Item:").title()
                if item in Terrase.menuT:
                    Total+=Terrase.menuT[item]
                    Carrito.append(item)
                elif(item=="Stop"):
                    break
            print(f"Su total es: {Total}")
            for a in Carrito:
                print (a)
        self.total=Total
        self.carrito=Carrito
        return self.carrito, self.total

    def pago(self):
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

    
    def __repr__(self) -> str:
        pass
