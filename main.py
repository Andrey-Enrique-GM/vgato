from entities.user import User
from entities.card import Card
from getpass import getpass


# Funcion para agregar un usuario a la base de datos
def register_user():
    name = input("Nombre: ")
    account = input("Cuenta: ")
    curp = input("CURP: ")
    password = getpass("Contraseña: ")

    # Validar si ya existe la cuenta
    if User.check_account_exists(account):
        print("La cuenta ya existe!!!")
        return

    User.insert(name, curp, account, password)
    print("Usuario registrado correctamente :)")


# Funcion para agregar una tarjeta a la base de datos
def register_card():
    number = getpass("Numero de tarjeta: ")
    bank = input("Banco: ")
    card_type = input("Tipo de tarjeta: ")

    Card.insert_card(number, bank, card_type)
    print("Tarjeta registrada correctamente :)")


# Funcion para hacer un listado de usuarios de la base de datos
def view_users():
    users = User.get_users()
    
    if not users:
        print("\nNo hay usuarios registrados.")
        return

    print("\n--- Lista de Usuarios ---")
    for user in users:
        print(f"Nombre: {user.name} | Cuenta: {user.account} | CURP: {user.curp}")
    print("-------------------------\n")


# Funcion para hacer un listado de tarjetas de la base de datos
def view_cards():
    cards = Card.get_cards()
    
    if not cards:
        print("\nNo hay tarjetas registradas.")
        return

    print("\n--- Lista de Tarjetas ---")
    for card in cards:
        print(f"Numero: {card['number']} | Banco: {card['bank']} | Tipo: {card['card_type']}")
    print("-------------------------\n")


# Funcion para iniciar sesion
def login():
    account = input("Cuenta: ")
    password = getpass("Contraseña: ")

    user = User.get_user_by_account(account)

    if user and user.password == password:
        return True
    else:
        return False
    #Esto hace lo mismo que todo ese if:
    #return user and user.password == password


# Este es el menuuu
if __name__ == "__main__":
    print("Inicio de sesion")
    if login():
        print("Seleccione una opcion del menu")
        print("1.- Registrar un usuario")
        print("2.- Registrar una tarjeta")
        print("3.- Consultar usuarios")
        print("4.- Consultar tarjetas")
        option = int(input())
        if option == 1:
            register_user()
        elif option == 2:
            register_card()
        elif option == 3:
            view_users()
        elif option == 4:
            view_cards()
    else:
        print("Credenciales invalidas")