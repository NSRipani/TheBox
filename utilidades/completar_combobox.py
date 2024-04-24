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
