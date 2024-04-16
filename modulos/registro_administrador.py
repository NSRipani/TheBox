# Librería de MySQL
from mysql.connector import Error
import mysql.connector

# Librerías de PyQt6
from PyQt6.QtWidgets import QDialog, QTableWidgetItem, QAbstractItemView, QLabel, QPushButton, QWidget, QMessageBox, QLineEdit, QGroupBox, QGridLayout, QTableWidget
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt

# Módulo de Estilos
from qss import style

# Módulo de para las cajas de mensajes
from modulos.mensajes import mensaje_ingreso_datos, inicio,errorConsulta

# conexion a la BD
from conexion_DB.dataBase import conectar_base_de_datos

class RegistroUser(QDialog):
    def __init__(self):
        super().__init__()
        self.registro()
    
    def registro(self):        
        self.setWindowTitle("Registro de administrador")
        self.setGeometry(700, 300, 540, 550)
        self.setWindowIcon(QIcon("img/logo.png"))
        self.setModal(True)
        self.setStyleSheet(style.fondo)
        
        self.titulo = QLabel("Administrador", self)
        self.titulo.setStyleSheet(style.label_titulo_profesor)
        self.titulo.move(20, 10)
        
        #Se crea un QGroupBox 
        self.groupBox = QGroupBox("Datos a completar del administrador", self)
        self.groupBox.setGeometry(20, 50, 500, 400)
        self.groupBox.setStyleSheet(style.qgrupo_profesor)
        
        #Se crea un QGridLayout para organizar los elementos dentro del QGroupBox.
        layout = QGridLayout(self.groupBox)
        
        #Se crea un QLabel con el texto "Contraseña actual" y se agrega al QGridLayout      
        self.user = QLabel("DNI:", self.groupBox)
        self.user.setStyleSheet(style.label_profesor)
        layout.addWidget(self.user, 0, 0)
        
        self.input_user = QLineEdit(self.groupBox)        
        self.input_user.setStyleSheet(style.lineedit_profesor)
        self.input_user.setMaxLength(8)
        self.input_user.setPlaceholderText("Sin puntos")
        layout.addWidget(self.input_user, 0, 1)
        
        self.password = QLabel("Contraseña:", self.groupBox)
        self.password.setStyleSheet(style.label_profesor)
        layout.addWidget(self.password, 1, 0)
        
        self.input_password = QLineEdit(self.groupBox)
        self.input_password.setStyleSheet(style.lineedit_profesor)
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.input_password, 1, 1)
        
        self.nombre = QLabel("Nombre:", self.groupBox)
        self.nombre.setStyleSheet(style.label_profesor)
        layout.addWidget(self.nombre, 2, 0)
        
        self.input_nombre = QLineEdit(self.groupBox)
        self.input_nombre.setStyleSheet(style.lineedit_profesor)
        layout.addWidget(self.input_nombre, 2, 1)
        
        self.apellido = QLabel("Apellido:", self.groupBox)
        self.apellido.setStyleSheet(style.label_profesor)
        layout.addWidget(self.apellido, 3, 0)
        
        self.input_apellido = QLineEdit(self.groupBox)
        self.input_apellido.setStyleSheet(style.lineedit_profesor)
        layout.addWidget(self.input_apellido, 3, 1)
        
        self.puesto = QLabel("Occupacion:", self.groupBox)
        self.puesto.setStyleSheet(style.label_profesor)
        layout.addWidget(self.puesto, 5, 0)
        self.input_job = QLineEdit(self.groupBox)
        self.input_job.setStyleSheet(style.lineedit_profesor)
        self.input_job.setPlaceholderText("Ej: Profesor")
        layout.addWidget(self.input_job, 5, 1)
        
        self.sex = QLabel("Sexo:", self.groupBox)
        self.sex.setStyleSheet(style.label_profesor)
        layout.addWidget(self.sex, 6, 0)
        
        self.input_sex = QLineEdit(self.groupBox)
        self.input_sex.setStyleSheet(style.lineedit_profesor)
        self.input_sex.setPlaceholderText("Hombre / Mujer")
        layout.addWidget(self.input_sex, 6, 1)
        
       # Se crea un QTableWidget y se agrega al QGridLayout en la posición (8, 0) que corresponde a la novena fila y primera columna.
        self.tableWidget = QTableWidget(self.groupBox)
        self.tableWidget.setStyleSheet(style.tabla_profesor)
        layout.addWidget(self.tableWidget, 8, 0, 1, 2)
        
        # Botones 
        save_button = QPushButton(self)
        save_button.setText("GUARDAR")
        save_button.setCursor(Qt.CursorShape.PointingHandCursor)
        save_button.setStyleSheet(style.botones_profesores)
        save_button.setGeometry(60, 460,150, 30)
        save_button.clicked.connect(self.confirmar)
        
        cancel_button = QPushButton(self)
        cancel_button.setText("VER TABLA")
        cancel_button.setCursor(Qt.CursorShape.PointingHandCursor)
        cancel_button.setStyleSheet(style.botones_profesores)
        cancel_button.setGeometry(60, 500,150, 30)
        cancel_button.clicked.connect(self.mostrar)
        
        cancel_button = QPushButton(self)
        cancel_button.setText("CANCELAR")
        cancel_button.setCursor(Qt.CursorShape.PointingHandCursor)
        cancel_button.setStyleSheet(style.botones_profesores)
        cancel_button.setGeometry(345, 500,150, 30)
        cancel_button.clicked.connect(self.cerrar)
        
        cancel_button = QPushButton(self)
        cancel_button.setText("ACTUALIZAR")
        cancel_button.setCursor(Qt.CursorShape.PointingHandCursor)
        cancel_button.setStyleSheet(style.botones_profesores)
        cancel_button.setGeometry(345, 460,150, 30)
        cancel_button.clicked.connect(self.actualizar)

        # Obtener datos de la tabla
        self.tableWidget.clicked.connect(self.obtenerdatos)
        
    def confirmar(self):
        dni = self.input_user.text().replace(".","")
        contraseña = self.input_password.text()
        nombre = self.input_nombre.text().capitalize().title()
        apellido = self.input_apellido.text().capitalize().title()
        ocupacion = self.input_job.text().capitalize()
        sexo = self.input_sex.text().capitalize()

        # Validar que el DNI sea un número entero
        if not dni.isdigit() or not len(dni) != 8:
            mensaje_ingreso_datos("Registro de administrador","El DNI debe ser::\n- Numérico.\n-Contener 8 dígitos")
            return # Salir de la función si la validación falla
        try:
            if dni:
                dni = int(dni)
        except ValueError:
            mensaje_ingreso_datos("Registro de administrador","El DNI debe ser:\n- Numérico.\n-Contener 8 dígitos.")
            return  
    
        if not contraseña.isalnum():
            mensaje_ingreso_datos("Registro de administrador","La contaseña debe contener letras y/o números.")
            return
           
        if not all(c.isalpha() or c.isspace() for c in nombre):
            mensaje_ingreso_datos("Registro de administrador","El nombre debe contener: \n- Letras y/o espacios entre nombres(si tiene mas de dos).")
            return

        if not all(c.isalpha() or c.isspace() for c in apellido):
            mensaje_ingreso_datos("Registro de administrador","El apellido debe contener: \n- Letras y/o espacios entre apellidos(si tiene mas de dos).")
            return

        if not ocupacion.isalpha():
            mensaje_ingreso_datos("Registro de administrador","Colocar su ocupación.")
            return

        if not sexo.isalpha():
            mensaje_ingreso_datos("Registro de administrador","El sexo debe ser 'Hombre' o 'Mujer'.")
            return
        
        cargar = inicio("Registro de alumnos","¿Desea guardar alumno?")
        if cargar == QMessageBox.StandardButton.Yes: 
            try:
                db = conectar_base_de_datos()
                cursor = db.cursor()
                query = "INSERT INTO profesor (dni, contraseña, nombre, apellido, ocupacion, sexo) VALUES (%s,%s,%s,%s,%s,%s)"
                values = (dni, contraseña, nombre, apellido, ocupacion, sexo)
                cursor.execute(query, values)
                db.commit()      

                if cursor:
                    mensaje_ingreso_datos("Registro de administrador","Registro cargado")

                    self.input_user.clear()
                    self.input_password.clear()
                    self.input_nombre.clear()
                    self.input_apellido.clear()
                    self.input_job.clear()
                    self.input_sex.clear()
                else:
                    mensaje_ingreso_datos("Registro de administrador","Registro no cargado")
                    
                cursor.close()
                db.close()        
                
            except Error as ex:
                errorConsulta("Registro de alumnos",f"Error en la consulta: {str(ex)}")
                print("Error al ejecutar la consulta", ex)
        else:
            errorConsulta("Registro de alumnos",f"Error en la consulta: {str(ex)}")
            
      
    def mostrar(self):
        ver = inicio("Registro de alumnos","¿Desea guardar alumno?")
        if ver == QMessageBox.StandardButton.Yes:
            try:
                db = conectar_base_de_datos()
                cursor = db.cursor()
                query = "SELECT * FROM profesor"
                cursor.execute(query)
                resultados = cursor.fetchall()

                if resultados:
                    
                    headers = [description[0].upper() for description in cursor.description]
                    
                    self.tableWidget.setRowCount(len(resultados))
                    self.tableWidget.setColumnCount(len(resultados[0]))
                    self.tableWidget.setHorizontalHeaderLabels(headers)
                    
                    # Ocultar encavezados vertical
                    encabezados_veticales = self.tableWidget.verticalHeader()
                    encabezados_veticales.setVisible(False)
                    
                    self.tableWidget.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
                    self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
                    
                    for i, row in enumerate(resultados):
                        for j, val in enumerate(row):
                            item = QTableWidgetItem(str(val))
                            if j in [1, 2, 5, 6]:  # Ajustar alineación para ciertas columnas
                                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                            self.tableWidget.setItem(i, j, item)
                    
                else:
                    mensaje_ingreso_datos("Registro de administrador","Registro no se muestra tabla")
                
                self.tableWidget.clearSelection()
                cursor.close()
                db.close()
            
            except Error as ex:
                errorConsulta("Registro de alumnos",f"Error en la consulta: {str(ex)}")
                print("Error executing the query", ex)
        else:
            print("no se mostro")
            
    def obtenerdatos(self):
        row = self.tableWidget.currentRow()
    
        dni = self.tableWidget.item(row, 1).text()  # Obtener el texto del QTableWidgetItem
        dni = int(dni)  # Convertir a entero

        password = self.tableWidget.item(row, 2).text()
        nombre = self.tableWidget.item(row, 3).text()
        apellido = self.tableWidget.item(row, 4).text()
        ocupacion = self.tableWidget.item(row, 5).text()
        sexo = self.tableWidget.item(row, 6).text()

        # Mostrar los datos en los campos correspondientes
        self.input_user.setText(str(dni))  # Convertir a texto antes de asignar al QLineEdit
        self.input_password.setText(password)
        self.input_nombre.setText(nombre)
        self.input_apellido.setText(apellido)
        self.input_job.setText(ocupacion)
        self.input_sex.setText(sexo)

        self.tableWidget.clearSelection() # Deselecciona la tabla
        
        
    def actualizar(self):
        
        if not self.tableWidget.currentItem():
            return
        
        dni = self.input_user.text().replace(".","")
        contraseña = self.input_password.text()
        nombre = self.input_nombre.text().capitalize().title()
        apellido = self.input_apellido.text().capitalize().title()
        ocupacion = self.input_job.text().capitalize()
        sexo = self.input_sex.text().capitalize()

        # Validar que el DNI sea un número entero
        if not dni.isdigit() or not len(dni) == 8:
            mensaje_ingreso_datos("Registro de administrador","El DNI debe ser::\n- Numérico.\n-Contener 8 dígitos")
            return # Salir de la función si la validación falla
        try:
            if dni:
                dni = int(dni)
        except ValueError:
            mensaje_ingreso_datos("Registro de administrador","El DNI debe ser::\n- Numérico.\n-Contener 8 dígitos")
            return 
    
        if not contraseña.isalnum():
            mensaje_ingreso_datos("Registro de administrador","La contaseña debe contener letras y/o números.")
            return

        if not all(c.isalpha() or c.isspace() for c in nombre):
            mensaje_ingreso_datos("Registro de administrador","El nombre debe contener: \n- Letras y/o espacios entre nombres(si tiene mas de dos).")
            return
        else:
            print("correcto")

        if not all(c.isalpha() or c.isspace() for c in apellido):
            mensaje_ingreso_datos("Registro de administrador","El apellido debe contener: \n- Letras y/o espacios entre apellidos(si tiene mas de dos).")
            return
        else:
            print("correcto")

        if not ocupacion.isalpha():
            mensaje_ingreso_datos("Registro de administrador","Colocar su ocupación.")
            return

        if not sexo.isalpha():
            mensaje_ingreso_datos("Registro de administrador","El sexo debe ser 'Hombre' o 'Mujer'.")
            return
        
        actual = inicio("Busqueda de administrador","¿Desea actualizar?")
        if actual == QMessageBox.StandardButton.Yes:
            try:
                db = conectar_base_de_datos()
                cursor = db.cursor()
                query = "UPDATE profesor SET contraseña=%s, nombre=%s, apellido=%s, ocupacion=%s, sexo=%s WHERE dni=%s"
                values = (contraseña, nombre, apellido, ocupacion, sexo, dni)
                cursor.execute(query, values)
                db.commit()
            
                if cursor:
                    mensaje_ingreso_datos("Registro de administrador","Registro actualizado")
                    self.input_user.clear()
                    self.input_password.clear()
                    self.input_nombre.clear()
                    self.input_apellido.clear()
                    self.input_job.clear()
                    self.input_sex.clear()

                    self.mostrar()
                
                self.tableWidget.clearSelection()
                cursor.close()
                db.close()

            except Error as ex:
                errorConsulta("Registro de alumnos",f"Error en la consulta: {str(ex)}")
                print("Error al ejecutar la consulta", ex)
        else:
            print("no se actualizo")
    def cerrar(self):
        self.close()