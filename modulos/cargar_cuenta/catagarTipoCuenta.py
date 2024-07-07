# conexion
from conexion_DB.dataBase import conectar_base_de_datos 


def actualizar_combobox_TipoCUENTA(self,QCompleter,Qt,style):
    #  Conexión a la base de datos MySQL
    conn = conectar_base_de_datos()
    cursor = conn.cursor()
    
    self.t_cuenta.clear()

    # Consulta para obtener los datos de una columna específica
    cursor.execute("SELECT nombre FROM tipo ORDER BY nombre ASC")
    resultados = cursor.fetchall()

    sugerencia = [str(item[0]) for item in resultados]

    lista_nombre = QCompleter(sugerencia)
    lista_nombre.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
    lista_nombre.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)
    lista_nombre.popup().setStyleSheet(style.completer)
    self.t_cuenta.setCompleter(lista_nombre)

    cursor.close()
    conn.close()
    
    return sugerencia
    
def actualizar_combobox_Categoria(self,QCompleter,Qt,style):
    #  Conexión a la base de datos MySQL
    conn = conectar_base_de_datos()
    cursor = conn.cursor()
    
    self.categoria.clear()

    # Consulta para obtener los datos de una columna específica
    cursor.execute("SELECT nombre FROM categoria ORDER BY nombre ASC")
    resultados = cursor.fetchall()

    debe_haber = [str(item[0]) for item in resultados]

    categoria = QCompleter(debe_haber)
    categoria.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
    categoria.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)
    categoria.popup().setStyleSheet(style.completer)
    self.categoria.setCompleter(categoria)

    cursor.close()
    conn.close()
    
    return debe_haber