import mysql.connector

def conectar_base_de_datos():
    try:
        db = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            password="root",
            database="thebox_bd"
        )
        return db
    except mysql.connector.Error as error:
        print("Error al conectar a la base de datos:", error)
        return None
    