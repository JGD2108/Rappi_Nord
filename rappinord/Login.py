import sqlite3
import stdiomask
from rappinord.Users import Register
from rappinord.user import User
con = sqlite3.connect("Register.db")
cur = con.cursor()

class Login():
    def compareUser():
        ## Vamos a tener 2 tablas una de usuarios y otra de administrador, dependiendo de
        ## lo que el usuario escoja se busca en la tabla
        Usuario = input("Digite su usuario: ")
        Password = stdiomask.getpass("Password")
        statement= (f"SELECT User from Users WHERE User='{Usuario}' AND Password = '{Password}'")
        cur.execute(statement)
        if not cur.fetchone():  # An empty result evaluates to False.
            print("Login failed")
        else:
            print("Welcome")
            Login.getInfo(Usuario)

    def compareAdmin():
        statement= (f"SELECT User from Admin WHERE User='{Login.get_name()}' AND Password = '{Login.get_password()}'")
        cur.execute(statement)
        if not cur.fetchone():  # An empty result evaluates to False.
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
        x = []
        total = 0
        user = User(nombre,id,cel,x,total)
        user.Pedido()

    def execute():
        opc1= int(input("1.Login o 2.Register"))
        if opc1==1:
            opc = int(input("1. Usuario o 2. administrador: "))
            if opc==1:
                Login.compareUser()
            else: 
                Login.compareAdmin()
        else:
            Register.Registrar()