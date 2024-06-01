# conexion
from conexion_DB.dataBase import conectar_base_de_datos 


def actualizar_combobox_TipoCUENTA(self):
    #  Conexión a la base de datos MySQL
    conn = conectar_base_de_datos()
    cursor = conn.cursor()
    
    self.t_cuenta.clear()

    # Consulta para obtener los datos de una columna específica
    cursor.execute("SELECT nombre FROM tipo ORDER BY nombre ASC")
    resultados = cursor.fetchall()

    for resultado in resultados:
        self.t_cuenta.addItem(str(resultado[0]).capitalize().title(), resultado)
    cursor.close()
    conn.close()