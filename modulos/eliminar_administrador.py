# Librería de MySQL
import mysql.connector
from mysql.connector import Error

# Librerías de PyQt6
from PyQt6.QtWidgets import QLabel, QPushButton, QAbstractItemView, QMessageBox, QLineEdit, QDialog, QGridLayout, QGroupBox, QTableWidgetItem, QTableWidget
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt

# Módulo de Estilos
from qss import style

# conexion a la BD
from conexion_DB.dataBase import conectar_base_de_datos

# Módulo de para las cajas de mensajes
from modulos.mensajes import inicio, mensaje_ingreso_datos, errorConsulta

# Clase de eliminar 
class DeleteUser(QDialog):
    def __init__(self):
        super().__init__()
        self.deleteUser()
        
    def deleteUser(self):
        self.setWindowTitle("Eliminar administrador")
        self.setGeometry(750, 300, 540, 500)
        self.setWindowIcon(QIcon("img/logo.png"))
        self.setModal(True)
        self.setStyleSheet(style.fondo)
        
        self.titulo = QLabel(self)
        self.titulo.setStyleSheet(style.label_titulo_profesor)
        self.titulo.setText("Gestión de profesor")
        self.titulo.setFont(QFont("Segoe UI", 13))
        self.titulo.move(20, 30)
        
        # Se crear un QGroupBox para contener todos los elementos
        self.groupBox = QGroupBox("Detalle de administrador", self)
        self.groupBox.setStyleSheet(style.qgrupo_profesor)
        self.groupBox.setGeometry(20, 70, 500, 350)
        
        #Se crea un QGridLayout para organizar los elementos dentro del QGroupBox.
        layout = QGridLayout(self.groupBox)
        
        # BOTON
        self.mostrar_button = QPushButton(self)
        self.mostrar_button.setText("MOSTRAR TABLA")
        self.mostrar_button.setStyleSheet(style.botones_profesores)
        self.mostrar_button.setGeometry(20, 30,110, 30)
        self.mostrar_button.clicked.connect(self.tabla)
        layout.addWidget(self.mostrar_button)
        
        # TABLA 
        self.tabla_view = QTableWidget(self)
        self.tabla_view.setStyleSheet(style.tabla_profesor)
        layout.addWidget(self.tabla_view)
        
        self.titulo = QLabel(self)
        self.titulo.setText("DNI Profesor")
        self.titulo.setStyleSheet(style.label_titulo_profesor)
        self.titulo.move(20, 230)
        layout.addWidget(self.titulo)
        
        self.dni_input = QLineEdit(self)
        self.dni_input.setStyleSheet(style.lineedit_profesor)
        self.dni_input.setGeometry(120, 330,80, 30)
        layout.addWidget(self.dni_input)
        
        save_button = QPushButton(self)
        save_button.setStyleSheet(style.botones_profesores)
        save_button.setText("ELIMINAR")
        save_button.setGeometry(195, 440,150, 30)
        save_button.clicked.connect(self.delete)
        
        # Obtener datos de la tabla
        self.tabla_view.clicked.connect(self.obtener_datos)

        
    def tabla(self):
        responde = inicio("Registro de profesores","¿Desea ver tabla?")
        if responde == QMessageBox.StandardButton.Yes:
            try:
                db = conectar_base_de_datos()
                cursor = db.cursor()
                query = query = "SELECT * FROM profesor"
                cursor.execute(query)
                resultados = cursor.fetchall()

                if resultados:
                    
                    headers = [description[0].upper() for description in cursor.description]
                    
                    self.tabla_view.setRowCount(len(resultados))
                    self.tabla_view.setColumnCount(len(resultados[0]))
                    self.tabla_view.setHorizontalHeaderLabels(headers)
                    
                    # Ocultar encavezados vertical
                    encabezados_veticales = self.tabla_view.verticalHeader()
                    encabezados_veticales.setVisible(False)
                    
                    self.tabla_view.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
                    self.tabla_view.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
                    
                    for i, row in enumerate(resultados):
                        for j, val in enumerate(row):
                            item = QTableWidgetItem(str(val))
                            if j in [1,4,5]:  # Ajustar alineación para ciertas columnas
                                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  
                            self.tabla_view.setItem(i, j, item)
                else:
                    mensaje_ingreso_datos("Registro de profesor","No se puede mostrar tabla")
                
                self.tabla_view.clearSelection()
                cursor.close()
                db.close()
            
            except Error as ex:
                errorConsulta("Registro de administrador",f"Error en la consulta: {str(ex)}")
                print("Error executing the query", ex)
        else:
            print("no se puede mostrar tabla")

        
    def obtener_datos(self):
        row = self.tabla_view.currentRow()
    
        dni = self.tabla_view.item(row, 1).text()  # Obtener el texto del QTableWidgetItem
        dni = int(dni)  # Convertir a entero para la entrada de datos del QLineEdit
        
        # Mostrar los datos en los campos correspondientes
        self.dni_input.setText(str(dni))  # Convertir a texto antes de asignar al QLineEdit
        
        
    def delete(self):
        # Primero corroborar la seleccion de la fila
        if not self.tabla_view.currentItem():
            return
        
        # Selecciona la fila acutal
        selectedRow = self.tabla_view.currentItem().row()
        
        # Convertir el Item a 'str'
        dni = self.tabla_view.item(selectedRow, 1).text()
        
        # Establece el Item en el QLineEdite para tomar la referencia en la cosuslta DELETE
        self.dni_input.setText(dni)
        
        ok = inicio("Registro de administrador","¿Desea eliminar administrador?")
        if ok == QMessageBox.StandardButton.Yes:       
            try:
                db = conectar_base_de_datos()
                cursor = db.cursor()
                cursor.execute(f"DELETE FROM profesor WHERE dni = '{dni}'")    
                db.commit()

                if cursor:
                    mensaje_ingreso_datos("Registro de administrador","Administrador eliminado")
                    self.dni_input.clear()
                    self.tabla()
                else:
                    mensaje_ingreso_datos("Registro de administrador","Administrador no eliminado")
                cursor.close()
                db.close()
            except Error as ex:
                errorConsulta("Registro de alumnos",f"Error en la consulta: {str(ex)}")
        else:
            print("Error executing the query", ex)
            