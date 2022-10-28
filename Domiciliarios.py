import sqlite3
con = sqlite3.connect("Domiciliario.db")
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS RegDomi")
sql="""
    CREATE TABLE RegDomi(
        Name TEXT,
        ID INT,
        Cel INT
    )
"""

"""
Para meter datos en la base de datos: 
quitas el execute de Drop table if exists y  todo de ahí para abajo 
data = [
        ("Baja Taco", 4.00),
        ("Burrito", 7.50),
        ("Bowl", 8.50),
        ("Nachos", 11.00),
        ("Quesadilla", 8.50),
        ("Super Burrito", 8.50),
        ("Super Quesadilla", 9.50),
        ("Taco", 3.00),
        ("Tortilla Salad", 8.00) ]

cur.executemany("INSERT INTO MENU VALUES(?, ?)", data)
con.commit()
"""

cur.execute(sql)
con.commit()
con.close()