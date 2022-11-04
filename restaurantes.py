import sqlite3
class Cafe:
    menuC={}
    cafe = sqlite3.connect("Cafe_menu.db")
    cur = cafe.cursor()
    x=[]
    for row in cur.execute("SELECT item FROM menu"):
        str = ''
        for item in row:
            str = str + item
        x.append(str)
    z=[]
    for row in cur.execute("SELECT Price FROM menu"):
        Price=''
        for item in row:
            z.append(item)
    menuC={}
    for i in range (len(x)):
        item = x[i]
        Price = z[i]
        new = {item:Price}
        menuC.update(new)
    def __init__(self, menuC: dict) -> None:
        self.menuC = menuC
        print(self.menuC)
    def escribir(self):
        print(self.menuC)
        
class Terrase:
    menuT={}
    terrase = sqlite3.connect("Terrase_menu.db")
    cur = terrase.cursor()
    x=[]
    for row in cur.execute("SELECT item FROM menu"):
        str = ''
        for item in row:
            str = str + item
        x.append(str)
    z=[]
    for row in cur.execute("SELECT Price FROM menu"):
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
    def escribir(self):
        print(self.menuT)