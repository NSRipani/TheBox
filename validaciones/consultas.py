# Módulo de Estilos
from qss.style_item import itemColor_TOTAL, itemColor_RESULTADO

def consulta1(self,cursor,results,QHeaderView,QTableWidget,QAbstractItemView,QTableWidgetItem,QDate,Qt):
    
    headers = [description[0].replace('_', ' ').upper() for description in cursor.description]
                
    self.tablaVIEW.setRowCount(len(results))
    self.tablaVIEW.setColumnCount(len(results[0]))
    self.tablaVIEW.setHorizontalHeaderLabels(headers)
    
    # Establecer la propiedad de "stretch" en el encabezado horizontal
    header = self.tablaVIEW.horizontalHeader()
    header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    self.tablaVIEW.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
    self.tablaVIEW.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
    self.tablaVIEW.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
    self.tablaVIEW.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

    for i, row in enumerate(results):
        for j, val in enumerate(row):
            item = QTableWidgetItem(str(val))
            # Indices de las columnas que contienen fechas
            if j == 6 or j == 9:  
                fecha = QDate.fromString(str(val), "yyyy-MM-dd")  # Convertir la fecha a objeto QDate
                item.setText(fecha.toString("dd-MM-yyyy"))  # Establecer el formato de visualización
            
            if j in [2, 4, 5, 6, 8, 9]:  # Ajustar alineación para ciertas columnas
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter) 
            self.tablaVIEW.setItem(i, j, item)
            
    if self.tablaVIEW.rowCount() == len(results):
        total_precios = sum(row[8] for row in results)  # para cada fila en results, se toma el valor que está en la posición 4 (quinta columna, considerando que la indexación comienza en 0) y se suma a un acumulador.

        # Agregar una fila al final de la tabla para mostrar la suma total
        total_row = self.tablaVIEW.rowCount()
        self.tablaVIEW.insertRow(total_row)

        # Mostrar la etiqueta "Total" en la primera celda de la fila de total
        item_total_label_alumno = QTableWidgetItem("TOTAL: ")
        item_total_label_alumno.setFont(itemColor_TOTAL(item_total_label_alumno))  # Funcion para estilos de item
        item_total_label_alumno.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tablaVIEW.setItem(total_row, 7, item_total_label_alumno)

        # Mostrar la suma total en la celda debajo de la columna 'precios'
        item_total_precio_alumno = QTableWidgetItem(str(f"$ {total_precios}"))
        item_total_precio_alumno.setFont(itemColor_RESULTADO(item_total_precio_alumno))  # Funcion para estilos de item
        self.tablaVIEW.setItem(total_row, 8, item_total_precio_alumno)
        item_total_precio_alumno.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                
def consulta2(self,cursor,results,QHeaderView,QTableWidget,QAbstractItemView,QAbstractScrollArea,QTableWidgetItem,QDate,Qt):
    
    headers = [description[0].replace('_', ' ').upper() for description in cursor.description]
    
    self.tablaVIEW.setRowCount(len(results))
    self.tablaVIEW.setColumnCount(len(results[0]))
    self.tablaVIEW.setHorizontalHeaderLabels(headers)
        
    # Establecer la propiedad de "stretch" en el encabezado horizontal
    header = self.tablaVIEW.horizontalHeader()
    header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)#ResizeToContents)# 
    header.setAutoScroll(True)
    self.tablaVIEW.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
    self.tablaVIEW.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
    self.tablaVIEW.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
    self.tablaVIEW.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
    self.tablaVIEW.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        
    for i, fila in enumerate(results):
        for j, valor in enumerate(fila):
            item = QTableWidgetItem(str(valor)) 
            if j == 7 or j == 9:  # Indices de las columnas que contienen fechas
                fecha = QDate.fromString(str(valor), "yyyy-MM-dd")  # Convertir la fecha a objeto QDate
                item.setText(fecha.toString("dd-MM-yyyy"))  # Establecer el formato de visualización
            
            if j in [2, 4, 5, 6, 7, 8, 9]:  # Ajustar alineación para ciertas columnas
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)                  
            self.tablaVIEW.setItem(i, j, item)
    
    if self.tablaVIEW.rowCount() == len(results):
        total_precios = sum(row[8] for row in results)  # para cada fila en results, se toma el valor que está en la posición 4 (quinta columna, considerando que la indexación comienza en 0) y se suma a un acumulador.

        # Agregar una fila al final de la tabla para mostrar la suma total
        total_row = self.tablaVIEW.rowCount()
        self.tablaVIEW.insertRow(total_row)

        # Mostrar la etiqueta "Total" en la primera celda de la fila de total
        item_total_label_alumno = QTableWidgetItem("TOTAL: ")
        item_total_label_alumno.setFont(itemColor_TOTAL(item_total_label_alumno))  # Funcion para estilos de item
        item_total_label_alumno.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tablaVIEW.setItem(total_row, 7, item_total_label_alumno)

        # Mostrar la suma total en la celda debajo de la columna 'precios'
        item_total_precio_alumno = QTableWidgetItem(str(f"$ {total_precios}"))
        item_total_precio_alumno.setFont(itemColor_RESULTADO(item_total_precio_alumno))  # Funcion para estilos de item
        self.tablaVIEW.setItem(total_row, 8, item_total_precio_alumno)
        item_total_precio_alumno.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        
def limpiar(self):
    # Obtener el número de filas de la tabla
    num_filas = self.tablaVIEW.rowCount()

    # Eliminar todas las filas de la tabla
    for i in range(num_filas):
        self.tablaVIEW.removeRow(0)

    # Eliminar los encabezados de la tabla
    self.tablaVIEW.clearContents()
    self.tablaVIEW.setRowCount(0) 