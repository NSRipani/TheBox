def tabla_updateUSER(self, cursor, resultados, QHeaderView, QTableWidget, QAbstractItemView, QTableWidgetItem, QDate, Qt):
    headers = [description[0].replace("_"," ").upper() for description in cursor.description]
    
    self.tablaUpdateRecord.setRowCount(len(resultados))
    self.tablaUpdateRecord.setColumnCount(len(resultados[0]))
    self.tablaUpdateRecord.setHorizontalHeaderLabels(headers)
    
    # Establecer la propiedad de "stretch" en el encabezado horizontal
    header = self.tablaUpdateRecord.horizontalHeader()
    header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    
    # Obtener la instancia del encabezado vertical
    vertical_header = self.tablaUpdateRecord.verticalHeader()
    vertical_header.setVisible(False)
    
    self.tablaUpdateRecord.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
    self.tablaUpdateRecord.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
    
    for i, row in enumerate(resultados):
        for j, val in enumerate(row):
            item = QTableWidgetItem(str(val))
            # Indices de las columnas que contienen fechas
            if j == 7:  
                fecha = QDate.fromString(str(val), "yyyy-MM-dd")  # Convertir la fecha a objeto QDate
                item.setText(fecha.toString("dd-MM-yyyy"))  # Establecer el formato de visualización
            
            if j in [0, 3, 5, 6, 7]:  # Ajustar alineación para ciertas columnas
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.tablaUpdateRecord.setItem(i, j, item)
            
def tabla_eliminarUSER(self, cursor, resultados, QHeaderView, QTableWidget, QAbstractItemView, QTableWidgetItem, QDate, Qt):
    headers = [description[0].replace("_"," ").upper() for description in cursor.description]
    
    self.tablaDeleteRecord.setRowCount(len(resultados))
    self.tablaDeleteRecord.setColumnCount(len(resultados[0]))
    self.tablaDeleteRecord.setHorizontalHeaderLabels(headers)
    
    # Establecer la propiedad de "stretch" en el encabezado horizontal
    header = self.tablaDeleteRecord.horizontalHeader()
    header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    
    # Obtener la instancia del encabezado vertical
    vertical_header = self.tablaDeleteRecord.verticalHeader()
    vertical_header.setVisible(False)
    
    self.tablaDeleteRecord.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
    self.tablaDeleteRecord.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
    
    for i, row in enumerate(resultados):
        for j, val in enumerate(row):
            item = QTableWidgetItem(str(val))
            # Indices de las columnas que contienen fechas
            if j == 7:  
                fecha = QDate.fromString(str(val), "yyyy-MM-dd")  # Convertir la fecha a objeto QDate
                item.setText(fecha.toString("dd-MM-yyyy"))  # Establecer el formato de visualización
            
            if j in [0, 3, 5, 6, 7]:  # Ajustar alineación para ciertas columnas
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.tablaDeleteRecord.setItem(i, j, item)
            
def borrarTabla(self):
    # Obtener el número de filas de la tabla
    num_filas = self.tablaDeleteRecord.rowCount()

    # Eliminar todas las filas de la tabla
    for i in range(num_filas):
        self.tablaDeleteRecord.removeRow(0)  