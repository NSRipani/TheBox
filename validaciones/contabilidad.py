from qss.style_item import itemColor_RESULTADO,itemColor_TOTAL

def validadciones(re,mensaje_ingreso_datos,date,descripcion,descripcion_h,deber,haberes):
    if not date:
        mensaje_ingreso_datos("Registro de Ingresos-Egresos","Debe establcer un rango de inicio y fin de fechas.")
        return
    
    if not descripcion.isalpha() and descripcion != '':
        mensaje_ingreso_datos("Registro de Ingresos-Egresos","El concepto en el 'Debe' debe ser solo texto o puede estar vacio.")
        return
    
    if not descripcion_h.isalpha() and descripcion_h != '':
        mensaje_ingreso_datos("Registro de Ingresos-Egresos","El concepto en el 'Haber' debe ser")
            
    patron_mun = re.compile(r'^[0-9]+$')
    if not (deber.isnumeric() and patron_mun.match(deber)):
        mensaje_ingreso_datos("Registro de Ingresos-Egresos","El debe debe ser numérico")
        return
    
    if not (haberes.isnumeric() and patron_mun.match(haberes)):
        mensaje_ingreso_datos("Registro de Ingresos-Egresos","El haber debe ser numérico")
        return
    
def limpiarCampos(self,QDate):
    self.fecha_gastos.setDate(QDate.currentDate())
    self.concepto_debe.clear()
    self.concepto_haber.clear()
    self.debe.clear()
    self.haber.clear()
    
def selccionarTabla(self,mensaje_ingreso_datos,QDate):
    rows = self.tablaGastos.currentRow()
        
    if rows == -1:  # Verifica si no se ha seleccionado ninguna fila
        return

    # Verifica si la fila seleccionada es la última fila de la tabla
    if rows == self.tablaGastos.rowCount() - 1:
        mensaje_ingreso_datos("Registro de Ingresos-Egresos","La última fila no debe ser precionada")
        return
    
    # id_concepto = int(self.tablaGastos.item(rows,0).text())
    fecha1 = self.tablaGastos.item(rows,1).text()
    fecha1 = QDate.fromString(fecha1,"dd-MM-yyyy")
    conceptoDebe = self.tablaGastos.item(rows,2).text()
    conceptoHaber = self.tablaGastos.item(rows,3).text()
    debe_valor = self.tablaGastos.item(rows,4).text()
    debe_valor = int(debe_valor)
    haber_valor = self.tablaGastos.item(rows,5).text()
    haber_valor = int(haber_valor)
    
    # self.idConcepto.setText(str(id_concepto))
    self.fecha_gastos.setDate(fecha1)
    self.concepto_debe.clear(conceptoDebe)
    self.concepto_haber.clear(conceptoHaber)
    self.debe.setText(str(debe_valor))
    self.haber.setText(str(haber_valor))
    
    self.tablaGastos.clearSelection() # Deselecciona la fila

def clear_tabla(self):
    # Obtener el número de filas de la tabla
    filas = self.tablaGastos.rowCount()

    # Eliminar todas las filas de la tabla
    for i in range(filas):
        self.tablaGastos.removeRow(0) 

def tabla_contabilidad(self,cursor,busqueda,QHeaderView,QTableWidget,QAbstractItemView,QTableWidgetItem,QDate,Qt):
    headers = [description[0].replace('_', ' ').upper() for description in cursor.description]
    
    self.tablaGastos.setRowCount(len(busqueda))
    self.tablaGastos.setColumnCount(len(busqueda[0]))
    self.tablaGastos.setHorizontalHeaderLabels(headers)
    
    # Establecer la propiedad de "stretch" en el encabezado horizontal
    header = self.tablaGastos.horizontalHeader()
    header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    header.setAutoScroll(True)
    
    vertical = self.tablaGastos.verticalHeader()
    vertical.setVisible(False)
    
    # Ajustar el tamaño de las filas para que se ajusten al contenido
    self.tablaGastos.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
    self.tablaGastos.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
    self.tablaGastos.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
    
    self.tablaGastos.setRowCount(len(busqueda) + 1)
    
    for i, row in enumerate(busqueda):
        for j, val in enumerate(row):
            if val is None:
                val = ''
            item = QTableWidgetItem(str(val))
            
            #Indices de las columnas que contienen fechas
            if j == 1:  
                fecha = QDate.fromString(str(val), "yyyy-MM-dd")  # Convertir la fecha a objeto QDate
                item.setText(fecha.toString("dd-MM-yyyy"))  # Establecer el formato de visualización
            if j == 3:
                item.setTextAlignment(Qt.AlignmentFlag.AlignRight)   
            if j in [0, 1]:  # Ajustar alineación para ciertas columnas
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter) 
            if j in [4, 5]:
                item.setTextAlignment(Qt.AlignmentFlag.AlignRight) 
            self.tablaGastos.setItem(i, j, item)
            
        # Calcular y mostrar la suma de las horas diarias en la fila adicional
        total_debe = sum(int(row[4]) for row in busqueda)
        item_total_horas = QTableWidgetItem('TOTAL:')
        item_total_horas.setFont(itemColor_TOTAL(item_total_horas))  # Funcion para estilos de item
        item_total_horas.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tablaGastos.setItem(len(busqueda), 3, item_total_horas)
        
        item_suma_horas1 = QTableWidgetItem(str(total_debe))
        item_suma_horas1.setFont(itemColor_RESULTADO(item_suma_horas1))  # Funcion para estilos de item
        item_suma_horas1.setTextAlignment(Qt.AlignmentFlag.AlignRight)
        self.tablaGastos.setItem(len(busqueda), 4, item_suma_horas1)
        
        total_haber = sum(int(row[5]) for row in busqueda)
        item_suma_horas2 = QTableWidgetItem(str(total_haber))
        item_suma_horas2.setFont(itemColor_RESULTADO(item_suma_horas2))  # Funcion para estilos de item
        item_suma_horas2.setTextAlignment(Qt.AlignmentFlag.AlignRight)
        self.tablaGastos.setItem(len(busqueda), 5, item_suma_horas2)
        
def cuentas(self,cursor,busqueda,QHeaderView,QTableWidget,QAbstractItemView,QTableWidgetItem,QDate,Qt):
    headers = [description[0].replace('_', ' ').upper() for description in cursor.description]
    
    self.tablacuenta.setRowCount(len(busqueda))
    self.tablacuenta.setColumnCount(len(busqueda[0]))
    self.tablacuenta.setHorizontalHeaderLabels(headers)
    
    # Establecer la propiedad de "stretch" en el encabezado horizontal
    header = self.tablacuenta.horizontalHeader()
    header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    header.setAutoScroll(True)
    
    vertical = self.tablacuenta.verticalHeader()
    vertical.setVisible(False)
    
    # Ajustar el tamaño de las filas para que se ajusten al contenido
    self.tablacuenta.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
    self.tablacuenta.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
    self.tablacuenta.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
    
    for i, row in enumerate(busqueda):
        for j, val in enumerate(row):
            item = QTableWidgetItem(str(val))
            
            #Indices de las columnas que contienen fechas
            if j == 0:  
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.tablacuenta.setItem(i, j, item)