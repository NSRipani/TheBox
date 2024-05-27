# Librería de MySQL
import mysql.connector
from mysql.connector import Error

# Librería para generar Archivos de tipo Excel(.xlsx)
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Border, Side, numbers

# Librerías de PyQt6
from PyQt6.QtWidgets import (QLabel,QFormLayout,QFileDialog, QCompleter, QAbstractScrollArea, QHeaderView, QGridLayout, QHBoxLayout, QDateEdit, 
                             QMessageBox, QTableWidget, QAbstractItemView, QTableWidgetItem, QPushButton, QLineEdit, QStatusBar, QWidget,
                             QVBoxLayout, QGroupBox, QMainWindow, QFrame, QTabWidget, QComboBox)
from PyQt6.QtGui import QIcon, QKeySequence, QAction, QPixmap,QGuiApplication
from PyQt6.QtCore import *

# Módulo de para las cajas de mensajes
from modulos.mensajes import (mensaje_ingreso_datos, errorConsulta, inicio, aviso_descargaExitosa, aviso_Advertencia_De_excel, 
                              resultado_empleado, aviso_resultado, mensaje_horas_empleados, aviso_resultado_asistencias)

# Validaciones
from validaciones.contabilidad import cuentas
# Módulo de Estilos
from qss import style


# conexion
from conexion_DB.dataBase import conectar_base_de_datos

class CuentaContable(QWidget):
    def __init__(self):
        super().__init__()
        self.cuenta()
        
    def cuenta(self):
        self.setWindowTitle("Registro de empleado")
        self.setWindowIcon(QIcon("img/logo.png"))
        self.setStyleSheet(style.fondo2)
        
        # Crear el QGroupBox
        group_box = QGroupBox("CARGAR CUENTA CONTABLE")
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
        self.tipo = QLineEdit()
        self.tipo.setStyleSheet(style.estilo_lineedit)

        n = QLabel("Nombre:")
        n.setStyleSheet(style.label)
        
        # Añadir widgets al formulario
        form_layout.addRow(n, self.nombre)

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
        # botones_layout.addWidget(excel_empleado)

        # Señales
        guardar_button.clicked.connect(self.guardar_empleado)
        mostrar_button.clicked.connect(self.mostrar_empleado)
        # limpiarTABLA.clicked.connect(self.limpiar_tabla_empleados)
        actualizar_button.clicked.connect(self.actualizar_empleado)
        eliminar_button.clicked.connect(self.eliminar_empleado)
        # excel_empleado.clicked.connect(self.planilla_excel)
        

        # Añadir los botones al formulario
        form_layout.addRow(botones_layout)
        
        # Crear la tabla
        self.tablacuenta = QTableWidget()
        self.tablacuenta.setStyleSheet(style.esttabla)
        self.tablacuenta.clicked.connect(self.autocompleto_de_datos_empleado)
        
        # Crear un layout vertical para el QGroupBox
        vbox = QVBoxLayout()
        vbox.addLayout(form_layout)
        vbox.addWidget(self.tablacuenta)

        # Configurar el QGroupBox con el layout
        group_box.setLayout(vbox)

        # Crear el layout principal y añadir el QGroupBox
        main_layout = QVBoxLayout()
        main_layout.addWidget(group_box)
        self.setLayout(main_layout)

        # Configurar la ventana
        self.setWindowTitle("Registro de cuenta contable")
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
                
        nom_emp = self.nombre.text().capitalize().title()
        if not isinstance(nom_emp, str) or not nom_emp.isalpha():
            mensaje_ingreso_datos("Registro de cuenta","La cuenta debe contener: \n- Letras y/o espacios entre cuentas.")
            return 
        try:
            db = conectar_base_de_datos()
            cursor = db.cursor()
            cursor.execute("INSERT INTO tipo (nombre) VALUES (%s)",(nom_emp,))
            db.commit()
            
            if cursor:
                mensaje_ingreso_datos("Registro de cuenta","Registro cargado")
                self.nombre.clear()
                # lim_campos(self,QDate)
            else:
                mensaje_ingreso_datos("Registro de cuenta","Registro no cargado")
                
            cursor.close()
            db.close()
        except Error as ex:
            errorConsulta("Registro de cuenta",f"Error en la consulta: {str(ex)}")
            print("Error executing the query", ex)
    
    def mostrar_empleado(self):
        try:
            db = conectar_base_de_datos()
            cursor = db.cursor()
            cursor.execute(f"SELECT * FROM tipo ORDER BY id_tipo")
            busqueda = cursor.fetchall()
            if len(busqueda) > 0:
                resultado_empleado("Registro de cuenta",f"Se encontraron {len(busqueda)} coincidencias.")
                cuentas(self,cursor,busqueda,QHeaderView,QTableWidget,QAbstractItemView,QTableWidgetItem,QDate,Qt)
            else:
                resultado_empleado("Registro de cuenta",f"Se encontraron {len(busqueda)} coincidencias.")
                
            cursor.close()
            db.close()
        except Error as ex:
            errorConsulta("Registro de cuenta",f"Error en la consulta: {str(ex)}")
            print("Error executing the query", ex)

    def autocompleto_de_datos_empleado(self):
        rows = self.tablacuenta.currentRow()
        
        descripcion = self.tablacuenta.item(rows,1).text()
        self.nombre.setText(descripcion)
        
        self.tablacuenta.clearSelection() # Deselecciona la fila

    def actualizar_empleado(self):
        # Verificar si se ha seleccionado una fila
        if not self.tablacuenta.currentItem():
            mensaje_ingreso_datos("Registro de cuenta","Debe seleccionar la cuenta de la tabla para actualizar")
            return
        
        id_empl = int(self.tablacuenta.item(self.tablacuenta.currentRow(), 0).text())
        descripcion = self.nombre.text().capitalize().title()
        
        if not isinstance(descripcion, str) or not descripcion.isalpha():
            mensaje_ingreso_datos("Registro de cuenta","La cuenta debe contener: \n- Letras y/o espacios entre nombres.")
            return 
                
        empleado_Actualizar = inicio("Registro de cuenta","¿Seguro que desea actulizar?")
        if empleado_Actualizar == QMessageBox.StandardButton.Yes:   
            try:
                db = conectar_base_de_datos()
                cursor = db.cursor()
                cursor.execute("UPDATE tipo SET nombre = %s WHERE id_tipo = %s", (descripcion,id_empl))
                db.commit() 
                
                if cursor:
                    mensaje_ingreso_datos("Registro de cuenta","Registro actualizado")
                    self.nombre.clear()
                else:
                    mensaje_ingreso_datos("Registro de cuenta","Registro no actualizado")
                    
                cursor.close()
                db.close() 
                
                self.tablacuenta.clearSelection() # Deselecciona la fila
                
            except Error as ex:
                errorConsulta("Registro de cuenta",f"Error en la consulta: {str(ex)}")
                print("Error executing the query", ex)
        else:
            print("No se actualiza registro")

    def eliminar_empleado(self):
        # Primero corroborar la seleccion de la fila
        if not self.tablacuenta.currentItem():
            mensaje_ingreso_datos("Registro de cuenta","Debe buscar una cuenta a eliminar")
            return
        
        # Selecciona la fila acutal
        selectedRow = self.tablacuenta.currentItem().row()
        id_ = int(self.tablacuenta.item(selectedRow, 0).text())
        
        empleado_eliminar = inicio("Registro de cuenta","¿Desea eliminar el empleado?")
        if empleado_eliminar == QMessageBox.StandardButton.Yes:
            try:
                db = conectar_base_de_datos()
                cursor = db.cursor()
                cursor.execute(f"DELETE FROM tipo WHERE id_tipo = {id_}")
                db.commit()
                if cursor:
                    mensaje_ingreso_datos("Registro de cuenta","Registro eliminado")
                    self.tablacuenta.removeRow(selectedRow)
                    self.nombre.clear()
                    self.tablacuenta.clearSelection() # Deselecciona la fila
                else:
                    mensaje_ingreso_datos("Registro de cuenta","Registro no eliminado")  
                                
            except Error as ex:
                errorConsulta("Registro de cuenta",f"Error en la consulta: {str(ex)}")
                print("Error executing the query", ex)
            cursor.close()
            db.close()
            
        else:
            print("No se elimino registro")
            
    # def planilla_excel(self):
    #     empleado_EXCEL(self,Workbook,Font,PatternFill,Border,Side,numbers,QFileDialog)
    # def limpiar_tabla_empleados(self):
    #     clearTabla(self)