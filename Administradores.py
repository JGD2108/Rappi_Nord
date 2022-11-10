import sqlite3
con = sqlite3.connect("Register.db")
register = con.cursor()
data = [
        ("Admin1","Cafe"),
        ("Admin2","Terrase"),
         ]

register.executemany("INSERT INTO Admin VALUES(?, ?)", data)
con.commit()
con.close()