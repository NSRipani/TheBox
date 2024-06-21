# Librería de MySQL
import mysql.connector
from mysql.connector import Error

import re

# Librerías de PyQt6
from PyQt6.QtWidgets import (QLabel,QFormLayout,QDialog, QCompleter, QAbstractScrollArea, QHeaderView, QGridLayout, QHBoxLayout, QDateEdit, 
                             QMessageBox, QTableWidget, QAbstractItemView, QTableWidgetItem, QPushButton, QLineEdit, QSpacerItem, QWidget,
                             QVBoxLayout, QGroupBox, QSizePolicy, QFrame, QTabWidget, QComboBox)
from PyQt6.QtGui import QIcon, QKeySequence, QAction, QPixmap,QGuiApplication
from PyQt6.QtCore import *

# Módulo de para las cajas de mensajes
from modulos.mensajes import mensaje_ingreso_datos, errorConsulta, inicio, resultado_empleado

# Validaciones
from validaciones.contabilidad import cuentas

# Módulo de Estilos
from qss import style

# Cargar tipo
from modulos.cargar_cuenta.catagarTipoCuenta import actualizar_combobox_TipoCUENTA,actualizar_combobox_Categoria

# conexion
from conexion_DB.dataBase import conectar_base_de_datos

class CuentaContable(QDialog):
    def __init__(self):
        super().__init__()
        self.cuenta()
        
    def cuenta(self):
        self.setWindowTitle("Registro de empleado")
        self.setWindowIcon(QIcon("img/logo.png"))
        self.setModal(True)
        self.setStyleSheet(style.fondo2)

        # Crear el QGroupBox
        group_box = QGroupBox("DETALLE DE CUENTA CONTABLE")
        group_box.setStyleSheet(style.estilo_grupo)

        contenedor_formularios = QHBoxLayout()
        
        titulo_tipocuenta = QLabel("CARGAR TIPO DE CUENTA")
        titulo_tipocuenta.setStyleSheet(style.label_contable)
        
        # Crear el layout del formulario
        # form_layout_Tcuenta = QFormLayout()
        form_layout_Cuenta = QFormLayout()
        
        # # Ajustar alineación y espaciado
        # form_layout_Tcuenta.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        # form_layout_Tcuenta.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        # form_layout_Tcuenta.setSpacing(10)
        # form_layout_Tcuenta.setContentsMargins(10, 10, 10, 10)
        
        form_layout_Cuenta.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        form_layout_Cuenta.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        form_layout_Cuenta.setSpacing(10)
        form_layout_Cuenta.setContentsMargins(10, 10, 10, 10)
        
        # # Crear widgets de etiquetas y entradas
        # self.nombre = QLineEdit()
        # self.nombre.setStyleSheet(style.estilo_lineedit)
        # self.nombre.setPlaceholderText("Activos, Pasivos, Patrimonio, Ingresos o Egreso")

        # t_cuneta = QLabel("Tipo:")
        # t_cuneta.setStyleSheet(style.label)
        
        # # Añadir widgets al formulario
        # form_layout_Tcuenta.addRow(titulo_tipocuenta)
        # form_layout_Tcuenta.addRow(t_cuneta, self.nombre)
        
        # # Crear los botones al formulaio 'Cuenta'
        # guardar_button = QPushButton("Guardar")
        # guardar_button.setStyleSheet(style.estilo_boton)
        # guardar_button.setCursor(Qt.CursorShape.PointingHandCursor)
        # mostrar_button = QPushButton("Mostrar")
        # mostrar_button.setStyleSheet(style.estilo_boton)
        # mostrar_button.setCursor(Qt.CursorShape.PointingHandCursor)
        # actualizar_button = QPushButton("Actualizar")
        # actualizar_button.setStyleSheet(style.estilo_boton)
        # actualizar_button.setCursor(Qt.CursorShape.PointingHandCursor)
        # eliminar_button = QPushButton("Eliminar")
        # eliminar_button.setStyleSheet(style.estilo_boton)
        # eliminar_button.setCursor(Qt.CursorShape.PointingHandCursor)
        
        # # Crear un layout horizontal para los botones
        # botones_layout = QHBoxLayout()
        # botones_layout.addWidget(guardar_button)
        # botones_layout.addWidget(mostrar_button)
        # botones_layout.addWidget(actualizar_button)
        # botones_layout.addWidget(eliminar_button)
        
        # layuot = QVBoxLayout()
        # spacer4 = QSpacerItem(10, 120, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        # layuot.addItem(spacer4)
        
        # # Añadir los botones al formulario
        # form_layout_Tcuenta.addRow(layuot)
        # form_layout_Tcuenta.addRow(botones_layout)
        
        # # Crear un QFrame para ser usado como divisor
        # divisor = QFrame()
        # divisor.setFrameShape(QFrame.Shape.VLine)  # Línea vertical
        # divisor.setFrameShadow(QFrame.Shadow.Sunken)
        
        titulo_tipocuenta = QLabel("CUENTA")
        titulo_tipocuenta.setStyleSheet(style.label_contable)
        
        n_cuenta = QLabel("Nombre:")
        n_cuenta.setStyleSheet(style.label)
        t_cuenta = QLabel("Tipo: ")
        t_cuenta.setStyleSheet(style.label)
        descripcion = QLabel("Descripción: ")
        descripcion.setStyleSheet(style.label)
        categoria = QLabel("Categoría: ")
        categoria.setStyleSheet(style.label)
        
        self.n_cuenta = QLineEdit()
        self.n_cuenta.setStyleSheet(style.estilo_lineedit)
        self.t_cuenta = QLineEdit()
        self.t_cuenta.setStyleSheet(style.estilo_lineedit)
        self.t_cuenta.setPlaceholderText("Activos, Pasivos, Patrimonio, Ingresos o Egreso")
        actualizar_combobox_TipoCUENTA(self,QCompleter,Qt,style)
        self.descripcion = QLineEdit()
        self.descripcion.setStyleSheet(style.estilo_lineedit)
        self.categoria = QLineEdit()
        self.categoria.setStyleSheet(style.estilo_lineedit)
        self.categoria.setPlaceholderText("'Debe' o 'Haber'")
        actualizar_combobox_Categoria(self,QCompleter,Qt,style)
        
        # Añadir widgets al formulario
        form_layout_Cuenta.addRow(titulo_tipocuenta)
        form_layout_Cuenta.addRow(n_cuenta, self.n_cuenta)
        form_layout_Cuenta.addRow(t_cuenta, self.t_cuenta)
        form_layout_Cuenta.addRow(descripcion, self.descripcion)
        form_layout_Cuenta.addRow(categoria, self.categoria)
        
        # Crear los botones al formulaio 'Tipo de Cuenta'
        guardar_button2 = QPushButton("Guardar")
        guardar_button2.setStyleSheet(style.estilo_boton)
        guardar_button2.setCursor(Qt.CursorShape.PointingHandCursor)
        mostrar_button2 = QPushButton("Mostrar")
        mostrar_button2.setStyleSheet(style.estilo_boton)
        mostrar_button2.setCursor(Qt.CursorShape.PointingHandCursor)
        actualizar_button2 = QPushButton("Actualizar")
        actualizar_button2.setStyleSheet(style.estilo_boton)
        actualizar_button2.setCursor(Qt.CursorShape.PointingHandCursor)
        eliminar_button2 = QPushButton("Eliminar")
        eliminar_button2.setStyleSheet(style.estilo_boton)
        eliminar_button2.setCursor(Qt.CursorShape.PointingHandCursor)
        
        # Crear un layout horizontal para los botones
        botones_layout2 = QHBoxLayout()
        botones_layout2.addWidget(guardar_button2)
        botones_layout2.addWidget(mostrar_button2)
        botones_layout2.addWidget(actualizar_button2)
        botones_layout2.addWidget(eliminar_button2)
        
        # Añadir los botones al formulario
        form_layout_Cuenta.addRow(botones_layout2)
        
        # contenedor_formularios.addLayout(form_layout_Tcuenta)
        # contenedor_formularios.addWidget(divisor)
        contenedor_formularios.addLayout(form_layout_Cuenta)

        # # Señales
        # guardar_button.clicked.connect(self.guardar_tipo)
        # mostrar_button.clicked.connect(self.mostrar_tipo)
        # actualizar_button.clicked.connect(self.actualizar_tipo)
        # eliminar_button.clicked.connect(self.eliminar_tipo)
        
        guardar_button2.clicked.connect(self.guardar_cuenta)
        mostrar_button2.clicked.connect(self.mostrar_cuenta)
        actualizar_button2.clicked.connect(self.actualizar_cuenta)
        eliminar_button2.clicked.connect(self.eliminar_cuenta)
        
        # Crear la tabla
        self.tablacuenta = QTableWidget()
        self.tablacuenta.setStyleSheet(style.esttabla)
        self.tablacuenta.clicked.connect(self.autocompleto_de_datos_tipo)
        
        # Crear un layout vertical para el QGroupBox
        vbox = QVBoxLayout()
        vbox.addLayout(contenedor_formularios)
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
        
    # def guardar_tipo(self):       
    #     nom_emp = self.nombre.text().capitalize().title()
    #     if not isinstance(nom_emp, str) or not nom_emp.isalpha():
    #         mensaje_ingreso_datos("Registro de cuenta","La cuenta debe contener: \n- Letras y/o espacios entre cuentas.")
    #         return 
    #     try:
    #         db = conectar_base_de_datos()
    #         cursor = db.cursor()
    #         cursor.execute("INSERT INTO tipo (nombre) VALUES (%s)",(nom_emp,))
    #         db.commit()
            
    #         if cursor:
    #             mensaje_ingreso_datos("Registro de cuenta","Registro cargado")
    #             self.nombre.clear()
    #             # lim_campos(self,QDate)
    #         else:
    #             mensaje_ingreso_datos("Registro de cuenta","Registro no cargado")
                
    #         cursor.close()
    #         db.close()
    #     except Error as ex:
    #         errorConsulta("Registro de cuenta",f"Error en la consulta: {str(ex)}")
    #         print("Error executing the query", ex)
    
    # def mostrar_tipo(self):
    #     try:
    #         db = conectar_base_de_datos()
    #         cursor = db.cursor()
    #         cursor.execute(f"SELECT * FROM tipo ORDER BY id_tipo")
    #         busqueda = cursor.fetchall()
    #         if len(busqueda) > 0:
    #             resultado_empleado("Registro de cuenta",f"Se encontraron {len(busqueda)} coincidencias.")
    #             cuentas(self,cursor,busqueda,QHeaderView,QTableWidget,QAbstractItemView,QTableWidgetItem,QDate,Qt)
    #         else:
    #             resultado_empleado("Registro de cuenta",f"Se encontraron {len(busqueda)} coincidencias.")
                
    #         cursor.close()
    #         db.close()
    #     except Error as ex:
    #         errorConsulta("Registro de cuenta",f"Error en la consulta: {str(ex)}")
    #         print("Error executing the query", ex)

    # def autocompleto_de_datos_tipo(self):
    #     rows = self.tablacuenta.currentRow()
        
    #     descripcion = self.tablacuenta.item(rows,1).text()
    #     self.nombre.setText(descripcion)
        
    #     self.tablacuenta.clearSelection() # Deselecciona la fila

    # def actualizar_tipo(self):
    #     # Verificar si se ha seleccionado una fila
    #     if not self.tablacuenta.currentItem():
    #         mensaje_ingreso_datos("Registro de cuenta","Debe seleccionar la cuenta de la tabla para actualizar")
    #         return
        
    #     id_tipo = int(self.tablacuenta.item(self.tablacuenta.currentRow(), 0).text())
    #     descripcion = self.nombre.text().capitalize().title()
        
    #     if not isinstance(descripcion, str) or not descripcion.isalpha():
    #         mensaje_ingreso_datos("Registro de cuenta","La cuenta debe contener: \n- Letras y/o espacios entre nombres.")
    #         return 
                
    #     empleado_Actualizar = inicio("Registro de cuenta","¿Seguro que desea actulizar?")
    #     if empleado_Actualizar == QMessageBox.StandardButton.Yes:   
    #         try:
    #             db = conectar_base_de_datos()
    #             cursor = db.cursor()
    #             cursor.execute("UPDATE tipo SET nombre = %s WHERE id_tipo = %s", (descripcion,id_tipo))
    #             db.commit() 
                
    #             if cursor:
    #                 mensaje_ingreso_datos("Registro de cuenta","Registro actualizado")
    #                 self.nombre.clear()
    #             else:
    #                 mensaje_ingreso_datos("Registro de cuenta","Registro no actualizado")
                    
    #             cursor.close()
    #             db.close() 
                
    #             self.tablacuenta.clearSelection() # Deselecciona la fila
                
    #         except Error as ex:
    #             errorConsulta("Registro de cuenta",f"Error en la consulta: {str(ex)}")
    #             print("Error executing the query", ex)
    #     else:
    #         print("No se actualiza registro")

    # def eliminar_tipo(self):
    #     # Primero corroborar la seleccion de la fila
    #     if not self.tablacuenta.currentItem():
    #         mensaje_ingreso_datos("Registro de cuenta","Debe buscar una cuenta a eliminar")
    #         return
        
    #     # Selecciona la fila acutal
    #     selectedRow = self.tablacuenta.currentItem().row()
    #     id_tipo = int(self.tablacuenta.item(selectedRow, 0).text())
        
    #     try:
    #         db = conectar_base_de_datos()
    #         cursor = db.cursor()
    #         cursor.execute(f"DELETE FROM tipo WHERE id_tipo = {id_tipo}")
    #         db.commit()
    #         if cursor:
    #             mensaje_ingreso_datos("Registro de cuenta","Registro eliminado")
    #             self.tablacuenta.removeRow(selectedRow)
    #             self.nombre.clear()
    #             self.tablacuenta.clearSelection() # Deselecciona la fila
    #         else:
    #             mensaje_ingreso_datos("Registro de cuenta","Registro no eliminado")  
                            
    #     except Error as ex:
    #         errorConsulta("Registro de cuenta",f"Error en la consulta: {str(ex)}")
    #         print("Error executing the query", ex)
    #     cursor.close()
    #     db.close()

    ### ////////////////////////// PARA CUENTA ///////////////////////////////////////
    def guardar_cuenta(self):       
        nomTipo = self.n_cuenta.text().capitalize()
        tipo = self.t_cuenta.currentText()
        descrip = self.descripcion.text().capitalize()
        categor = self.categoria.text().capitalize()
        
        patron = re.compile(r'^[a-zA-ZáéíóúÁÉÍÓÚüÜ\'\s]+$') 
        if not isinstance(nomTipo, str) or nomTipo.isspace() or not patron.match(nomTipo): 
            mensaje_ingreso_datos("Registro de cuenta","El 'nombre' debe contener:\n\n- Letras y/o espacios entre nombres(si tiene mas de dos).")
            return
        if not isinstance(tipo, str) or not tipo.isalpha():
            mensaje_ingreso_datos("Registro de cuenta","El tipo debe contener: \n- Las opciones mostradas.")
            return
        if not isinstance(descrip, str) or descrip.isspace() or not patron.match(descrip): 
            mensaje_ingreso_datos("Registro de cuenta","La descripción debe contener: \n- Solo texto.")
            return 
        if not isinstance(categor, str) or not categor.isalpha():
            mensaje_ingreso_datos("Registro de cuenta","La categoría deben contener: \n- 'Debe' o 'Haber'.")
            return 
        
        try:
            db = conectar_base_de_datos()
            cursor = db.cursor()
            cursor.execute("INSERT INTO cuenta (nombre,tipo,descripcion,categoria) VALUES (%s,%s,%s,%s)",(nomTipo,tipo,descrip,categor))
            db.commit()
            
            if cursor:
                mensaje_ingreso_datos("Registro de cuenta","Registro cargado")
                self.n_cuenta.clear()
                self.t_cuenta.setCurrentIndex(0)
                self.descripcion.clear()
                self.categoria.clear()
                self.tablacuenta.clearSelection() # Deselecciona la fila
            else:
                mensaje_ingreso_datos("Registro de cuenta","Registro no cargado")
                
            cursor.close()
            db.close()
        except Error as ex:
            errorConsulta("Registro de cuenta",f"Error en la consulta: {str(ex)}")
            print("Error executing the query", ex)
    
    def mostrar_cuenta(self):
        try:
            db = conectar_base_de_datos()
            cursor = db.cursor()
            cursor.execute(f"SELECT * FROM cuenta ORDER BY id_cuenta")
            busqueda = cursor.fetchall()
            if len(busqueda) > 0:
                resultado_empleado("Registro de cuenta",f"Se encontraron {len(busqueda)} coincidencias.")
                cuentas(self,cursor,busqueda,QHeaderView,QTableWidget,QAbstractItemView,QTableWidgetItem,QDate,Qt)
                self.tablacuenta.clearSelection() # Deselecciona la fila
            else:
                resultado_empleado("Registro de cuenta",f"Se encontraron {len(busqueda)} coincidencias.")
                
            cursor.close()
            db.close()
        except Error as ex:
            errorConsulta("Registro de cuenta",f"Error en la consulta: {str(ex)}")
            print("Error executing the query", ex)

    def autocompleto_de_datos_tipo(self):
        row = self.tablacuenta.currentRow()
        
        nomTipo = self.tablacuenta.item(row,1).text()
        tipo = self.tablacuenta.item(row,2).text()
        descrip = self.tablacuenta.item(row,3).text()
        categor = self.tablacuenta.item(row,4).text()
        
        self.n_cuenta.setText(nomTipo)
        self.t_cuenta.setCurrentText(tipo)
        self.descripcion.setText(descrip)
        self.categoria.setText(categor)

        self.tablacuenta.clearSelection() # Deselecciona la fila

    def actualizar_cuenta(self):
        # Verificar si se ha seleccionado una fila
        if not self.tablacuenta.currentItem():
            mensaje_ingreso_datos("Registro de cuenta","Debe seleccionar la cuenta de la tabla para actualizar")
            return
        
        id_cuenta = int(self.tablacuenta.item(self.tablacuenta.currentRow(), 0).text())
        nomTipo = self.n_cuenta.text().capitalize()
        tipo = self.t_cuenta.currentText()
        descrip = self.descripcion.text().capitalize()
        categor = self.categoria.text().capitalize()
        
        patron = re.compile(r'^[a-zA-ZáéíóúÁÉÍÓÚüÜ\'\s]+$') 
        if not isinstance(nomTipo, str) or nomTipo.isspace() or not patron.match(nomTipo): 
            mensaje_ingreso_datos("Registro de cuenta","El 'nombre' debe contener:\n\n- Letras y/o espacios entre nombres(si tiene mas de dos).")
            return
        if not isinstance(tipo, str) or not tipo.isalpha():
            mensaje_ingreso_datos("Registro de cuenta","El tipo debe contener: \n- Las opciones mostradas.")
            return
        if not isinstance(descrip, str) or descrip.isspace() or not patron.match(descrip): 
            mensaje_ingreso_datos("Registro de cuenta","La descripción debe contener: \n- Solo texto.")
            return 
        if not isinstance(categor, str) or not categor.isalpha():
            mensaje_ingreso_datos("Registro de cuenta","La categoría deben contener: \n- 'Debe' o 'Haber'.")
            return 
           
        try:
            db = conectar_base_de_datos()
            cursor = db.cursor()
            cursor.execute("UPDATE cuenta SET nombre = %s, tipo = %s, descripcion = %s, categoria = %s WHERE id_cuenta = %s", (nomTipo,tipo,descrip,categor,id_cuenta))
            db.commit() 
            
            if cursor:
                mensaje_ingreso_datos("Registro de cuenta","Registro actualizado")
                self.n_cuenta.clear()
                self.t_cuenta.setCurrentIndex(0)
                self.descripcion.clear()
                self.categoria.clear()
                self.tablacuenta.clearSelection() # Deselecciona la fila
            else:
                mensaje_ingreso_datos("Registro de cuenta","Registro no actualizado")
                
            cursor.close()
            db.close() 
        
        except Error as ex:
            errorConsulta("Registro de cuenta",f"Error en la consulta: {str(ex)}")

    def eliminar_cuenta(self):
        # Primero corroborar la seleccion de la fila
        if not self.tablacuenta.currentItem():
            mensaje_ingreso_datos("Registro de cuenta","Debe buscar una cuenta a eliminar")
            return
        
        # Selecciona la fila acutal
        selectedRow = self.tablacuenta.currentItem().row()
        id_cuenta = int(self.tablacuenta.item(selectedRow, 0).text())
        
        try:
            db = conectar_base_de_datos()
            cursor = db.cursor()
            cursor.execute(f"DELETE FROM cuenta WHERE id_cuenta = {id_cuenta}")
            db.commit()
            if cursor:
                mensaje_ingreso_datos("Registro de cuenta","Registro eliminado")
                self.tablacuenta.removeRow(selectedRow)
                self.n_cuenta.clear()
                self.t_cuenta.setCurrentIndex(0)
                self.descripcion.clear()
                self.categoria.clear()
                self.tablacuenta.clearSelection() # Deselecciona la fila
            else:
                mensaje_ingreso_datos("Registro de cuenta","Registro no eliminado")  
                            
        except Error as ex:
            errorConsulta("Registro de cuenta",f"Error en la consulta: {str(ex)}")
            print("Error executing the query", ex)
        cursor.close()
        db.close()