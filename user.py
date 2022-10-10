from restaurantes import Cafe, Terrase
class User(Cafe):
    def __init__(self, nombre: str, id: int, ubicacion: str, tel: int) -> None:
        self.nombre = nombre
        self.id = id
        self.ubicacion = ubicacion
        self.tel = tel
        
    def pago():
            pass

    def pedido(self):
            print("Escoja el restaurante a escoger")
            answer= input("1. Cafe, 2. Terrase")
            while(answer!="1" and answer!="2"):
                print("escoja 1 o 2")
                answer= input("1. Cafe '\t' 2. Terrase")
            if answer=="1":
                total=0
                while True:
                    item=input("Item:").title()
                    if item in Cafe.menuC:
                        total+=Cafe.menuC[item]
                        print("Total:$",end="")
                        print("{:.2f}".format(total))
                    elif(item=="Stop"):
                        break
    
    def __repr__(self) -> str:
        pass
