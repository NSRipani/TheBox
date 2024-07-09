# Librería de MySQL
import mysql.connector
from mysql.connector import Error

# Librería para generar Archivos de tipo Excel(.xlsx)
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Border, Side, numbers

# Librerías de PyQt6
from PyQt6.QtWidgets import (QLabel,QFormLayout,QFileDialog, QCompleter, QHeaderView, QHBoxLayout, QDateEdit, 
                             QMessageBox, QTableWidget, QAbstractItemView, QTableWidgetItem, QPushButton, QLineEdit,
                             QVBoxLayout, QGroupBox, QDialog,QComboBox)
from PyQt6.QtGui import QIcon, QGuiApplication
from PyQt6.QtCore import *

# Módulo de para las cajas de mensajes
from modulos.mensajes import mensaje_ingreso_datos, errorConsulta, inicio, ingreso_datos

# Módulo de Estilos
from qss import style

# Validaciones
from validaciones.empleado import variables,lim_campos, seleccion_DeTabla, verTabla
from validaciones.archivo_Excel import empleado_EXCEL

# conexion
from conexion_DB.dataBase import conectar_base_de_datos

class Empleado(QDialog):
    def __init__(self):
        super().__init__()
        self.empleo()
        
    def empleo(self):
        self.setWindowTitle("Registro de empleado")
        self.setWindowIcon(QIcon("img/logo.png"))
        self.setStyleSheet(style.fondo2)
        self.setModal(True)
        
        # Crear el QGroupBox
        group_box = QGroupBox("DATOS DEL EMPLEADO")
        group_box.setStyleSheet(style.estilo_grupo)

        # Crear el layout del formulario
        form_layout = QFormLayout()
        
        # Ajustar alineación y espaciado
        form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        form_layout.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        form_layout.setSpacing(10)
        form_layout.setContentsMargins(10, 10, 10, 10)

        # Crear widgets de etiquetas y entradas
        self.nombre = QLineEdit()
        self.nombre.setStyleSheet(style.estilo_lineedit)
        self.apellido = QLineEdit()
        self.apellido.setStyleSheet(style.estilo_lineedit)
        self.sex = QComboBox()
        self.sex.setStyleSheet(style.estilo_combo)
        self.sex.addItem("Seleccione...", "")  # Primer ítem vacío
        self.sex.addItem("Hombre", "Hombre")
        self.sex.addItem("Mujer", "Mujer")
        self.sex.setCurrentIndex(0)
        
        self.edad = QLineEdit()
        self.edad.setMaxLength(2)
        self.edad.setPlaceholderText("Ej: 23")
        self.edad.setStyleSheet(style.estilo_lineedit)
        self.dni = QLineEdit()
        self.dni.setPlaceholderText("Sin punto")
        self.dni.setStyleSheet(style.estilo_lineedit)
        self.celular = QLineEdit()
        self.celular.setStyleSheet(style.estilo_lineedit)
        self.celular.setPlaceholderText("Ej: 3424789123")
        self.fecha = QDateEdit()
        self.fecha.setStyleSheet(style.fecha)
        self.fecha.setLocale(QLocale("es-AR"))
        self.fecha.setCursor(Qt.CursorShape.PointingHandCursor)
        self.fecha.setFixedWidth(200)
        self.fecha.setDate(QDate.currentDate())
        self.fecha.setDisplayFormat("dd/MM/yyyy")
        self.fecha.setCalendarPopup(True)

        n = QLabel("Nombre:")
        n.setStyleSheet(style.label)
        a = QLabel("Apellido:")
        a.setStyleSheet(style.label)
        s = QLabel("Sexo:")
        s.setStyleSheet(style.label)
        e = QLabel("Edad:")
        e.setStyleSheet(style.label)
        d = QLabel("DNI:")
        d.setStyleSheet(style.label)
        c = QLabel("N° Celular:")
        c.setStyleSheet(style.label)
        f = QLabel("Fecha:")
        f.setStyleSheet(style.label)

        # Añadir widgets al formulario
        form_layout.addRow(n, self.nombre)
        form_layout.addRow(a, self.apellido)
        form_layout.addRow(s, self.sex)
        form_layout.addRow(e, self.edad)
        form_layout.addRow(d, self.dni)
        form_layout.addRow(c, self.celular)
        form_layout.addRow(f, self.fecha)

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
        excel_empleado = QPushButton()
        icon_excel = QIcon("img/excel.png")
        excel_empleado.setIcon(icon_excel)
        excel_empleado.setIconSize(QSize(20,20))
        excel_empleado.setFixedWidth(50)
        excel_empleado.setCursor(Qt.CursorShape.PointingHandCursor)
        excel_empleado.setStyleSheet(style.boton_excel)
        
        # Crear un layout horizontal para los botones
        botones_layout = QHBoxLayout()
        botones_layout.addWidget(guardar_button)
        botones_layout.addWidget(mostrar_button)
        botones_layout.addWidget(actualizar_button)
        botones_layout.addWidget(eliminar_button)
        botones_layout.addWidget(excel_empleado)

        # Señales
        guardar_button.clicked.connect(self.guardar_empleado)
        mostrar_button.clicked.connect(self.mostrar_empleado)
        # limpiarTABLA.clicked.connect(self.limpiar_tabla_empleados)
        actualizar_button.clicked.connect(self.actualizar_empleado)
        eliminar_button.clicked.connect(self.eliminar_empleado)
        excel_empleado.clicked.connect(self.planilla_excel)
        

        # Añadir los botones al formulario
        form_layout.addRow(botones_layout)
        
        # Crear la tabla
        self.tablaEmp = QTableWidget()
        self.tablaEmp.setStyleSheet(style.esttabla)
        self.tablaEmp.clicked.connect(self.autocompleto_de_datos_empleado)
        
        # Crear un layout vertical para el QGroupBox
        vbox = QVBoxLayout()
        vbox.addLayout(form_layout)
        vbox.addWidget(self.tablaEmp)

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
    
    
    def guardar_empleado(self):
                
        nom_emp = self.nombre.text().title()
        apell_emp = self.apellido.text().title()
        sex_emp = self.sex.currentData()
        edad_emp = self.edad.text()
        dni_emp = self.dni.text()
        cel = self.celular.text()
        fecha = self.fecha.date().toPyDate()
        
        validacion = variables(nom_emp,apell_emp,sex_emp,edad_emp,dni_emp,cel)
        if validacion != "Validación exitosa.":
            mensaje_ingreso_datos("Error de validación", "Verifique los datos por favor")
            return
        try:
            db = conectar_base_de_datos()
            cursor = db.cursor()
            
            # Verificar si el 'dni' ya existe
            cursor.execute("SELECT COUNT(*) FROM registro_empleado WHERE dni = %s", (dni_emp,))
            resultado = cursor.fetchone()
            
            if resultado[0] > 0:
                mensaje_ingreso_datos("Registro duplicado", "Ya existe un registro con ese DNI")
                return
            
            cursor.execute("INSERT INTO registro_empleado (nombre, apellido, sexo, edad, dni, celular, fecha) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                            (nom_emp,apell_emp,sex_emp,edad_emp,dni_emp,cel,fecha))
            db.commit()
            
            if cursor:
                ingreso_datos("Registro de empleado","Registro cargado")
                lim_campos(self,QDate)
            else:
                ingreso_datos("Registro de empleado","Registro no cargado")
                
            cursor.close()
            db.close()
        except Error as ex:
            errorConsulta("Registro de alumnos",f"Error en la consulta: {str(ex)}")
            print("Error executing the query", ex)
        # else:
        #     print("no se guardo")
    
    def mostrar_empleado(self):
        try:
            db = conectar_base_de_datos()
            cursor = db.cursor()
            cursor.execute(f"SELECT id_empleado AS ID, nombre, apellido, sexo, edad, dni, celular, fecha FROM registro_empleado ORDER BY id_empleado")
            busqueda = cursor.fetchall()
            if len(busqueda) > 0:
                ingreso_datos("Registro de empleado",f"Se encontraron {len(busqueda)} coincidencias.")
                verTabla(self,cursor,busqueda,QHeaderView,QTableWidget,QAbstractItemView,QTableWidgetItem,QDate,Qt)
            else:
                ingreso_datos("Registro de empleado",f"Se encontraron {len(busqueda)} coincidencias.")
                
            cursor.close()
            db.close()
        except Error as ex:
            errorConsulta("Registro de empleado",f"Error en la consulta: {str(ex)}")
            print("Error executing the query", ex)

    def autocompleto_de_datos_empleado(self):
        seleccion_DeTabla(self,QDate)
    
    def actualizar_empleado(self):
        # Verificar si se ha seleccionado una fila
        if not self.tablaEmp.currentItem():
            mensaje_ingreso_datos("Registro de empleado","Debe seleccionar el empleado te la tabla para actualizar")
            return
        
        id_empl = int(self.tablaEmp.item(self.tablaEmp.currentRow(), 0).text())
        nom_emp = self.nombre.text().title()
        apell_emp = self.apellido.text().title()
        sex_emp = self.sex.currentData()
        edad_emp = self.edad.text()
        dni_emp = self.dni.text()
        cel = self.celular.text()
        fecha = self.fecha.date().toPyDate()
        
        validacion = variables(nom_emp,apell_emp,sex_emp,edad_emp,dni_emp,cel)
        if validacion != "Validación exitosa.":
            mensaje_ingreso_datos("Error de validación", "Verifique los datos por favor")
            return
                
        empleado_Actualizar = inicio("Busqueda de empleado","¿Seguro que desea actulizar?")
        if empleado_Actualizar == QMessageBox.StandardButton.Yes:   
            try:
                db = conectar_base_de_datos()
                cursor = db.cursor()
                cursor.execute("UPDATE registro_empleado SET nombre = %s, apellido = %s, sexo = %s, edad = %s,  dni = %s, celular = %s, fecha = %s"
                               "WHERE id_empleado = %s", (nom_emp,apell_emp,sex_emp,edad_emp,dni_emp,cel,fecha,id_empl))
                db.commit() 
                
                if cursor:
                    ingreso_datos("Registro de empleado","Registro actualizado")
                    lim_campos(self,QDate)
                else:
                    ingreso_datos("Registro de empleado","Registro no actualizado")
                    
                cursor.close()
                db.close() 
                
                self.tablaEmp.clearSelection() # Deselecciona la fila
                
            except Error as ex:
                errorConsulta("Registro de empleado",f"Error en la consulta: {str(ex)}")
                print("Error executing the query", ex)
        else:
            print("No se actualiza registro")

    def eliminar_empleado(self):
        # Primero corroborar la seleccion de la fila
        if not self.tablaEmp.currentItem():
            mensaje_ingreso_datos("Registro de empleado","Debe buscar el empleado a eliminar")
            return
        
        # Selecciona la fila acutal
        selectedRow = self.tablaEmp.currentItem().row()
        id_emple = int(self.tablaEmp.item(selectedRow, 0).text())
        
        empleado_eliminar = inicio("Registro de empleado","¿Desea eliminar el empleado?")
        if empleado_eliminar == QMessageBox.StandardButton.Yes:
            try:
                db = conectar_base_de_datos()
                cursor = db.cursor()
                # cursor.execute(f"DELETE FROM registro_empleado WHERE id_empleado = {id_emple}")
                cursor.execute(f"UPDATE registro_empleado SET habilitado = 0 WHERE id_empleado= {id_emple}")#, (id_dis,))
                
                db.commit()
                if cursor:
                    ingreso_datos("Registro de empleado","Registro eliminado")
                    self.tablaEmp.removeRow(selectedRow)
                    lim_campos(self,QDate)
                    self.tablaEmp.clearSelection() # Deselecciona la fila
                else:
                    ingreso_datos("Registro de empleado","Registro no eliminado")  
                                
            except Error as ex:
                errorConsulta("Registro de empleado",f"Error en la consulta: {str(ex)}")
                print("Error executing the query", ex)
            cursor.close()
            db.close()
            
        else:
            print("No se elimino registro")
            
    def planilla_excel(self):
        empleado_EXCEL(self,Workbook,Font,PatternFill,Border,Side,numbers,QFileDialog)