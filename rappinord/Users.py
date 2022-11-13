import sqlite3
import stdiomask
con = sqlite3.connect("Register.db")
register = con.cursor()
"""
administrador = [("Jg2108", "1001915145", "Jose", "3043774896", "1001915145"),
                ("CFV123","200162691", "Cristian", "3109876543", "1042849073"),]
register.executemany("INSERT INTO Users VALUES(?,?,?,?,?)",administrador)
con.commit()
con.close()"""

class Register():
    def get_Name():
        Name=input("Digite su nombre: ")
        return Name

    def get_User():
        while True: 
            User= input("Digite el usuario que desea: ")
            statement= (f"SELECT User from Users WHERE User='{User}'")
            register.execute(statement)
            if not register.fetchone(): 
                print("Usuario valido")
                break
            else:
                print("Usuario ya existe intente de nuevo")
        return User

    def get_Password():
        Password= stdiomask.getpass("Digite su contraseña: ")
        return Password

    def getCel():
        try:
            Cel = input("Digite su cel: ")
            while len(Cel)!=10:
                print("Digite un numero de telefono valido: ")
                Cel = input("Digite su cel: ")
        except ValueError:
            print("Digite un número: ")
        return Cel

    def getId():
        try:
            Id = input("Digite su ID: ")
        except ValueError:
            print("Digite un numero: ")
        return Id
    
    def Registrar():
        data = [(Register.get_User(), Register.get_Password(), Register.get_Name(), Register.getCel(), Register.getId())]
        register.executemany("INSERT INTO Users VALUES(?,?,?,?,?)",data)
        con.commit()
        con.close()
