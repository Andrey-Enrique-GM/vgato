from persistance.db import get_connection
from security.crypto import encrypt, decrypt

class Card:

    def __init__(self, id_card:int, number:str, bank:str, card_type:str):
        self.id_card = id_card
        self.number = number
        self.bank = bank
        self.card_type = card_type

    # Metodo para agregar una tarjeta a la base de datos
    def insert_card(number, bank, card_type):
        connection = get_connection()
        cursor = connection.cursor()

        number_encrypt = encrypt(number)

        sql = "INSERT INTO card (number, bank, card_type) VALUES (%s, %s, %s)"
        cursor.execute(sql, (number_encrypt, bank, card_type))
        connection.commit()

        cursor.close()
        connection.close()


    # Metodo para obtener las tarjetas de la base de datos
    def get_cards():
        connection = get_connection()
        cursor = connection.cursor(dictionary = True)
        sql = "SELECT id_card, number, bank, card_type FROM card"

        cursor.execute(sql)
        rows = cursor.fetchall()

        return [
            {
                "id": row["id_card"],
                "number": decrypt(row["number"]),
                "bank": row["bank"],
                "card_type": row["card_type"]
            }
            for row in rows
        ]
    
    