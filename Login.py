import sqlite3
con = sqlite3.connect("Register.db")
cur = con.cursor()
class Login():
    def get_name():
        Usuario = input("Digite su Usuario: ")
        return Usuario
    
    def get_password():
        Password = input("Pssword: ")
        return Password

    def compareUser():
        ## Vamos a tener 2 tablas una de usuarios y otra de administrador, dependiendo de
        ## lo que el usuario escoja se busca en la tabla
        statement= (f"SELECT User from Users WHERE User='{Login.get_name()}' AND Password = '{Login.get_password()}'")
        cur.execute(statement)
        if not cur.fetchone():  # An empty result evaluates to False.
            print("Login failed")
        else:
            print("Welcome")

    def compareAdmin():
        statement= (f"SELECT User from Admin WHERE User='{Login.get_name()}' AND Password = '{Login.get_password()}'")
        cur.execute(statement)
        if not cur.fetchone():  # An empty result evaluates to False.
            print("Login failed")
        else:
            print("Welcome")
    def execute():
        opc = input("1. Usuario o 2. administrador: ")
        opc = int(opc)
        if opc==1:
            Login.compareUser()
        else: 
            Login.compareAdmin()

Login.execute()
    

