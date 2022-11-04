from domiciliario import Domiciliario
from domiciliario import Hola
from user import User

class Domicilios(User):
    def __init__(self, domiciliario: Domiciliario ) -> None:
        self.domiciliario = domiciliario
        
        