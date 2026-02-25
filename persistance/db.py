import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host = "localhost",                  #"65.99.225.32",          #localhost
        user = "root",                  #"siste214_gato_si",      #user
        password = "admin",             #"ITSON@2026#si",     #admin
        database = "gatodb"              #"siste214_gato_si",  #gatodb
    )