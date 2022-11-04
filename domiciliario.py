from __future__ import annotations
from abc import ABC, abstractmethod
import sqlite3
class Domiciliario:
    _state = None
    con = sqlite3.connect("Domiciliario.db")
    cur = con.cursor()
    x=[]
    for row in cur.execute("SELECT NAME FROM RegDomi"):
        str = ''
        for item in row:
            str = str + item
        x.append(str)
    Domi={}
    for i in range (len(x)):
            Name = x[i]
            new = {Name:"Available"}
            Domi.update(new)
    def __init__(self, Domi:dict, state:State) -> None:
        self.Domi = Domi
        self.setDomi(state)
    
    def setDomi(self, state:State):
        self._state = state
        self._state.domiciliario = self
    
    def presentState(self):
        print(f"Domiciliario esta en {type(self._state).__name__}")
    
    def makeAvailable(self, key):
        self._state.makeAvailable()
        x="Available"
        self.Domi[key] = x
        return self.Domi

    
    def makeOccupied(self,key):
        self._state.makeOccupied()
        x="Occupied"
        self.Domi[key] = x
        return self.Domi
    

class State(ABC):
    @property
    def domiciliario(self)->Domiciliario:
        return self._domiciliario

    @domiciliario.setter
    def domiciliario(self, domiciliario:Domiciliario)->None:
        self._domiciliario = domiciliario
    
    @abstractmethod
    def makeAvailable(self)->None:
        pass

    @abstractmethod
    def makeOccupied(self)->None:
        pass

class Available(State):
    def makeAvailable(self) -> None:
        print("Already available")
    
    def makeOccupied(self) -> None:
        self.domiciliario.setDomi(Ocuppied())

class Ocuppied(State):
    def makeAvailable(self) -> None:
        self.domiciliario.setDomi(Available())
     
    def makeOccupied(self) -> None:
        print("Already Occupied")

class Estado():
    def __init__(self, Dom:Domiciliario) -> None:
        self.Dom = Dom
    def makeOcupado(self):
        myDom = Domiciliario(self.Dom.Domi,Available())
        while True:
            for key,value in self.Dom.Domi.items():
                if value=="Available":
                    myDom.makeOccupied(key)
                    print(self.Dom.Domi)
                    break
            break
        return self.Dom.Domi
    def makeDisponible(self):
        myDom = Domiciliario(self.Dom.Domi, Ocuppied())
        while True:
            for key,value in self.Dom.Domi.items():
                if value=="Occupied":
                    myDom.makeAvailable(key)
                    print(self.Dom.Domi)
                    break
            break
        return self.Dom.Domi

