# conexion
from conexion_DB.dataBase import conectar_base_de_datos 
# from modulos.mensajes import mensaje_ingreso_datos
from qss import style
# import re
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QCompleter

# "def validar_datos(self, nomTipo, tipo, descrip, categor):
#     nomTipo = nomTipo.strip()
#     if not (nomTipo != "" and nomTipo.replace("", " ") and isinstance(nomTipo, str) and re.findall(r'^[a-zA-ZáéíóúÁÉÍÓÚüÜ\'\s]+$',nomTipo)):
#         mensaje_ingreso_datos("Registro de cuenta","El 'Nombre' debe corresponder a una cuenta contable")
#         self.n_cuenta.setFocus()
#         return
    
#     if not isinstance(tipo, str) or not tipo.isalpha():
#         mensaje_ingreso_datos("Registro de cuenta","El Tipo debe contener:\n\n- Activo.\n- Pasivo.\n- Ingreso.\n- Engreso.\n- Patrimonio.")
#         return
#     sugerencia = actualizar_combobox_TipoCUENTA(self,QCompleter,Qt,style)
#     if tipo not in sugerencia: 
#         mensaje_ingreso_datos("Registro de cuenta", "Debe elegir el tipo de cuenta de la lista de sugerencias")
#         return
    
#     descrip = descrip.strip()
#     if not (descrip != "" and descrip.replace("", " ") and isinstance(descrip, str) and re.findall(r'^[a-zA-ZáéíóúÁÉÍÓÚüÜ\'\s]+$',descrip)):
#         mensaje_ingreso_datos("Registro de cuenta","La Descripción debe contener:\n\n- Solo texto.")
#         self.descripcion.setFocus()
#         return
        
#     if not isinstance(categor, str) or not categor.isalpha():
#         mensaje_ingreso_datos("Registro de cuenta","La Categoría deben contener:\n\n- 'Debe' o 'Haber'.")
#         return 
#     debe_haber = actualizar_combobox_Categoria(self,QCompleter,Qt,style)
#     if categor not in debe_haber: 
#         mensaje_ingreso_datos("Registro de cuenta", "Debe elegir la categoria('debe' o 'haber') correspondiente\na la cuenta a crear y a la lista de sugerencias")
#         return

#     return "Validación exitosa

def actualizar_combobox_TipoCUENTA(self):
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
    
def actualizar_combobox_Categoria(self):
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