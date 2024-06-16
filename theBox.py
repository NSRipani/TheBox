# Módulo para abrir aplicación
import sys

# Librería de MySQL
import mysql.connector
from mysql.connector import Error

# Librerías de PyQt6
from PyQt6.QtWidgets import QApplication
from modulos.ventana_principal import VentanaPrincipal


# CLASE PARA BASE DE DATOS
class ConexionBaseDeDatos:
    def __init__(self):
        self.conexion = None
        
    def conectar(self):
        try:
            self.conexion = mysql.connector.connect(
                host = "localhost",
                port = "3306",
                user = "root",
                password = "root",
                database = "thebox_bd"
            )
            if self.conexion.is_connected():
                print("La base de datos esta conectada")
                cursor = self.conexion.cursor()
                cursor.execute("SELECT database()")
                registro = cursor.fetchone()
                print("Conectado a la DB: ", registro)
        except Error as ex:
            print("Los datos no coinciden con la base de datos")
    
    def desconectar(self):
        if self.conexion and self.conexion.is_connected():
            self.conexion.close()
            print("La conexion ha finalizdo")
  
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = VentanaPrincipal()
    login_window.show()
    sys.exit(app.exec())
    
