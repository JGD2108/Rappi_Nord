from __future__ import annotations
from abc import ABC, abstractmethod
import sqlite3

class Domiciliario:
    def __init__(self) -> None:
        self.occupied_state = OcuppiedState()
        self.available_state = AvailableState()
        
        self.state = self.occupied_state
    
    def set_state(self, state: State):
        self.state = state

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
            new = {Name:"Available"}
            Domi.update(new)

    def presentState(self):
        print(f"Domiciliario esta en {type(self.state).__name__}")
    
    def makeAvailable(self, key):
        self.state.available
        x="Available"
        self.Domi[key] = x
        return self.Domi

    def makeOccupied(self,key):
        self.state.occupied
        x="Occupied"
        self.Domi[key] = x
        return self.Domi
    

class State():
    def makeOcuppied(self):
        raise NotImplementedError

    def makeAvailable(self):
        raise NotImplementedError

class OcuppiedState(State):
    def __init__(self, context: Domiciliario) -> None:
        self.context = context
    
    def available(self):
        self.context.set_state(self.context.available_state)
        print("Estás disponible para hacer domicilios")

    def occupied(self):
        print("No te encuentras disponible para hacer domicilios")

class AvailableState(State):
    def __init__(self, context: Domiciliario):
        self.context = context

    def occupied(self):
        self.context.set_state(self.context.occupied_state)
        print("No puedes hacer domicilios")

    def available(self):
        print("Actualemente ya te encuentras disponible para hacer domicilios")
    
