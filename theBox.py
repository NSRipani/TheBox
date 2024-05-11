# Módulo para abrir aplicación
import sys

# Librería de MySQL
import mysql.connector
from mysql.connector import Error

# Librerías de PyQt6
from PyQt6.QtWidgets import QApplication,QLabel, QPushButton, QWidget, QMessageBox, QLineEdit, QCheckBox
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import QSettings, Qt

# Módulos de la carpta del proyecto
from modulos.registro_administrador import RegistroUser
from modulos.eliminar_administrador import DeleteUser
from modulos.ventana_principal import VentanaPrincipal
from modulos.mensajes import mensaje_ingreso_datos, errorConsulta, inicio
from conexion_DB.dataBase import conectar_base_de_datos

# Módulo de Estilos
from qss import style


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

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):        
        self.setWindowTitle("Log In")
        self.setGeometry(750, 300, 450, 500)
        self.setFixedWidth(450) 
        self.setFixedHeight(500)
        self.setWindowIcon(QIcon("img/logo.png"))
        self.setStyleSheet(style.fondo_logo)
        
        self.logo_label = QLabel(self)
        self.logo_label.setStyleSheet(style.logo_label)
        self.logo_label.setGeometry(155, 30,150,150)
        self.logo_label.setScaledContents(True)
        self.logo_label.setPixmap(QPixmap("img/logo.png"))
        self.logo_label.setStyleSheet("background-color: transparent;")
        
        self.user_label = QLabel("N° de DNI:", self)
        self.user_label.setStyleSheet(style.est)
        self.user_label.move(55, 200)
        
        self.user_input = QLineEdit(self)
        self.user_input.setStyleSheet(style.lineedit_logo)
        self.user_input.setMaxLength(8)
        self.user_input.setPlaceholderText("Sin puntos")
        self.user_input.setGeometry(150, 196, 170, 25)
        
        self.password_label = QLabel("Contraseña:", self)
        self.password_label.setStyleSheet(style.est)
        self.password_label.move(55, 240)
        
        self.password_input = QLineEdit(self)
        self.password_input.setStyleSheet(style.lineedit_logo)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setGeometry(150, 236,170, 25)
        self.password_input.setPlaceholderText("Ingrese números y letras")

        self.ver_contraseña = QCheckBox(self)
        self.ver_contraseña.setText("Ver contraseña")
        self.ver_contraseña.move(125, 265)
        self.ver_contraseña.clicked.connect(self.ver)
        
        self.Remember = QCheckBox("Recordarme", self)
        self.Remember.move(235, 265)
        self.Remember.setChecked(True)
        
        self.login_button = QPushButton("Iniciar sesion", self)
        self.login_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.login_button.setStyleSheet(style.estBo)
        self.login_button.setGeometry(120, 320,220, 30)
        self.login_button.clicked.connect(self.login)
        
        self.register_button = QPushButton("Registrar administrador", self)
        self.register_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.register_button.setStyleSheet(style.estBo)
        self.register_button.setGeometry(120, 360,220, 30)
        self.register_button.clicked.connect(self.registroUser)
    
        self.delete_user_button = QPushButton("Eliminar administrador", self)
        self.delete_user_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.delete_user_button.setStyleSheet(style.estBo)
        self.delete_user_button.setGeometry(120, 400, 220, 30)
        self.delete_user_button.clicked.connect(self.delete_User) 
   
        self.load_settings()
        self.login_button.clicked.connect(self.save_settings)

    # Carga la configuración previamente guardada desde el archivo de configuración
    def load_settings(self):
        settings = QSettings("MyApp", "Login")
        username = settings.value("DNI:", "")
        password = settings.value("Contraseña:", "")
        remember = settings.value("Recordarme", False, type=bool)

        self.user_input.setText(username)
        self.password_input.setText(password)
        self.Remember.setChecked(remember)

    # Guarda la configuración actual del formulario de inicio de sesión en el archivo de configuración
    def save_settings(self):
        settings = QSettings("MyApp", "Login")
        username = self.user_input.text()
        password = self.password_input.text()
        remember = self.Remember.isChecked()
    
        settings.setValue("DNI:", username)
        settings.setValue("Contraseña:", password)
        settings.setValue("Recordarme", remember)
    
    # Función para ingreso a la ventana pricipal
    def login(self):
        # Llama a la clase 'ConexionBaseDeDatos'
        conexion_bd = ConexionBaseDeDatos()
        conexion_bd.conectar()
        
        dni = self.user_input.text()
        contraseña = self.password_input.text()
        
        if not dni.isalnum():
            mensaje_ingreso_datos("Inicio de sesion","El DNI debe ser numérico")
            return

        try:
            dni = int(dni)
        except ValueError:
            mensaje_ingreso_datos("Inicio de sesion","Error, el DNI debe ser un número entero")
            return

        if not contraseña:
            mensaje_ingreso_datos("Inicio de sesion","La contraseña debe ser:\n- Texto y/o número\n- No puede estar vacía")
            return

        consulta = inicio("Abrir ventana principal","¿Desea abrir la venta principal?")
        if consulta == QMessageBox.StandardButton.Yes:    
            try:
                db = conectar_base_de_datos()
                cursor = db.cursor()
                
                query = f"SELECT * FROM profesor WHERE dni = '{dni}' AND contraseña = '{contraseña}'"
                
                cursor.execute(query)
                resultados = cursor.fetchone()
                if resultados:
                    mensaje_ingreso_datos("Inicio de sesion","Acceso consedido")

                    self.ventanaPrincipal = VentanaPrincipal()
                    self.ventanaPrincipal.show()
                    self.hide()
                else:
                    mensaje_ingreso_datos("Inicio de sesion","Acceso denegado")

                    
                cursor.close()
                db.close()

            except Error as ex:
                errorConsulta("Inicio de sesion",f"Error en la consulta: {ex}")
        else:
            print("No se abrirá una nueva ventana")
            
        conexion_bd.desconectar()
            
    # Función para abrir venta para el registro de ADMINISTRADOR
    def registroUser(self):
        
        # Aquí puedes abrir la ventana de registro de DUEÑOS
        self.ventana_registro = RegistroUser()
        self.ventana_registro.show()
        
    
    # Función para el chequeo de la contraseña para mostrarla
    def ver(self, clicked):
        if clicked:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
    
    # Función para corroborar el tilde en el CheckBox de 'Remember'        
    def recordar(self, clicked):
        if clicked:
            self.Remember.setChecked(True)
        else:
            self.Remember.setChecked(False)
    
    # Función para abrir venta para el eliminar de ADMINISTRADOR
    def delete_User(self):
        self.user_delete = DeleteUser()
        self.user_delete.show()
  
   
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = Login()
    login_window.show()
    sys.exit(app.exec())