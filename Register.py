import sqlite3
con = sqlite3.connect("Register.db")
register = con.cursor()
administrador = [("Jg2108", "1001915145", "Jose", "3043774896", "1001915145"),
                ("CFV123","200162691", "Cristian", "3109876543", "1042849073"),]
register.executemany("INSERT INTO Users VALUES(?,?,?,?,?)",administrador)
con.commit()
con.close()