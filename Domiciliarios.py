import sqlite3
con = sqlite3.connect("Domiciliario.db")
cur = con.cursor()
###cur.execute("DROP TABLE IF EXISTS RegDomi")

data = [
        ("Jose David",1001915145, 3043774896),
        ("Cristian", 1001915145, 310554675),
         ]

cur.executemany("INSERT INTO RegDomi VALUES(?, ?, ?)", data)
con.commit()
"""

cur.execute(sql)
con.commit()
con.close()
"""