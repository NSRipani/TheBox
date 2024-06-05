# Librería de MySQL
import mysql.connector
from mysql.connector import Error

# Librería para generar Archivos de tipo Excel(.xlsx)
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Border, Side, numbers

# Librerías de PyQt6
from PyQt6.QtWidgets import (QLabel,QFormLayout,QFileDialog, QCompleter, QAbstractScrollArea, QHeaderView, QGridLayout, QHBoxLayout, QDateEdit, 
                             QMessageBox, QTableWidget, QAbstractItemView, QTableWidgetItem, QPushButton, QLineEdit, QStatusBar, QWidget,
                             QVBoxLayout, QGroupBox, QDialog, QFrame, QTabWidget, QComboBox)
from PyQt6.QtGui import QIcon, QKeySequence, QAction, QPixmap,QGuiApplication
from PyQt6.QtCore import *

# Módulo de para las cajas de mensajes
from modulos.mensajes import (mensaje_ingreso_datos, errorConsulta, inicio, aviso_descargaExitosa, aviso_Advertencia_De_excel, 
                              resultado_empleado, aviso_resultado, mensaje_horas_empleados, aviso_resultado_asistencias)

# Módulo de Estilos
from qss import style

# Validaciones
from validaciones.empleado import variables,lim_campos, seleccion_DeTabla, verTabla
from validaciones.archivo_Excel import empleado_EXCEL

# conexion
from conexion_DB.dataBase import conectar_base_de_datos

class RegistroUser(QDialog):
    def __init__(self):
        super().__init__()
        self.empleo()
        
    def empleo(self):
        self.setWindowTitle("Registro de admin")
        self.setWindowIcon(QIcon("img/logo.png"))
        self.setStyleSheet(style.fondo2)
        self.setModal(True)
        
        # Crear el QGroupBox
        group_box = QGroupBox("DATOS DEL ADMIN")
        group_box.setStyleSheet(style.estilo_grupo)

        # Crear el layout del formulario
        form_layout = QFormLayout()
        
        # Ajustar alineación y espaciado
        form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        form_layout.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        form_layout.setSpacing(10)
        form_layout.setContentsMargins(10, 10, 10, 10)

        # Crear widgets de etiquetas y entradas
        self.dni = QLineEdit()
        self.dni.setStyleSheet(style.estilo_lineedit)
        self.dni.setMaxLength(8)
        self.contraseña = QLineEdit()
        self.contraseña.setStyleSheet(style.estilo_lineedit)
        self.nombre = QLineEdit()
        self.nombre.setStyleSheet(style.estilo_lineedit)
        self.apellido = QLineEdit()
        self.apellido.setStyleSheet(style.estilo_lineedit)
        self.puesto = QLineEdit()
        self.puesto.setStyleSheet(style.estilo_lineedit)
        self.sex = QLineEdit()
        self.sex.setStyleSheet(style.estilo_lineedit)
        self.sex.setPlaceholderText("Hombre / Mujer")

        d = QLabel("DNI:")
        d.setStyleSheet(style.label)
        c = QLabel("Contraseña:")
        c.setStyleSheet(style.label)
        n = QLabel("Nommbre:")
        n.setStyleSheet(style.label)
        a = QLabel("Apellido:")
        a.setStyleSheet(style.label)
        p = QLabel("Puesto:")
        p.setStyleSheet(style.label)
        s = QLabel("Sexo:")
        s.setStyleSheet(style.label)

        # Añadir widgets al formulario
        form_layout.addRow(d, self.dni)
        form_layout.addRow(c, self.contraseña)
        form_layout.addRow(n, self.nombre)
        form_layout.addRow(a, self.apellido)
        form_layout.addRow(p, self.puesto)
        form_layout.addRow(s, self.sex)

        # Crear los botones
        guardar_button = QPushButton("Guardar")
        guardar_button.setStyleSheet(style.estilo_boton)
        guardar_button.setCursor(Qt.CursorShape.PointingHandCursor)
        mostrar_button = QPushButton("Mostrar")
        mostrar_button.setStyleSheet(style.estilo_boton)
        mostrar_button.setCursor(Qt.CursorShape.PointingHandCursor)
        actualizar_button = QPushButton("Actualizar")
        actualizar_button.setStyleSheet(style.estilo_boton)
        actualizar_button.setCursor(Qt.CursorShape.PointingHandCursor)
        eliminar_button = QPushButton("Eliminar")
        eliminar_button.setStyleSheet(style.estilo_boton)
        eliminar_button.setCursor(Qt.CursorShape.PointingHandCursor)
        
        # Crear un layout horizontal para los botones
        botones_layout = QHBoxLayout()
        botones_layout.addWidget(guardar_button)
        botones_layout.addWidget(mostrar_button)
        botones_layout.addWidget(actualizar_button)
        botones_layout.addWidget(eliminar_button)

        # Señales
        guardar_button.clicked.connect(self.guardar)
        mostrar_button.clicked.connect(self.mostrar)
        # limpiarTABLA.clicked.connect(self.limpiar_tabla_empleados)
        actualizar_button.clicked.connect(self.actualizar)
        eliminar_button.clicked.connect(self.eliminar)
        

        # Añadir los botones al formulario
        form_layout.addRow(botones_layout)
        
        # Crear la tabla
        self.tableWidget = QTableWidget()
        self.tableWidget.setStyleSheet(style.esttabla)
        self.tableWidget.clicked.connect(self.autocompleto_de_datos_empleado)
        
        # Crear un layout vertical para el QGroupBox
        vbox = QVBoxLayout()
        vbox.addLayout(form_layout)
        vbox.addWidget(self.tableWidget)

        # Configurar el QGroupBox con el layout
        group_box.setLayout(vbox)

        # Crear el layout principal y añadir el QGroupBox
        main_layout = QVBoxLayout()
        main_layout.addWidget(group_box)
        self.setLayout(main_layout)

        # Configurar la ventana
        self.setFixedSize(1300, 800)
        
        # Centrar la ventana
        self.centrar_ventana()

    def centrar_ventana(self):
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)
        
    def guardar(self):
        dni = self.dni.text().replace(".","")
        contraseña = self.contraseña.text()
        nombre = self.nombre.text().capitalize().title()
        apellido = self.apellido.text().capitalize().title()
        ocupacion = self.puesto.text().capitalize()
        sexo = self.sex.text().capitalize()

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

                    self.dni.clear()
                    self.contraseña.clear()
                    self.nombre.clear()
                    self.apellido.clear()
                    self.puesto.clear()
                    self.sex.clear()
                else:
                    mensaje_ingreso_datos("Registro de administrador","Registro no cargado")
                    
                cursor.close()
                db.close()        
                
            except Error as ex:
                errorConsulta("Registro de alumnos",f"Error en la consulta: {str(ex)}")
                print("Error al ejecutar la consulta", ex)
    
    def mostrar(self):
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
                
                header = self.tableWidget.horizontalHeader()
                header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
                header.setAutoScroll(True)
                
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

    def autocompleto_de_datos_empleado(self):
        row = self.tableWidget.currentRow()
    
        dni = self.tableWidget.item(row, 1).text()  # Obtener el texto del QTableWidgetItem
        dni = int(dni)  # Convertir a entero

        password = self.tableWidget.item(row, 2).text()
        nombre = self.tableWidget.item(row, 3).text()
        apellido = self.tableWidget.item(row, 4).text()
        ocupacion = self.tableWidget.item(row, 5).text()
        sexo = self.tableWidget.item(row, 6).text()

        # Mostrar los datos en los campos correspondientes
        self.dni.setText(str(dni))  # Convertir a texto antes de asignar al QLineEdit
        self.contraseña.setText(password)
        self.nombre.setText(nombre)
        self.apellido.setText(apellido)
        self.puesto.setText(ocupacion)
        self.sex.setText(sexo)

        self.tableWidget.clearSelection() # Deselecciona la tabla

    def actualizar(self):
        if not self.tableWidget.currentItem():
            return
        
        dni = self.dni.text().replace(".","")
        contraseña = self.contraseña.text()
        nombre = self.nombre.text().capitalize().title()
        apellido = self.apellido.text().capitalize().title()
        ocupacion = self.puesto.text().capitalize()
        sexo = self.sex.text().capitalize()

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
                    self.dni.clear()
                    self.contraseña.clear()
                    self.nombre.clear()
                    self.apellido.clear()
                    self.puesto.clear()
                    self.sex.clear()

                    self.mostrar()
                
                self.tableWidget.clearSelection()
                cursor.close()
                db.close()

            except Error as ex:
                errorConsulta("Registro de alumnos",f"Error en la consulta: {str(ex)}")
                print("Error al ejecutar la consulta", ex)

    def eliminar(self):
        # Primero corroborar la seleccion de la fila
        if not self.tableWidget.currentItem():
            return
        
        # Selecciona la fila acutal
        selectedRow = self.tableWidget.currentItem().row()
        
        # Convertir el Item a 'str'
        dni = self.tableWidget.item(selectedRow, 1).text()
        
        # Establece el Item en el QLineEdite para tomar la referencia en la cosuslta DELETE
        self.dni.setText(dni)
        
        ok = inicio("Registro de administrador","¿Desea eliminar administrador?")
        if ok == QMessageBox.StandardButton.Yes:       
            try:
                db = conectar_base_de_datos()
                cursor = db.cursor()
                cursor.execute(f"DELETE FROM profesor WHERE dni = '{dni}'")    
                db.commit()

                if cursor:
                    mensaje_ingreso_datos("Registro de administrador","Administrador eliminado")
                    self.dni.clear()
                    self.contraseña.clear()
                    self.nombre.clear()
                    self.apellido.clear()
                    self.puesto.clear()
                    self.sex.clear()
                    self.mostrar()
                else:
                    mensaje_ingreso_datos("Registro de administrador","Administrador no eliminado")
                cursor.close()
                db.close()
            except Error as ex:
                errorConsulta("Registro de alumnos",f"Error en la consulta: {str(ex)}")
        else:
            print("Error executing the query", ex)
