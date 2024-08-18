# Módulo de Estilos
from qss.style_item import itemColor_TOTAL, itemColor_RESULTADO

def consultaPorAlumno(self,cursor,results,QHeaderView,QTableWidget,QAbstractItemView,QTableWidgetItem,QDate,Qt):
    
    headers = [description[0].replace('_', ' ').upper() for description in cursor.description]
                
    self.tablaVIEW.setRowCount(len(results))
    self.tablaVIEW.setColumnCount(len(results[0]))
    self.tablaVIEW.setHorizontalHeaderLabels(headers)
    
    self.tablaVIEW.verticalHeader().setVisible(False)
    
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
            if j == 5 or j == 8:  
                fecha = QDate.fromString(str(val), "yyyy-MM-dd")  # Convertir la fecha a objeto QDate
                item.setText(fecha.toString("dd-MM-yyyy"))  # Establecer el formato de visualización
            if j in [2, 4, 5, 8]:  # Ajustar alineación para ciertas columnas
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            if j == 7:  # Ajustar alineación para ciertas columnas
                item.setTextAlignment(Qt.AlignmentFlag.AlignRight)
                # item.setText(f"$ {val}")
            self.tablaVIEW.setItem(i, j, item)
            
    if self.tablaVIEW.rowCount() == len(results):
        total_precios = sum(row[7] for row in results)  # para cada fila en results, se toma el valor que está en la posición 4 (quinta columna, considerando que la indexación comienza en 0) y se suma a un acumulador.

        # Agregar una fila al final de la tabla para mostrar la suma total
        total_row = self.tablaVIEW.rowCount()
        self.tablaVIEW.insertRow(total_row)

        # Mostrar la etiqueta "Total" en la primera celda de la fila de total
        item_total_label_alumno = QTableWidgetItem("TOTAL: ")
        item_total_label_alumno.setFont(itemColor_TOTAL(item_total_label_alumno))  # Funcion para estilos de item
        item_total_label_alumno.setTextAlignment(Qt.AlignmentFlag.AlignRight)
        self.tablaVIEW.setItem(total_row, 6, item_total_label_alumno)

        # Mostrar la suma total en la celda debajo de la columna 'precios'
        item_total_precio_alumno = QTableWidgetItem(str(f"$ {total_precios}"))
        item_total_precio_alumno.setFont(itemColor_RESULTADO(item_total_precio_alumno))  # Funcion para estilos de item
        self.tablaVIEW.setItem(total_row, 7, item_total_precio_alumno)
        item_total_precio_alumno.setTextAlignment(Qt.AlignmentFlag.AlignRight)
                
def totalAlumno(self,cursor,results,QHeaderView,QTableWidget,QAbstractItemView,QAbstractScrollArea,QTableWidgetItem,QDate,Qt):
    
    headers = [description[0].replace('_', ' ').upper() for description in cursor.description]
    
    self.tablaVIEW.setRowCount(len(results))
    self.tablaVIEW.setColumnCount(len(results[0]))
    self.tablaVIEW.setHorizontalHeaderLabels(headers)
        
    # Establecer la propiedad de "stretch" en el encabezado horizontal
    header = self.tablaVIEW.horizontalHeader()
    header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)#ResizeToContents)# 
    header.setAutoScroll(True)
    
    # Obtener la instancia del encabezado vertical
    vertical_header = self.tablaVIEW.verticalHeader()
    vertical_header.setVisible(False)
    
    self.tablaVIEW.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
    self.tablaVIEW.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
    self.tablaVIEW.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
    self.tablaVIEW.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
    self.tablaVIEW.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        
    for i, fila in enumerate(results):
        for j, valor in enumerate(fila):
            item = QTableWidgetItem(str(valor)) 
            if j in [6, 9]:# or j == 9:  # Indices de las columnas que contienen fechas
                fecha = QDate.fromString(str(valor), "yyyy-MM-dd")  # Convertir la fecha a objeto QDate
                item.setText(fecha.toString("dd-MM-yyyy"))  # Establecer el formato de visualización
            if j in [2, 4, 5, 6, 9]:  # Ajustar alineación para ciertas columnas
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            if j == 8:  # Ajustar alineación para ciertas columnas
                item.setTextAlignment(Qt.AlignmentFlag.AlignRight)
                # item.setText(f"$ {valor}")
            self.tablaVIEW.setItem(i, j, item)
    
    if self.tablaVIEW.rowCount() == len(results):
        total_precios = sum(row[8] for row in results)  # para cada fila en results, se toma el valor que está en la posición 4 (quinta columna, considerando que la indexación comienza en 0) y se suma a un acumulador.

        # Agregar una fila al final de la tabla para mostrar la suma total
        total_row = self.tablaVIEW.rowCount()
        self.tablaVIEW.insertRow(total_row)

        # Mostrar la etiqueta "Total" en la primera celda de la fila de total
        item_total_label_alumno = QTableWidgetItem("TOTAL: ")
        item_total_label_alumno.setFont(itemColor_TOTAL(item_total_label_alumno))  # Funcion para estilos de item
        item_total_label_alumno.setTextAlignment(Qt.AlignmentFlag.AlignRight)
        self.tablaVIEW.setItem(total_row, 7, item_total_label_alumno)

        # Mostrar la suma total en la celda debajo de la columna 'precios'
        item_total_precio_alumno = QTableWidgetItem(str(f"$ {total_precios}"))
        item_total_precio_alumno.setFont(itemColor_RESULTADO(item_total_precio_alumno))  # Funcion para estilos de item
        self.tablaVIEW.setItem(total_row, 8, item_total_precio_alumno)
        item_total_precio_alumno.setTextAlignment(Qt.AlignmentFlag.AlignRight)
        
def limpiar(self):
    # Obtener el número de filas de la tabla
    num_filas = self.tablaVIEW.rowCount()

    # Eliminar todas las filas de la tabla
    for i in range(num_filas):
        self.tablaVIEW.removeRow(0)

    # Eliminar los encabezados de la tabla
    self.tablaVIEW.clearContents()
    self.tablaVIEW.setRowCount(0) 
    
def consultarDeDisciplina(self,cursor,results,QHeaderView,QTableWidget,QAbstractItemView,QTableWidgetItem,QDate,Qt):
    headers = [description[0].replace('_', ' ').upper() for description in cursor.description]
    headers.append("Total Precio")

    self.tablaVIEW.setRowCount(len(results))
    self.tablaVIEW.setColumnCount(len(results[0]))
    self.tablaVIEW.setHorizontalHeaderLabels(headers)
    
    # Establecer la propiedad de "stretch" en el encabezado horizontal
    header = self.tablaVIEW.horizontalHeader()
    header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
    # Obtener la instancia del encabezado vertical
    vertical_header = self.tablaVIEW.verticalHeader()
    vertical_header.setVisible(False)
    
    self.tablaVIEW.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
    self.tablaVIEW.setAutoScroll(True)
    self.tablaVIEW.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
    
    for i, row in enumerate(results):
        for j, val in enumerate(row):
            item = QTableWidgetItem(str(val))
            
            # Indices de las columnas que contienen fechas
            if j in [4,5,6]:  
                fecha = QDate.fromString(str(val), "yyyy-MM-dd")  # Convertir la fecha a objeto QDate
                item.setText(fecha.toString("dd-MM-yyyy"))  # Establecer el formato de visualización
            if j in [3, 4, 5, 6]:  # Ajustar alineación para ciertas columnas
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter) 
            if j == 3:  # Ajustar alineación para ciertas columnas
                item.setTextAlignment(Qt.AlignmentFlag.AlignRight) 
                # item.setText(f"$ {val}")
            self.tablaVIEW.setItem(i, j, item)
    
    # Después de mostrar los resultados en la tabla
    if self.tablaVIEW.rowCount() == len(results):
        total_precios = sum(row[3] for row in results)  # para cada fila en results, se toma el valor que está en la posición 4 (quinta columna, considerando que la indexación comienza en 0) y se suma a un acumulador.

        # Agregar una fila al final de la tabla para mostrar la suma total
        total_row = self.tablaVIEW.rowCount()
        self.tablaVIEW.insertRow(total_row)

        # Mostrar la etiqueta "Total" en la primera celda de la fila de total
        item_total_label = QTableWidgetItem("TOTAL: ")
        item_total_label.setFont(itemColor_TOTAL(item_total_label))  # Funcion para estilos de item
        item_total_label.setTextAlignment(Qt.AlignmentFlag.AlignRight)
        self.tablaVIEW.setItem(total_row, 2, item_total_label)

        # Mostrar la suma total en la celda debajo de la columna 'precios'
        item_total_precio = QTableWidgetItem(str(f"$ {total_precios}"))
        item_total_precio.setFont(itemColor_RESULTADO(item_total_precio))  # Funcion para estilos de item
        self.tablaVIEW.setItem(total_row, 3, item_total_precio)
        item_total_precio.setTextAlignment(Qt.AlignmentFlag.AlignRight)
        
def consultaPorDisciplina(self,cursor,results,QHeaderView,QTableWidget,QAbstractItemView,QTableWidgetItem,QDate,Qt):
    headers = [description[0].replace('_', ' ').upper() for description in cursor.description]
    
    self.tablaVIEW.setRowCount(len(results))
    self.tablaVIEW.setColumnCount(len(results[0]))
    self.tablaVIEW.setHorizontalHeaderLabels(headers)
    
    # Establecer la propiedad de "stretch" en el encabezado horizontal
    header = self.tablaVIEW.horizontalHeader()
    header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    
    self.tablaVIEW.verticalHeader().setVisible(False)
    
    self.tablaVIEW.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
    self.tablaVIEW.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
    self.tablaVIEW.setAutoScroll(True)
        
    for i, row in enumerate(results):
        for j, val in enumerate(row):
            item = QTableWidgetItem(str(val))
            
            # Indices de las columnas que contienen fechas
            if j == 7 :  
                fecha = QDate.fromString(str(val), "yyyy-MM-dd")  # Convertir la fecha a objeto QDate
                item.setText(fecha.toString("dd-MM-yyyy"))  # Establecer el formato de visualización
            
            if j in [2, 4, 7]:  # Ajustar alineación para ciertas columnas
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  
            if j == 8:  # Ajustar alineación para ciertas columnas
                item.setTextAlignment(Qt.AlignmentFlag.AlignRight)
                # item.setText(f"$ {val}")
            self.tablaVIEW.setItem(i, j, item)
                
    # Después de mostrar los resultados en la tabla
    if self.tablaVIEW.rowCount() == len(results):
        total_precios = sum(row[8] for row in results)  # para cada fila en results, se toma el valor que está en la posición 4 (quinta columna, considerando que la indexación comienza en 0) y se suma a un acumulador.

        # Agregar una fila al final de la tabla para mostrar la suma total
        total_row = self.tablaVIEW.rowCount()
        self.tablaVIEW.insertRow(total_row)

        # Mostrar la etiqueta "Total" en la primera celda de la fila de total
        item_total_label2 = QTableWidgetItem("TOTAL: ")
        item_total_label2.setFont(itemColor_TOTAL(item_total_label2))  # Funcion para estilos de item
        item_total_label2.setTextAlignment(Qt.AlignmentFlag.AlignRight)
        self.tablaVIEW.setItem(total_row, 7, item_total_label2)

        # Mostrar la suma total en la celda debajo de la columna 'precios'
        item_total_precio2 = QTableWidgetItem(str(f"$ {total_precios}"))
        item_total_precio2.setFont(itemColor_RESULTADO(item_total_precio2))  # Funcion para estilos de item
        item_total_precio2.setTextAlignment(Qt.AlignmentFlag.AlignRight)
        self.tablaVIEW.setItem(total_row, 8, item_total_precio2)

def asistenciaTotal(self,cursor,results,QHeaderView,QTableWidget,QAbstractItemView,QTableWidgetItem,QDate,Qt):
    headers = [description[0].replace('_', ' ').upper() for description in cursor.description]
    self.tablaVIEW.setRowCount(len(results))
    self.tablaVIEW.setColumnCount(len(results[0]))
    self.tablaVIEW.setHorizontalHeaderLabels(headers)
    
    # Establecer la propiedad de "stretch" en el encabezado horizontal
    header = self.tablaVIEW.horizontalHeader()
    header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    
    # Obtener la instancia del encabezado vertical
    vertical_header = self.tablaVIEW.verticalHeader()
    vertical_header.setVisible(False)
    
    # Ajustar el tamaño de las filas para que se ajusten al contenido
    self.tablaVIEW.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
    self.tablaVIEW.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
    self.tablaVIEW.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        
    for i, row in enumerate(results):
        for j, val in enumerate(row):
            item = QTableWidgetItem(str(val))
            
            # Indices de las columnas que contienen fechas
            if j == 5:
                fecha = QDate.fromString(str(val), "yyyy-MM-dd")  # Convertir la fecha a objeto QDate
                item.setText(fecha.toString("dd-MM-yyyy"))  # Establecer el formato de visualización
            
            if j in [2, 4, 5]:  # Ajustar alineación para ciertas columnas     
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  
            self.tablaVIEW.setItem(i, j, item)
    # Calcular la cantidad total de días de asistencia
    total_dias_asistencia = sum(1 for row in results if row[5])

    # Crear una nueva fila en la tabla para mostrar la cantidad total de días de asistencia
    row_count = self.tablaVIEW.rowCount()
    self.tablaVIEW.insertRow(row_count)     # Agregar la nueva fila al final de la tabla

    # Mostrar la etiqueta "Total" en la primera celda de la fila de total
    item_total_label3 = QTableWidgetItem("TOTAL: ")
    item_total_label3.setFont(itemColor_TOTAL(item_total_label3))  # Funcion para estilos de item
    item_total_label3.setTextAlignment(Qt.AlignmentFlag.AlignRight)
    self.tablaVIEW.setItem(row_count, 4, item_total_label3)
    
    # Agregar la información de la cantidad total de días de asistencia en la nueva fila
    item_dias_asistencia = QTableWidgetItem(str(total_dias_asistencia))
    item_dias_asistencia.setFont(itemColor_RESULTADO(item_dias_asistencia))  # Funcion para estilos de item
    item_dias_asistencia.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
    self.tablaVIEW.setItem(row_count, 5, item_dias_asistencia)  # Agregar en la primera columna o en la que desees
    
def asistenciaPorAlumno(self,cursor,results5,QHeaderView,QTableWidget,QAbstractItemView,QTableWidgetItem,QDate,Qt):
    headers = [description[0].replace('_', ' ').upper() for description in cursor.description]
    
    self.tablaVIEW.setRowCount(len(results5))
    self.tablaVIEW.setColumnCount(len(results5[0]))
    self.tablaVIEW.setHorizontalHeaderLabels(headers)
    
    # Establecer la propiedad de "stretch" en el encabezado horizontal
    self.tablaVIEW.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    
    self.tablaVIEW.verticalHeader().setVisible(False)
    
    # Ajustar el tamaño de las filas para que se ajusten al contenido
    self.tablaVIEW.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
    self.tablaVIEW.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
    self.tablaVIEW.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        
    for i, row in enumerate(results5):
        for j, val in enumerate(row):
            item = QTableWidgetItem(str(val))
            
            # Indices de las columnas que contienen fechas
            if j == 5:  
                fecha = QDate.fromString(str(val), "yyyy-MM-dd")  # Convertir la fecha a objeto QDate
                item.setText(fecha.toString("dd-MM-yyyy"))  # Establecer el formato de visualización
            
            if j in [2, 4, 5]:  # Ajustar alineación para ciertas columnas
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)   
            self.tablaVIEW.setItem(i, j, item)
            
    # Calcular la cantidad total de días de asistencia
    total_dias_asistencia = sum(1 for row in results5 if row[5])

    # Crear una nueva fila en la tabla para mostrar la cantidad total de días de asistencia
    row_count = self.tablaVIEW.rowCount()
    self.tablaVIEW.insertRow(row_count)

    # Mostrar la etiqueta "Total" en la primera celda de la fila de total
    item_total_label4 = QTableWidgetItem("TOTAL:")
    item_total_label4.setFont(itemColor_TOTAL(item_total_label4))  # Funcion para estilos de item
    item_total_label4.setTextAlignment(Qt.AlignmentFlag.AlignRight)
    self.tablaVIEW.setItem(row_count, 4, item_total_label4)
    
    # Agregar la información de la cantidad total de días de asistencia en la nueva fila
    item_dias_asistencia2 = QTableWidgetItem(str(total_dias_asistencia))
    item_dias_asistencia2.setFont(itemColor_RESULTADO(item_dias_asistencia2))  # Funcion para estilos de item
    item_dias_asistencia2.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
    self.tablaVIEW.setItem(row_count, 5, item_dias_asistencia2)  # Agregar en la primera columna o en la que desees
