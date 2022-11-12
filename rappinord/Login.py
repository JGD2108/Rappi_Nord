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
        statement= (f"SELECT User from Users WHERE User='{Usuario}' AND Password = '{Password}'")
        cur.execute(statement)
        if not cur.fetchone():  # An empty result evaluates to False.
            print("Login failed")
        else:
            print("Welcome", Usuario)
            Login.getInfo(Usuario)

    def compareAdmin():
        Usuario = input("Digite su usuario: ")
        Password = stdiomask.getpass("Password: ")
        statement= (f"SELECT User from Admin WHERE User='{Usuario}' AND Password = '{Password}'")
        cur.execute(statement)
        if not cur.fetchone():  # An empty result evaluates to False.
            print("Login failed")
        else:
            print("Welcome", Usuario)
            proceso.execute()
        
    def getInfo(Usuario: str):
        statement = (f"SELECT * FROM Users where User = '{Usuario}'")
        cur.execute(statement)
        record = cur.fetchone()
        nombre = record[2]
        cel = record[3]
        id = record[4]
        x = []
        total = 0
        user = User(nombre,id,cel,x,total)
        user.Pedido()

    def execute():
        opc1= int(input("1.Login; 2.Register: "))
        if opc1 == 1:
            opc = int(input("1. Usuario; 2. administrador: "))
            if opc == 1:
                Login.compareUser()
            else: 
                Login.compareAdmin()
        else:
            Register.Registrar()