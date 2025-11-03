# import database
# from menu_principal import mostrar_menu_principal

# if __name__ == "__main__":
#     mostrar_menu_principal()
#     database.create_tables()

# main.py
from menu_principal import mostrar_menu_principal
from database import create_tables

if __name__ == "__main__":
    create_tables()
    mostrar_menu_principal()

