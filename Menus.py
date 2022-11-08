import sqlite3
con = sqlite3.connect("Menus.db")
cur = con.cursor()
data =[("Baja Taco", 4.00),
        ("Burrito", 7.50),
        ("Bowl", 8.50),
        ("Nachos", 11.00),
        ("Quesadilla", 8.50),
        ("Super Burrito", 8.50),
        ("Super Quesadilla", 9.50),
        ("Taco", 3.00),
        ("Tortilla Salad", 8.00)]
cur.executemany("INSERT INTO Cafe VALUES(?,?)",data)
cur.executemany("INSERT INTO Terrase VALUES(?,?)",data)
con.commit()
con.close()
