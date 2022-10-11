from restaurantes import Cafe, Terrase
class User(Cafe,Terrase):
    def __init__(self, nombre: str, id: int, ubicacion: str, tel: int, carrito:list,Total:int) -> None:
        self.nombre = nombre
        self.id = id
        self.ubicacion = ubicacion
        self.tel = tel
        
    def pedido(self,Total):
        carrito=[]
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
                    carrito.append(item)
                elif(item=="Stop"):
                    break
            print(f"Su total es: {Total}")
        elif(answer=="2"):
            print("Digite stop cuando desee parar")
            while True:
                item=input("Item:").title()
                if item in Terrase.menuT:
                    Total+=Terrase.menuT[item]
                    carrito.append(item)
                elif(item=="Stop"):
                    break
            print(f"Su total es: {Total}")
            for a in carrito:
                print (a)
        return Total,carrito

    def pago(self):
            print("Digite con que desea pagar")
            while True:
                print("1. Datafono")
                print("2. Efectivo")
                opc=input()
                if opc=="1" or opc=="2":
                    break
            if opc=="1":
                pass
    
    def __repr__(self) -> str:
        pass
