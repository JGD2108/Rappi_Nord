from rappinord.domiciliario import Domiciliario
import sqlite3

con = sqlite3.connect("Domiciliario.db")
cur = con.cursor()


class Domicilios():
    def __init__(self, domiciliario: Domiciliario) -> None:
        self.domiciliario = domiciliario

    def get_infoD(ID):
        statement = (f"SELECT * FROM Domiciliario where User = '{ID}'")
        cur.execute(statement)
        record = cur.fetchone()
        nombre = record[0]
        id = record[1]
        cel = record[2]
        state = record[3]
        Domis = Domiciliario(nombre, id, cel, state)
        Domis.disponibilidad()

    def get_pedido():
        state = "Pendiente"
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
        if opc == 0:
            statement = (f"INSERT INTO Pedidos(Estado) VALUES('Entregando') where Name ='{nombre}'")
            cur.execute(statement)
            cur.fetchone
            con.commit()
        elif opc == 1:
            statement = (f"DELETE FROM Domiciliario where Name = '{nombre}'")
            cur.execute(statement)
            cur.fetchone
            con.commit()

    def process():
        Domicilios.get_infoD()
