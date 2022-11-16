from rappinord.domicilios import Domicilios


class Domiciliario:
    def __init__(self, name: str, id: int, cel: int, state: str, Domi: list) -> None:
        self.Domi = Domi
        self.name = name
        self.id = id
        self.cel = cel
        self.state = state

    def disponibilidad(self):
        if self.state == "Available":
            list = Domicilios.get_pedido()
            print(f"El pedido a entregar es: {list}")
            name = list[0]
            Domiciliario.realizar_domicilio(name)
        else:
            print("No puede hacer más de un domicilio a la vez")

    def realizar_domicilio(nombre: str):
        print(f"Pedido entregado a {nombre}?")
        opc = int(input("1. Si"))
        Domicilios.estado_pedido(opc, nombre)


class process():
    def execute():
        pass
