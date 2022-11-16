
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

class process():
    def execute():
        pass
