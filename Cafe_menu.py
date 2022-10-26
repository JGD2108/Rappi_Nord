import sqlite3
con = sqlite3.connect("Cafe_menu.db")
cur = con.cursor()
"""
cur.execute("DROP TABLE IF EXISTS menu")
sql="""##CREATE TABLE MENU(
        ##item TEXT,
        ##Price INT
##)"""


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
"""