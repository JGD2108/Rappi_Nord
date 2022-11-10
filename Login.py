import sqlite3
con = sqlite3.connect("Register.db")
cur = con.cursor()
class Login():
    def get_name():
        Usuario = input("Digite su Usuario")
        return Usuario
    
    def get_password():
        Password = input("Pssword")
        return Password

    def compare():
        ## Vamos a tener 2 tablas una de usuarios y otra de administrador, dependiendo de
        ## lo que el usuario escoja se busca en la tabla
        statement= (f"SELECT username from users WHERE username='{Login.get_name()}' AND Password = '{Login.get_password()}'")
        cur.execute(statement)
        if not cur.fetchone():  # An empty result evaluates to False.
            print("Login failed")
        else:
            print("Welcome")

    def execute():
        Login.compare()
    

