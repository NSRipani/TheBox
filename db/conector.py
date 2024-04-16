import mysql 
import mysql.connector
from mysql.connector import Error

class Conexion():
    def __init__(self):
        try:
            conexion = mysql.connector.connect(
                host = "localhost",
                port = "3306",
                user = "root",
                password = "root",
                database = "thebox_bd"
            )
            if conexion.is_connected():
                print("La base de datos esta conectada")
                cursor = conexion.cursor()
                cursor.execute("SELECT database()")
                registro = cursor.fetchone()
                print("Conectado a la DB: ", registro)
        except Error as ex:
            print("Los datos no coinciden con la base de datos")
        finally:
            if conexion.is_connected():
                conexion.close()
                print("La conexion ha finalizdo")
                
    
    