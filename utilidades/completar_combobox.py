from conexion_DB.dataBase import conectar_base_de_datos

# def actualizar_combobox_user(self):
#     conn = conectar_base_de_datos()
#     cursor = conn.cursor()
    
    
    # self.idUser.clear()
    
    # # Consulta para obtener los datos de una columna específica
    # cursor.execute("SELECT dni FROM usuario ORDER BY dni ASC")
    # datos = cursor.fetchall()

    # for resultado in datos:
    #     self.idUser.addItem(str(resultado[0]), resultado)
                
    # cursor.close()
    # conn.close()

    
# def actualizar_combobox_disc(self):
    # #  Conexión a la base de datos MySQL
    # conn = conectar_base_de_datos()
    # cursor = conn.cursor()
    
    # self.idDis.clear()

    # # Consulta para obtener los datos de una columna específica
    # cursor.execute("SELECT id_disciplina, nombre, precio FROM disciplina ORDER BY nombre ASC")
    # resultados = cursor.fetchall()
    
    # # Agregar un valor vacío al inicio del combobox
    # self.idDis.addItem("", -1)
    
    # for resultado in resultados:
    #     self.idDis.addItem(str(resultado[1]).capitalize().title(), resultado)
    # cursor.close()
    # conn.close()

# Funcion para completar el comobobox en la pestaña 'PAGO'
# def completar_nombre_empleado(self):
#     #  Conexión a la base de datos MySQL
#     conn = conectar_base_de_datos()
#     cursor = conn.cursor()
    
#     self.id_horas_empleado.clear()
#     self.id_horas_empleado.addItem("Seleccionar empleado", None)  # Añadir un elemento inicial informativo
    
#     cursor.execute("SELECT id_empleado, nombre, apellido FROM registro_empleado ORDER BY nombre ASC")
#     resultados = cursor.fetchall()

#     for resultado in resultados:
#         self.id_horas_empleado.addItem(str(resultado[1]).title(), resultado)
    
#     cursor.close()
#     conn.close() 
    
# Funcion para completar el comobobox en la pestaña 'consulta'
# def actualizar_combobox_consulta4(self):
#     #  Conexión a la base de datos MySQL
#     conn = conectar_base_de_datos()
#     cursor = conn.cursor()
    
#     self.view_disciplina.clear()

#     # Consulta para obtener los datos de una columna específica
#     cursor.execute("SELECT nombre FROM disciplina ORDER BY nombre ASC")
#     resultados = cursor.fetchall()

#     for resultado in resultados:
#         self.view_disciplina.addItem(str(resultado[0]).capitalize().title(), resultado)
#     cursor.close()
#     conn.close()
    
    
# def actualizar_combobox_consulta1_usuario(self):
#     # Conexión a la base de datos MySQL
#     conn = conectar_base_de_datos()
#     cursor = conn.cursor()
    
#     self.view_nomb.clear()
#     self.view_nomb.addItem("Selecciona un valor", None)  # Agrega un elemento predeterminado
    
#     # Consulta para obtener los datos de una columna específica
#     cursor.execute("SELECT u.dni FROM usuario u ORDER BY u.dni ASC")
#     resultados = cursor.fetchall()

#     for resultado in resultados:
#         self.view_nomb.addItem(str(resultado[0]).title(), resultado)
    
#     # self.view_nomb.currentIndexChanged.connect(self.actualizar_campo_texto_combobox)  # Conecta la señal de cambio de índice
    
#     cursor.close()
#     conn.close()

# def actualizar_campo_texto_combobox(self, index):
#     if index > 0:
#         self.view_nomb_texto.setText(str(self.view_nomb.currentText()))  # Actualiza el campo de texto con el valor seleccionado
#     else:
#         self.view_nomb_texto.setText("Selecciona un valor")  # Restablece el texto predeterminado
    
#     self.view_nomb_texto.setReadOnly(True)  # Establece el campo de texto como de solo lectura
    
# def actualizar_combobox_IDcuenta(self):
#     #  Conexión a la base de datos MySQL
#     conn = conectar_base_de_datos()
#     cursor = conn.cursor()
    
#     self.cuenta.clear()

#     # Consulta para obtener los datos de una columna específica
#     cursor.execute("SELECT * FROM cuenta c ORDER BY c.id_cuenta ASC")
#     resultados = cursor.fetchall()

#     for resultado in resultados:
#         self.cuenta.addItem(str(resultado[0]), resultado)

#     cursor.close()
#     conn.close()
    
# def actualizar_combobox_cuentaHaber(self):
#     #  Conexión a la base de datos MySQL
#     conn = conectar_base_de_datos()
#     cursor = conn.cursor()
    
#     self.concepto_haber.clear()

#     # Consulta para obtener los datos de una columna específica
#     cursor.execute("SELECT c.nombre FROM cuenta c WHERE categoria = 'haber' ORDER BY c.nombre ASC")
#     resultados = cursor.fetchall()

#     for resultado in resultados:
#         self.concepto_haber.addItem(str(resultado[0]).capitalize().title(), resultado)
#     cursor.close()
#     conn.close()

# Conexión a la base de datos MySQL
    # conn = conectar_base_de_datos()
    # cursor = conn.cursor()

    # # Consulta para obtener los datos de una columna específica
    # cursor.execute("SELECT dni FROM usuario ORDER BY dni ASC'")
    # dato = cursor.fetchall()
    # sugerencia = [str(item[0]) for item in dato]

    # self.idUser = QLineEdit(sugerencia)
    # self.idUser.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
    # self.idUser.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)
    # self.idUser.popup().setStyleSheet(style.completer)
    # self.concepto_debe.setCompleter(self.idUser)
    
    # cursor.close()
    # conn.close()
    


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.view_nomb = QComboBox(self)
#         self.view_nomb.setPlaceholderText("Seleccionar un DNI")
#         self.view_nomb.activated.connect(self.on_item_selected)
#         self.view_nomb.view().showEvent = self.load_items

#         layout = QVBoxLayout()
#         layout.addWidget(self.view_nomb)
        
#         container = QWidget()
#         container.setLayout(layout)
#         self.setCentralWidget(container)

#     def load_items(self, event):
#         # Conexión a la base de datos MySQL
#         conn = conectar_base_de_datos()
#         cursor = conn.cursor()

#         # Consulta para obtener los datos de una columna específica
#         cursor.execute("SELECT u.dni FROM usuario u ORDER BY u.dni ASC")
#         resultados = cursor.fetchall()

#         self.view_nomb.clear()
#         self.view_nomb.addItem("Seleccionar un DNI", None)  # Agrega un elemento predeterminado

#         for resultado in resultados:
#             self.view_nomb.addItem(str(resultado[0]), resultado)

#         cursor.close()
#         conn.close()

#     def on_item_selected(self):
#         current_text = self.view_nomb.currentText()
#         if current_text != "Seleccionar un DNI":
#             print(f"Seleccionado: {current_text}")
#             self.view_nomb.setCurrentIndex(0)
#             self.view_nomb.setPlaceholderText("Seleccionar un DNI")

