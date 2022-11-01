from abc import abstractmethod,ABCMeta
import json
from typing import Dict
class InternalState(metaclass= ABCMeta):
    @abstractmethod
    def changeState(self):
        pass
class Available(InternalState):
    def changeSate(self):
        print("Available Person")

class Occupied(InternalState):
    def changeSate(self):
        print("Occupied Person")

class Domiciliario:
    def __init__(self, nombreD: str, telD: int) -> None:
        self.nombreD = nombreD
        self.telD = telD
        self.state = None

    def setState(self,status):
        self.state=status

    def getState(self):
        return self.state
    
    def changeState(self):
        self.state.changeState()


class Flyweight():
    """
    The Flyweight stores a common portion of the state (also called intrinsic
    state) that belongs to multiple real business entities. The Flyweight
    accepts the rest of the state (extrinsic state, unique for each entity) via
    its method parameters.
    """
    def __init__(self, sharedState:str) -> None:
        self.sharedState = sharedState
    def operation(self, uniqueState:str) -> None:
        s = json.dumps(self._sharedState)
        u = json.dumps(uniqueState)
        

class FlyweightFactory():
    """
    The Flyweight Factory creates and manages the Flyweight objects. It ensures
    that flyweights are shared correctly. When the client requests a flyweight,
    the factory either returns an existing instance or creates a new one, if it
    doesn't exist yet.
    """
    _domiciliarios: Dict[str, Flyweight]={}

    def __init__(self, initialFlyweight: Dict) -> None:
        for state in initialFlyweight:
            self._domiciliarios[self.get_key(state)] = Flyweight(state)
    
    def get_key(self, state:Dict) -> None:
        return "_".join(sorted(state))

    def getFlyweight(self,shared_state:Dict) -> Flyweight:
        """
        Returns an existing Flyweight with a given state or creates a new one.
        """
        key = self.get_key(shared_state)

        if not self._domiciliarios(key):
            self._domiciliarios[key]= Flyweight(shared_state)
        
        return self._domiciliarios[key]
    
    def listFlyweights(self)->None:
        count = len(self._domiciliarios)

