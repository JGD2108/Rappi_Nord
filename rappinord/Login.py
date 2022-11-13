import sqlite3
import stdiomask
from rappinord.Users import Register
from rappinord.user import User
from rappinord.dunord import proceso
con = sqlite3.connect("Register.db")
cur = con.cursor()

class Login():
    def compareUser():
        ## Vamos a tener 2 tablas una de usuarios y otra de administrador, dependiendo de
        ## lo que el usuario escoja se busca en la tabla
        Usuario = input("Digite su usuario: ")
        Password = stdiomask.getpass("Password: ")
        statement = (f"SELECT User from Users WHERE User = '{Usuario}' AND Password = '{Password}'")
        cur.execute(statement)
        if not cur.fetchone():  # An empty result evaluates to False.
            print("Login failed")
        else:
            print("Welcome", Usuario)
            Login.getInfo(Usuario)

    def compareAdmin():
        Usuario = input("Digite su usuario: ")
        Password = stdiomask.getpass("Password: ")
        statement = (f"SELECT User from Admin WHERE User = '{Usuario}' AND Password = '{Password}'")
        cur.execute(statement)
        if not cur.fetchone():  # An empty result evaluates to False.
            print("Login failed")
        else:
            print("Welcome", Usuario)
            proceso.execute()

    def compareDomiciliario():
        ID = input("Digite su ID: ")
        Password = stdiomask.getpass("Password: ")
        statement = (f"SELECT ID from Domiciliario WHERE ID = '{ID}' AND Password = '{Password}'")
        cur.execute(statement)
        if not cur.fetchone():
            print("Login failed")
        else:
            print("Welcome")
 
    def getInfo(Usuario: str):
        statement = (f"SELECT * FROM Users where User = '{Usuario}'")
        cur.execute(statement)
        record = cur.fetchone()
        nombre = record[2]
        cel = record[3]
        id = record[4]
        x = ""
        total = 0
        ubicacion = ""
        user = User(nombre ,id ,cel ,x , total, ubicacion)
        user.Proceso()

    def execute():
        opc1= int(input("1.Login; 2.Register: "))
        if opc1 == 1:
            while True:
                opc = int(input("1. Usuario; 2. administrador; 3. Domiciliario: "))
                if opc == 1:
                    Login.compareUser()
                    break
                elif opc == 2: 
                    Login.compareAdmin()
                    break
                elif opc == 3:
                    Login.compareDomiciliario()
                    break
                else:
                    print("Intente de nuevo con una opción válida")
        else:
            Register.Registrar()