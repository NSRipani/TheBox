from modulos.mensajes import mensaje_ingreso_datos,aviso_descargaExitosa,aviso_Advertencia_De_excel
import re


# from openpyxl import Workbook

def registroUSER(nombre1 , apellido1, dni, sexo, edad, celu):
    patron = re.compile(r'^[a-zA-ZáéíóúÁÉÍÓÚüÜ\'\s]+$') 
    if not isinstance(nombre1, str) or nombre1.isspace() or not patron.match(nombre1): #'match' -> verificar si la cadena coincide con este patrón.
        mensaje_ingreso_datos("Registro de alumnos","El 'nombre' debe contener:\n\n- Letras y/o espacios entre nombres(si tiene mas de dos).")
        return

    if not isinstance(apellido1, str) or apellido1.isspace() or not patron.match(apellido1):
        mensaje_ingreso_datos("Registro de alumnos","El 'apellido' debe contener:\n\n- Letras y/o espacios entre nombres(si tiene mas de dos).")
        return

    patron2 = re.compile(r'^[0-9]+$')
    if not dni.isdigit() or not len(dni) == 8 or not patron2.match(dni):
        mensaje_ingreso_datos("Registro de empleado","El 'DNI' debe ser:\n\n- Numérico y contener 8 números enteros")
        return   

    if not (isinstance(sexo, str) and patron.match(sexo)):
        mensaje_ingreso_datos("Registro de alumnos","Debe elegir una sexo")
        return
    
    if not edad.isdigit() or not len(edad) == 2 or not patron2.match(edad):
        mensaje_ingreso_datos("Registro de alumnos","La 'edad' debe ser:\n\n- Valores numéricos.\n- Contener 2 dígitos.\n- No contener puntos(.)")
        return
    edad = int(edad)

    if not (celu.isdigit() and patron2.match(celu)):
        mensaje_ingreso_datos("Registro de alumnos","El 'celular' debe ser:\n\n- Valores numéricos.\n- Contener 10 dígitos.\n- No contener puntos(.)")
        return
    
def limpiasElementosUser(self,QDate):
    self.input_nombre1.clear()
    self.input_apellido1.clear()
    self.input_dni.clear()
    self.input_sex.setCurrentIndex(0)
    self.input_age.clear()
    self.input_celular.clear()
    self.input_date.setDate(QDate.currentDate())
    
def limpiar_campos(self):
    if not self.tablaUpdateRecord.currentItem():
        mensaje_ingreso_datos("Registro de alumnos","Los campos deben esta completados para limparlos")
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

    self.tablaUpdateRecord.clearSelection()  # Deseleccionar la fila eliminada

def limpiar_tablaRecord(self):  
    # Obtener el número de filas de la tabla
    filas = self.tablaRecord.rowCount()

    # Eliminar todas las filas de la tabla
    for i in range(filas):
        self.tablaRecord.removeRow(0)  # Eliminar la fila en la posición 0
        
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
    
def actualizarUSER(nombre2 , apellido2, dni2, sexo2, edad2, celu2):
    patron_Letras = re.compile(r'^[a-zA-ZáéíóúÁÉÍÓÚüÜ\'\s]+$') 
    if not isinstance(nombre2, str) or nombre2.isspace() or not patron_Letras.match(nombre2):
        mensaje_ingreso_datos("Registro de alumnos","El 'nombre' solo debe contener letras y/o espacios")
        return

    if not isinstance(apellido2, str) or apellido2.isspace() or not patron_Letras.match(apellido2):
        mensaje_ingreso_datos("Registro de alumnos","El 'apellido' solo debe contener letras y/o espacios")
        return
    
    patronNum = re.compile(r'^[0-9]+$')
    if not (dni2.isnumeric() and len(dni2) == 8 and patronNum.match(dni2)):
        mensaje_ingreso_datos("Registro de alumnos","El 'DNI' debe ser:\n- Valores numéricos.\n- Contener 8 dígitos.\n- No contener puntos(.)")
        return
    dni2 = int(dni2)    

    if not (isinstance(sexo2, str) and patron_Letras.match(sexo2)):
        mensaje_ingreso_datos("Registro de alumnos","Debe elegir una sexo")
        return
    
    if not (edad2.isnumeric() and len(edad2) == 2 and patronNum.match(edad2)):
        mensaje_ingreso_datos("Registro de alumnos","El 'edad' debe ser:\n- Valores numéricos.\n- Contener 2 dígitos.\n- No contener puntos(.)")
        return
    edad2 = int(edad2)
    
    if not (celu2.isnumeric() and patronNum.match(celu2)):
        mensaje_ingreso_datos("Registro de alumnos","El 'celular' debe ser: \n- Valores numéricos. \n- Contener 10 dígitos.\n- No contener puntos(.)")
        return
    
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
            if j in [0, 3, 5, 6, 7]:  # Ajustar alineación para ciertas columnas
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.tablaRecord.setItem(i, j, item)