from modulos.mensajes import mensaje_ingreso_datos

def variables(re,nom_emp,apell_emp,sex_emp,dni_emp,cel):
    patron_mun = re.compile(r'^[0-9]+$')
    patron_alpha = re.compile(r'^[a-zA-ZáéíóúÁÉÍÓÚüÜ\'\s]+$') 
    if not isinstance(nom_emp, str) or nom_emp.isspace() or not patron_alpha.match(nom_emp):
        mensaje_ingreso_datos("Registro de empleado","El nombre debe contener: \n- Letras y/o espacios entre nombres(si tiene mas de dos).")
        return
    
    if not isinstance(apell_emp, str) or apell_emp.isspace() or not patron_alpha.match(apell_emp):
        mensaje_ingreso_datos("Registro de empleado","El apellido debe contener: \n- Letras y/o espacios entre nombres(si tiene mas de dos).")
        return  
    
    if not (sex_emp.isalpha() and patron_alpha.match(sex_emp)):
        mensaje_ingreso_datos("Registro de empleado","Debe elegir el sexo.")
        return   
    
    if not (dni_emp.isnumeric() and len(dni_emp) == 8 and patron_mun.match(dni_emp)):
        mensaje_ingreso_datos("Registro de empleado","El DNI debe ser numérico y contener 8 números enteros")
        return
    dni_emp = int(dni_emp)
        
    if not (cel.isnumeric() and len(cel) == 10 and patron_mun.match(cel)):
        mensaje_ingreso_datos("Registro de empleado","El celular debe ser numérico y contener 10 números enteros")
        return
    
def lim_campos(self,QDate):
    self.nombre_emp.clear()
    self.apellido_emp.clear()
    self.sexo_emp.clear()
    self.dni_emp.clear()
    self.celular_emp.clear()
    self.fecha.setDate(QDate.currentDate())
    
def seleccion_DeTabla(self,QDate):
    fila = self.tablaEmp.currentRow()
    
    nom_emp = self.tablaEmp.item(fila,1).text()
    apell_emp = self.tablaEmp.item(fila,2).text()
    sex_emp = self.tablaEmp.item(fila,3).text()
    dni_emp = self.tablaEmp.item(fila,4).text()
    cel = self.tablaEmp.item(fila,5).text()
    fecha = self.tablaEmp.item(fila,6).text()
    fecha = QDate.fromString(fecha,"dd-MM-yyyy")
    
    self.nombre_emp.setText(nom_emp)
    self.apellido_emp.setText(apell_emp)
    self.sexo_emp.setText(sex_emp)
    self.dni_emp.setText(dni_emp)
    self.celular_emp.setText(cel)
    self.fecha.setDate(fecha)

    self.tablaEmp.clearSelection() # Deselecciona la fila

def verTabla(self,cursor,busqueda,QHeaderView,QTableWidget,QAbstractItemView,QTableWidgetItem,QDate,Qt):
    headers = [description[0].replace('_', ' ').upper() for description in cursor.description]
    
    self.tablaEmp.setRowCount(len(busqueda))
    self.tablaEmp.setColumnCount(len(busqueda[0]))
    self.tablaEmp.setHorizontalHeaderLabels(headers)
    
    # Establecer la propiedad de "stretch" en el encabezado horizontal
    header = self.tablaEmp.horizontalHeader()
    header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    header.setAutoScroll(True)
    
    titulosV = self.tablaEmp.verticalHeader()
    titulosV.setVisible(False)
    
    # Ajustar el tamaño de las filas para que se ajusten al contenido
    self.tablaEmp.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
    self.tablaEmp.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
    self.tablaEmp.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        
    for i, row in enumerate(busqueda):
        for j, val in enumerate(row):
            item = QTableWidgetItem(str(val))
            
            # Indices de las columnas que contienen fechas
            if j == 6:  
                fecha = QDate.fromString(str(val), "yyyy-MM-dd")  # Convertir la fecha a objeto QDate
                item.setText(fecha.toString("dd-MM-yyyy"))  # Establecer el formato de visualización
            
            if j in [0,4,5,6]:  # Ajustar alineación para ciertas columnas
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)   
            self.tablaEmp.setItem(i, j, item)
            
def clearTabla(self):
    # Obtener el número de filas de la tabla
    num_filas = self.tablaEmp.rowCount()

    # Eliminar todas las filas de la tabla
    for i in range(num_filas):
        self.tablaEmp.removeRow(0) 