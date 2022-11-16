from rappinord.domiciliario import Domiciliario
import sqlite3

con = sqlite3.connect("Domiciliarios.db")
cur = con.cursor()

class Domicilios():
    def __init__(self, domiciliario: Domiciliario) -> None:
        self.domiciliario = domiciliario

    def get_infoD(ID):
        statement = (f"SELECT * FROM Domiciliarios where User = '{ID}'")
        cur.execute(statement)
        record = cur.fetchone()
        nombre = record[0]
        id = record[1]
        cel = record[2]
        state = record[3]
        Domis = Domiciliario(nombre, id, cel, state)
        Domis.disponibilidad()

    def process():
        Domicilios.get_infoD()

        
        