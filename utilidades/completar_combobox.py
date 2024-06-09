from conexion_DB.dataBase import conectar_base_de_datos

def actualizar_combobox_user(self):
    conn = conectar_base_de_datos()
    cursor = conn.cursor()
    
    self.idUser.clear()
    
    # Consulta para obtener los datos de una columna específica
    cursor.execute("SELECT dni FROM usuario ORDER BY dni ASC")
    datos = cursor.fetchall()

    for resultado in datos:
        self.idUser.addItem(str(resultado[0]), resultado)
                
    cursor.close()
    conn.close()

    
def actualizar_combobox_disc(self):
    #  Conexión a la base de datos MySQL
    conn = conectar_base_de_datos()
    cursor = conn.cursor()
    
    self.idDis.clear()

    # Consulta para obtener los datos de una columna específica
    cursor.execute("SELECT id_disciplina, nombre, precio FROM disciplina ORDER BY nombre ASC")
    resultados = cursor.fetchall()

    for resultado in resultados:
        self.idDis.addItem(str(resultado[1]).capitalize().title(), resultado)
    cursor.close()
    conn.close()

# Funcion para completar el comobobox en la pestaña 'PAGO'
def completar_nombre_empleado(self):
    #  Conexión a la base de datos MySQL
    conn = conectar_base_de_datos()
    cursor = conn.cursor()
    
    self.id_horas_empleado.clear()
    cursor.execute("SELECT id_empleado, nombre, apellido FROM registro_empleado ORDER BY nombre ASC")
    resultados = cursor.fetchall()

    for resultado in resultados:
        self.id_horas_empleado.addItem(str(resultado[1]).capitalize().title(), resultado)
    
    cursor.close()
    conn.close() 
    
# Funcion para completar el comobobox en la pestaña 'consulta'
def actualizar_combobox_consulta4(self):
    #  Conexión a la base de datos MySQL
    conn = conectar_base_de_datos()
    cursor = conn.cursor()
    
    self.view_disciplina.clear()

    # Consulta para obtener los datos de una columna específica
    cursor.execute("SELECT nombre FROM disciplina ORDER BY nombre ASC")
    resultados = cursor.fetchall()

    for resultado in resultados:
        self.view_disciplina.addItem(str(resultado[0]).capitalize().title(), resultado)
    cursor.close()
    conn.close()
    
    
def actualizar_combobox_consulta1_usuario(self):
    #  Conexión a la base de datos MySQL
    conn = conectar_base_de_datos()
    cursor = conn.cursor()
    
    self.view_nomb.clear()

    # Consulta para obtener los datos de una columna específica
    cursor.execute("SELECT u.dni FROM usuario u ORDER BY u.dni ASC")
    resultados = cursor.fetchall()

    for resultado in resultados:
        self.view_nomb.addItem(str(resultado[0]).capitalize().title(), resultado)
    cursor.close()
    conn.close()
    
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