from persistance.db import get_connection
from security.crypto import encrypt, decrypt

class User:

    def __init__(self, id:int, name:str, curp:str, account:str, password:str):
        self.id = id
        self.name = name
        self.curp = curp
        self.account = account
        self.password = password
        

    # Metodo para insertar un usuario en la base de datos
    def insert(name, curp, account, password):
        connection = get_connection()
        cursor = connection.cursor()

        curp_encrypt = encrypt(curp)
        password_encrypt = encrypt(password)

        sql = "INSERT INTO user (name, curp, account, password) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (name, curp_encrypt, account, password_encrypt))
        connection.commit()

        cursor.close()
        connection.close()


    # Metodo para verificar si se duplica un usuario
    def check_account_exists(account):
        # Hacer una consulta SQL que retorne los elementos que coincidan con esa cuenta
        # Retornar true si la coleccion contiene 1 o mas elementos. Si contiene cero, retorna false

        connection = get_connection()
        cursor = connection.cursor()

        sql = "SELECT account FROM user WHERE account = %s"
        cursor.execute(sql, (account,))
        
        rows = cursor.fetchall()

        cursor.close()
        connection.close()

        # Si hay 1 o mas registros -> True
        # Si no hay registros -> False
        return len(rows) > 0


    # Metodo para obtener los usuarios de la base de datos
    def get_users():
        connection = get_connection()
        cursor = connection.cursor(dictionary = True)
        sql = "SELECT id, name, curp, account, password FROM user"

        cursor.execute(sql)
        rows = cursor.fetchall()

        return [
            User (
                id = row["id"],
                name = row["name"],
                curp = decrypt(row["curp"]),
                account = row["account"],
                password = decrypt(row["password"])
            )
            for row in rows
        ]


    # Metodo para saber el usuario por su cuenta
    def get_user_by_account(account):
        connection = get_connection()
        cursor = connection.cursor(dictionary = True)
        sql = "SELECT id, name, curp, account, password FROM user WHERE account = %s"

        cursor.execute(sql, (account,))
        row = cursor.fetchone()

        if row is None:
            return None
        else:
            return User(
                id = row["id"],
                name = row["name"],
                account= row["account"],
                curp = decrypt(row["curp"]),
                password = decrypt(row["password"])
            )

