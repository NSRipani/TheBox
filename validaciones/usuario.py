from modulos.mensajes import mensaje_ingreso_datos,ingreso
import re
from qss.style_item import itemColor_RESULTADO, itemColor_TOTAL


def registroUSER(self,nombre1, apellido1, dni, sexo, edad, celu):
    
    nombre1 = nombre1.strip()
    if not (nombre1 != "" and nombre1.replace("", " ") and isinstance(nombre1, str) and re.findall(r'^[a-zA-ZáéíóúÁÉÍÓÚüÜ\'\s]+$',nombre1)):
        mensaje_ingreso_datos("Registro de cliente","El 'Nombre' debe contener:\n\n- Letras y/o espacios entre nombres(si tiene mas de dos).")
        self.input_nombre1.setFocus()
        return
    
    apellido1 = apellido1.strip()
    if not (apellido1 != "" and apellido1.replace("", " ") and isinstance(apellido1, str) and re.findall(r'^[a-zA-ZáéíóúÁÉÍÓÚüÜ\'\s]+$',apellido1)):
        mensaje_ingreso_datos("Registro de cliente","El 'apellido' debe contener:\n\n- Letras y/o espacios entre nombres(si tiene mas de dos).")
        self.input_apellido1.setFocus()
        return
    
    patron_dni = re.compile(r'^\d{8}$')
    if not dni.isdigit() or not patron_dni.match(dni) or not len(dni) == 8:#or not len(dni) == 8
        mensaje_ingreso_datos("Registro de cliente","El DNI debe contener: \n\n- Números enteros (8).\n- No contener puntos(.)")
        self.input_dni.setFocus()
        return
    try:
        if dni:
            dni = int(dni)
    except ValueError:
        mensaje_ingreso_datos("Registro de cliente","El Celular debe ser numérico")
        return
    
    if not isinstance(sexo, str) or not sexo.isalpha():
        mensaje_ingreso_datos("Registro de cliente","Debe elegir un sexo.\n\nEl sexo es 'Hombre' o 'Mujer'")
        return
    if sexo:
        sexo = sexo.capitalize()    
    
    patron_edad = re.compile(r'^\d{2}$')
    if not edad.isdigit() or not len(edad) == 2 or not patron_edad.match(edad):
        mensaje_ingreso_datos("Registro de cliente","La Edad debe contener:\n\n- Contener 2 (DOS) números enteros.\n- No contener puntos(.)")
        self.input_age.setFocus()
        return
    try:
        if edad:
            edad = int(edad)
    except ValueError:
        mensaje_ingreso_datos("Registro de cliente","El Celular debe ser numérico")
        return
            
    patron_celu = re.compile(r'^[0-9]+$')
    if not (celu.isdigit() and patron_celu.match(celu)):
        mensaje_ingreso_datos("Registro de cliente","El Celular debe ser:\n\n- Números enteros.\n- No contener puntos(.)")
        self.input_celular.setFocus()
        return
    try:
        if celu:
            celu = int(celu)
            print(f"El celular es {celu}")
    except ValueError:
        mensaje_ingreso_datos("Registro de cliente","El Celular debe ser numérico")
        return
    
    return "Validación exitosa."
    
def limpiasElementosUser(self,QDate):
    self.input_nombre1.clear()
    self.input_apellido1.clear()
    self.input_dni.clear()
    self.input_sex.setCurrentIndex(0)
    self.input_age.clear()
    self.input_celular.clear()
    self.input_date.setDate(QDate.currentDate())

def limpiar_tablaRecord(self):  
    # Obtener el número de filas de la tabla
    filas = self.tablaRecord.rowCount()

    # Eliminar todas las filas de la tabla
    for i in range(filas):
        self.tablaRecord.removeRow(0)  # Eliminar la fila en la posición 0
    
def limpiar_campos(self):
    if not self.tablaUpdateRecord.currentItem():
        mensaje_ingreso_datos("Registro de cliente","Los campos deben esta completados para limparlos")
        return
    
    # self.id2.clear()
    self.input_nombre2.clear()
    self.input_apellido2.clear()
    self.input_dni2.clear()
    self.input_sex2.setCurrentIndex(0)
    self.input_age2.clear()
    self.input_celular2.clear()
    
    self.input_apellido2.setEnabled(False)
    self.input_dni2.setEnabled(False)
    self.input_sex2.setEnabled(False)
    self.input_age2.setEnabled(False)
    self.input_date2.setEnabled(False)
    self.input_celular2.setEnabled(False)
    
def autoCompletadoACTULIZAR(self,QDate):
    row = self.tablaUpdateRecord.currentRow()
    
    nombre2 = self.tablaUpdateRecord.item(row, 1).text()
    apellido2 = self.tablaUpdateRecord.item(row, 2).text()
    dni2 = self.tablaUpdateRecord.item(row, 3).text().replace(".", "")  # Eliminar cualquier punto en el DNI
    sexo2 = self.tablaUpdateRecord.item(row, 4).text()
    edad2 = self.tablaUpdateRecord.item(row, 5).text().replace(".", "")
    edad2 = int(edad2)
    celular2 = self.tablaUpdateRecord.item(row, 6).text()
    fecha2 = self.tablaUpdateRecord.item(row, 7).text()
    fecha2 = QDate.fromString(fecha2, "dd-MM-yyyy")
    
    self.input_apellido2.setEnabled(True)
    self.input_dni2.setEnabled(True)
    self.input_sex2.setEnabled(True)
    self.input_age2.setEnabled(True)
    self.input_date2.setEnabled(True)
    self.input_celular2.setEnabled(True) 
    
    self.input_nombre2.setText(nombre2)  
    self.input_apellido2.setText(apellido2)
    self.input_dni2.setText(dni2)  # Convertir a texto antes de asignar al QLineEdit
    self.input_sex2.setCurrentText(sexo2)
    self.input_age2.setText(str(edad2))  # Convertir a texto antes de asignar al QLineEdit
    self.input_celular2.setText(celular2)  # Convertir a texto antes de asignar al QLineEdit
    self.input_date2.setDate(fecha2)

    # self.tablaUpdateRecord.clearSelection()  # Deseleccionar la fila eliminada

def actualizacionUSER(self,nombre2, apellido2, dni2, sexo2, edad2, celu2):
    
    nombre2 = nombre2.strip()
    if not (nombre2 != "" and nombre2.replace("", " ") and isinstance(nombre2, str) and re.findall(r'^[a-zA-ZáéíóúÁÉÍÓÚüÜ\'\s]+$',nombre2)):
        mensaje_ingreso_datos("Registro de cliente","El 'Nombre' debe contener:\n\n- Letras y/o espacios entre nombres(si tiene mas de dos).")
        self.input_nombre2.setFocus()
        return
    
    apellido2 = apellido2.strip()
    if not (apellido2 != "" and apellido2.replace("", " ") and isinstance(apellido2, str) and re.findall(r'^[a-zA-ZáéíóúÁÉÍÓÚüÜ\'\s]+$',apellido2)):
        mensaje_ingreso_datos("Registro de cliente","El 'apellido' debe contener:\n\n- Letras y/o espacios entre nombres(si tiene mas de dos).")
        self.input_apellido2.setFocus()
        return
    
    patron_dni = re.compile(r'^\d{8}$')
    if not dni2.isdigit() or not patron_dni.match(dni2) or not len(dni2) == 8:#or not len(dni) == 8
        mensaje_ingreso_datos("Registro de cliente","El DNI debe contener: \n\n- Números enteros (8).\n- No contener puntos(.)")
        self.input_dni.setFocus()
        return
    try:
        if dni2:
            dni2 = int(dni2)
    except ValueError:
        mensaje_ingreso_datos("Registro de cliente","El Celular debe ser numérico")
        return
    
    if not isinstance(sexo2, str) or not sexo2.isalpha():
        mensaje_ingreso_datos("Registro de cliente","Debe elegir un sexo.\n\nEl sexo es 'Hombre' o 'Mujer'")
        return
    if sexo2:
        sexo2 = sexo2.capitalize()    
    
    patron_edad = re.compile(r'^\d{2}$')
    if not edad2.isdigit() or not len(edad2) == 2 or not patron_edad.match(edad2):
        mensaje_ingreso_datos("Registro de cliente","La Edad debe contener:\n\n- Contener 2 (DOS) números enteros.\n- No contener puntos(.)")
        self.input_age2.setFocus()
        return
    try:
        if edad2:
            edad2 = int(edad2)
    except ValueError:
        mensaje_ingreso_datos("Registro de cliente","El Celular debe ser numérico")
        return
            
    patron_celu = re.compile(r'^[0-9]+$')
    if not (celu2.isdigit() and patron_celu.match(celu2)):
        mensaje_ingreso_datos("Registro de cliente","El Celular debe ser:\n\n- Números enteros.\n- No contener puntos(.)")
        self.input_celular2.setFocus()
        return
    try:
        if celu2:
            celu2 = int(celu2)
            print(f"El celular es {celu2}")
    except ValueError:
        mensaje_ingreso_datos("Registro de cliente","El Celular debe ser numérico")
        return
    
    return "Validación exitosa."

        
def limpiar_tablaUpdate(self):
    # Obtener el número de filas de la tabla
    filas = self.tablaUpdateRecord.rowCount()

    # Eliminar todas las filas de la tabla
    for i in range(filas):
        self.tablaUpdateRecord.removeRow(0)  # Eliminar la fila en la posición 0
        
    self.tablaUpdateRecord.setEnabled(False)
    self.input_apellido2.setEnabled(False)
    self.input_dni2.setEnabled(False)
    self.input_sex2.setEnabled(False)
    self.input_age2.setEnabled(False)
    self.input_date2.setEnabled(False)
    self.input_celular2.setEnabled(False)
    
def limpiasElementosUseraActualizar(self,QDate):
    self.input_nombre2.clear()
    self.input_apellido2.clear()
    self.input_dni2.clear()
    self.input_sex2.setCurrentIndex(0)
    self.input_age2.clear()
    self.input_celular2.clear()
    self.input_date2.setDate(QDate.currentDate())
    
def tabla_registroUSER(self, cursor, resultados, QHeaderView, QTableWidget, QAbstractItemView, QTableWidgetItem, QDate, Qt):
    headers = [description[0].upper().replace("_"," ") for description in cursor.description]
    
    self.tablaRecord.setRowCount(len(resultados))
    self.tablaRecord.setColumnCount(len(resultados[0]))
    self.tablaRecord.setHorizontalHeaderLabels(headers)
    
    # Establecer la propiedad de "stretch" en el encabezado horizontal
    header = self.tablaRecord.horizontalHeader()
    header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    
    # Obtener la instancia del encabezado vertical
    vertical_header = self.tablaRecord.verticalHeader()
    vertical_header.setVisible(False)

    self.tablaRecord.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
    self.tablaRecord.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
    
    for i, row in enumerate(resultados):
        for j, val in enumerate(row):
            item = QTableWidgetItem(str(val))
            # Indices de las columnas que contienen fechas
            if j == 7:  
                fecha = QDate.fromString(str(val), "yyyy-MM-dd")  # Convertir la fecha a objeto QDate
                item.setText(fecha.toString("dd-MM-yyyy"))  # Establecer el formato de visualización
            if j in [0, 3, 5, 6,7]:  # Ajustar alineación para ciertas columnas
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.tablaRecord.setItem(i, j, item)
    
    # Calcular la cantidad total de registros
    total_registros = sum(1 for row in resultados if row[1])

    # Crear una nueva fila en la tabla para mostrar la cantidad total de días de asistencia
    row_count = self.tablaRecord.rowCount()
    self.tablaRecord.insertRow(row_count) # Agregar la nueva fila al final de la tabla

    # Mostrar la etiqueta "Total" en la primera celda de la fila de total
    item_label = QTableWidgetItem("TOTAL:")
    item_label.setFont(itemColor_TOTAL(item_label)) # Funcion para estilos de item
    item_label.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
    self.tablaRecord.setItem(row_count, 0, item_label)
    
    # Agregar la información de la cantidad total de días de asistencia en la nueva fila
    item_registros = QTableWidgetItem(str(total_registros))
    item_registros.setFont(itemColor_RESULTADO(item_registros)) # Funcion para estilos de item
    item_registros.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
    self.tablaRecord.setItem(row_count, 1, item_registros)  # Agregar en la primera columna o en la que desees