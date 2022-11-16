import sqlite3
con = sqlite3.connect("Domiciliario.db")
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS Pedidos")
sql= """CREATE TABLE IF NOT EXISTS Pedidos(
        Name TEXT,
        Pedido TEXT,
        Total FLOAT,
        Ubicacion TEXT,
        Cel TEXT, 
        Estado TEXT
        )"""

cur.execute(sql)
con.commit()
con.close()