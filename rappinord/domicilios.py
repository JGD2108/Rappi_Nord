import sqlite3

con = sqlite3.connect("Domiciliario.db")
cur = con.cursor()

class Domiciliario:
    def __init__(self, name: str, id: int, cel: int, state: str) -> None:
        self.name = name
        self.id = id
        self.cel = cel
        self.state = state

    def disponibilidad(self,Domis):
        """
        Cambiar a occupied domiciliario 
        Verificar disponibilidad
        """
        if self.state == "Available":
            list = Domicilios.get_pedido()
            print(f"El pedido a entregar es: {list}")
            name = list[0]
            cur.execute(f"UPDATE Domiciliarios SET Estado = 'Occupied' WHERE Name = '{Domis.name}' ")
            con.commit()
            Domiciliario.realizar_domicilio(Domiciliario,name,Domis)
        else:
            print("No puede hacer más de un domicilio a la vez")

    def realizar_domicilio(self,nombre: str,Domis):
        """
        Cambiar a disponible una vez el domicilio este terminado
        """
        print(f"Pedido entregado a {nombre}?")
        opc = input("1. Si")
        opc = int(opc)
        cur.execute(f"UPDATE Domiciliarios SET Estado = 'Available' WHERE Name = '{Domis.name}' ")
        con.commit()
        Domicilios.estado_pedido(opc, nombre)


class Domicilios():

    def get_infoD(ID):
        """
        Obtención de información del domiciliario 
        dela base de datos para crear el objeto
        """
        statement = (f"SELECT * FROM Domiciliarios where ID = '{ID}'")
        cur.execute(statement)
        record = cur.fetchone()
        nombre = record[0]
        id = record[1]
        cel = record[2]
        state = record[3]
        Domis = Domiciliario(nombre, id, cel, state)
        Domis.disponibilidad(Domis)

    def get_pedido():
        """
        Tomar el pedido de la bd
        """
        state = "Pendientes"
        statement = (f"SELECT * FROM Pedidos where Estado = '{state}'")
        cur.execute(statement)
        record = cur.fetchone()
        nombre = record[0]
        pedido = record[1]
        total = record[2]
        ubicacion = record[3]
        cel = record[4]
        estado = record[5]
        Domicilios.estado_pedido(0, nombre)
        x = [nombre, pedido, total, ubicacion, cel, estado]
        return x

    def estado_pedido(opc:int, nombre:str):
        """
        Cambiar el estado del pedido
        """
        if opc == 0:
            cur.execute(f"UPDATE Pedidos SET Estado = 'Entregando' WHERE Name = '{nombre}' ")
            con.commit()
        else:
            statement = (f"DELETE FROM Pedidos WHERE Name = '{nombre}'")
            cur.execute(statement)
            cur.fetchone
            con.commit()
        

    def process():
        Domicilios.get_infoD()
