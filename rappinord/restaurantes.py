import sqlite3

class Cafe:
    menuC={}
    cafe = sqlite3.connect("Menus.db")
    cur = cafe.cursor()
    x=[]

    for row in cur.execute("SELECT Item FROM Cafe"):
        str = ''
        for item in row:
            str = str + item
        x.append(str)
    z=[]

    for row in cur.execute("SELECT Price FROM Cafe"):
        Price=''
        for item in row:
            z.append(item)
            
    for i in range (len(x)):
        item = x[i]
        Price = z[i]
        new = {item:Price}
        menuC.update(new)
    def __init__(self, menuC: dict) -> None:
        self.menuC = menuC
        
class Terrase:
    menuT={}
    terrase = sqlite3.connect("Menus.db")
    cur = terrase.cursor()
    x=[]

    for row in cur.execute("SELECT Item FROM Terrase"):
        str = ''
        for item in row:
            str = str + item
        x.append(str)
    z=[]

    for row in cur.execute("SELECT Price FROM Terrase"):
        Price=''
        for item in row:
            z.append(item)

    for i in range (len(x)):
        item = x[i]
        Price = z[i]
        print(item)
        print(Price)
        new = {item:Price}
        menuT.update(new)

    def __init__(self, menuT: dict) -> None:
        self.menuT = menuT