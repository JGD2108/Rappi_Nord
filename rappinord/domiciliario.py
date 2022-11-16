from __future__ import annotations
from abc import ABC, abstractmethod
import sqlite3

class Domiciliario:
    def __init__(self, name: str, id: int, cel: int, state: str, Domi: list) -> None:
        self.Domi = Domi
        self.name = name
        self.id = id
        self.cel = cel
        self.state = state

    def disponibilidad(self):
        if self.state == "Available":
            pass

    def makeAvailable(self, key):
        x="Available"
        self.Domi[key] = x
        return self.Domi
    
    def makeOccupied(self, key):
        x="Occupied"
        self.Domi[key] = x
        return self.Domi

    con = sqlite3.connect("Domiciliario.db")
    cur = con.cursor()
    x=[]
    for row in cur.execute("SELECT NAME FROM Domiciliarios"): ##Seleccionar los nombres del sql
        str = ''
        for item in row:
            str = str + item
        x.append(str)
    Domi={}

    for i in range (len(x)):
            Name = x[i]
            new = {Name:"Occupied"}
            Domi.update(new)

class process():
    def execute():
        pass
