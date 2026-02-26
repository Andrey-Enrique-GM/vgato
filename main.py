from entities.user import User
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
        print("2.- Consultar usuarios")
        option = int(input())
        if option == 1:
            register_user()
        elif option == 2:
            view_users()
    else:
        print("Credenciales invalidas")