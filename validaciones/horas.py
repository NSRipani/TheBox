from qss.style_item import itemColor_RESULTADO,itemColor_TOTAL

def tabla_General(self,cursor,busqueda,QHeaderView,QTableWidget,QAbstractItemView,QTableWidgetItem,Qt,QDate):
    headers = [description[0].replace('_', ' ').upper() for description in cursor.description]
                
    self.tablaHoras.setRowCount(len(busqueda))
    self.tablaHoras.setColumnCount(len(busqueda[0]))
    self.tablaHoras.setHorizontalHeaderLabels(headers)
    
    # Establecer la propiedad de "stretch" en el encabezado horizontal
    header = self.tablaHoras.horizontalHeader()
    header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    header.setAutoScroll(True)
    
    vert_header = self.tablaHoras.verticalHeader()
    vert_header.setVisible(False)
    
    # Ajustar el tamaño de las filas para que se ajusten al contenido
    self.tablaHoras.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
    self.tablaHoras.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
    self.tablaHoras.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        
    self.tablaHoras.setRowCount(len(busqueda) + 1)   
    
    for i, row in enumerate(busqueda):
        for j, val in enumerate(row):
            item = QTableWidgetItem(str(val))
            
            # Indices de las columnas que contienen fechas
            if j == 4:  
                fecha = QDate.fromString(str(val), "yyyy-MM-dd")  # Convertir la fecha a objeto QDate
                item.setText(fecha.toString("dd-MM-yyyy"))  # Establecer el formato de visualización
            
            if j in [0,1,3,4]:  # Ajustar alineación para ciertas columnas
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)   
            self.tablaHoras.setItem(i, j, item)
    
    # Calcular y mostrar la suma de las horas diarias en la fila adicional
    total_horas = sum(int(row[3]) for row in busqueda)
    motrar_total_horas2 = QTableWidgetItem('TOTAL:')
    motrar_total_horas2.setFont(itemColor_TOTAL(motrar_total_horas2))  # Funcion para estilos de item
    motrar_total_horas2.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
    self.tablaHoras.setItem(len(busqueda), 2, motrar_total_horas2)
    
    suma_horas2 = QTableWidgetItem(str(total_horas))
    suma_horas2.setFont(itemColor_RESULTADO(suma_horas2))  # Funcion para estilos de item
    suma_horas2.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
    self.tablaHoras.setItem(len(busqueda), 3, suma_horas2)
                
def clearTabla(self):
    # Obtener el número de filas de la tabla
    num_filas = self.tablaHoras.rowCount()

    # Eliminar todas las filas de la tabla
    for i in range(num_filas):
        self.tablaHoras.removeRow(0)
    
def autoCompletado(self,QDate,mensaje_ingreso_datos):
    fila = self.tablaHoras.currentRow()
    if fila == -1:  # Verifica si no se ha seleccionado ninguna fila
        return

    # Verifica si la fila seleccionada es la última fila de la tabla
    if fila == self.tablaHoras.rowCount() - 1:
        mensaje_ingreso_datos("Registro de Ingresos-Egresos","La última fila no debe ser precionada")
        return
    
    emple = self.tablaHoras.item(fila,2).text()
    horas_h = self.tablaHoras.item(fila,3).text()
    fecha_h = self.tablaHoras.item(fila, 4).text()
    fecha_h = QDate.fromString(fecha_h, "dd-MM-yyyy")

    # Autocompletar los QLineEdits y la fecha
    self.id_horas_empleado.setCurrentText(emple)
    self.horas_tra.setText(horas_h)
    self.fecha_tra.setDate(fecha_h)

    self.tablaHoras.clearSelection() # Deselecciona la fila

def tabla_HorasXEmpleado(self,cursor,busqueda,QHeaderView,QTableWidget,QAbstractItemView,QTableWidgetItem,Qt,QDate):
    headers = [description[0].replace('_', ' ').upper() for description in cursor.description]
                
    self.tablaHoras.setRowCount(len(busqueda))
    self.tablaHoras.setColumnCount(len(busqueda[0]))
    self.tablaHoras.setHorizontalHeaderLabels(headers)
    
    # Establecer la propiedad de "stretch" en el encabezado horizontal
    header = self.tablaHoras.horizontalHeader()
    header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    header.setAutoScroll(True)
    
    encabezados_very = self.tablaHoras.verticalHeader()
    encabezados_very.setVisible(False)
    
    # Ajustar el tamaño de las filas para que se ajusten al contenido
    self.tablaHoras.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
    self.tablaHoras.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
    self.tablaHoras.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        
    self.tablaHoras.setRowCount(len(busqueda) + 1)
    for i, row in enumerate(busqueda):
        for j, val in enumerate(row):
            item = QTableWidgetItem(str(val))
            
            #Indices de las columnas que contienen fechas
            if j == 4:  
                fecha = QDate.fromString(str(val), "yyyy-MM-dd")  # Convertir la fecha a objeto QDate
                item.setText(fecha.toString("dd-MM-yyyy"))  # Establecer el formato de visualización
            
            if j in [0,3,4]:  # Ajustar alineación para ciertas columnas
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)   
            self.tablaHoras.setItem(i, j, item)
        
    # Calcular y mostrar la suma de las horas diarias en la fila adicional
    total_horas = sum(int(row[3]) for row in busqueda)
    total_horas_empleados = QTableWidgetItem('TOTAL:')
    total_horas_empleados.setFont(itemColor_TOTAL(total_horas_empleados))  # Funcion para estilos de item
    total_horas_empleados.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
    self.tablaHoras.setItem(len(busqueda), 2, total_horas_empleados)
    
    item_seuma_horas = QTableWidgetItem(str(total_horas))
    item_seuma_horas.setFont(itemColor_RESULTADO(item_seuma_horas))  # Funcion para estilos de item
    item_seuma_horas.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
    self.tablaHoras.setItem(len(busqueda), 3, item_seuma_horas)

def tabla_HorasTotales(self,cursor,busqueda,QHeaderView,QTableWidget,QAbstractItemView,QTableWidgetItem,Qt,QDate):
    headers = [description[0].replace('_', ' ').upper() for description in cursor.description]
                
    self.tablaHoras.setRowCount(len(busqueda))
    self.tablaHoras.setColumnCount(len(busqueda[0]))
    self.tablaHoras.setHorizontalHeaderLabels(headers)
    
    # Establecer la propiedad de "stretch" en el encabezado horizontal
    header = self.tablaHoras.horizontalHeader()
    header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    
    encabezados_very = self.tablaHoras.verticalHeader()
    encabezados_very.setVisible(False)
    
    # Ajustar el tamaño de las filas para que se ajusten al contenido
    self.tablaHoras.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
    self.tablaHoras.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
    self.tablaHoras.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
    
    self.tablaHoras.setRowCount(len(busqueda) + 1)   
    for i, row in enumerate(busqueda):
        for j, val in enumerate(row):
            item = QTableWidgetItem(str(val))
            
            #Indices de las columnas que contienen fechas
            if j == 4:  
                fecha = QDate.fromString(str(val), "yyyy-MM-dd")  # Convertir la fecha a objeto QDate
                item.setText(fecha.toString("dd-MM-yyyy"))  # Establecer el formato de visualización
            
            if j in [0,3,4]:  # Ajustar alineación para ciertas columnas
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)   
            self.tablaHoras.setItem(i, j, item)
            
        # Calcular y mostrar la suma de las horas diarias en la fila adicional
        total_horas = sum(int(row[3]) for row in busqueda)
        item_total_horas2 = QTableWidgetItem('TOTAL:')
        item_total_horas2.setFont(itemColor_TOTAL(item_total_horas2))  # Funcion para estilos de item
        item_total_horas2.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tablaHoras.setItem(len(busqueda), 2, item_total_horas2)
        
        item_suma_horas2 = QTableWidgetItem(str(total_horas))
        item_suma_horas2.setFont(itemColor_RESULTADO(item_suma_horas2))  # Funcion para estilos de item
        item_suma_horas2.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tablaHoras.setItem(len(busqueda), 3, item_suma_horas2)