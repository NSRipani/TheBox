from qss.style_item import itemColor_RESULTADO, itemColor_TOTAL

def seleccionDeTablaPAGOS(self,QDate):
    fila = self.tablePagos.currentRow()
    
    id_user = self.tablePagos.item(fila,1).text()
    id_user = int(id_user)
    name_discipl = self.tablePagos.item(fila,2).text()
    tipoPago = self.tablePagos.item(fila,3).text()
    fecha = self.tablePagos.item(fila,4).text()
    fecha = QDate.fromString(fecha,"dd-MM-yyyy")
    
    # disciplinas =  [self.idDis.itemText(i).lower() for i in range(self.idDis.count())]
    # id_disciplina = disciplinas.index(name_discipl.lower())
    
    self.idUser.setText(str(id_user))
    self.idDis.setText(str(name_discipl))
    self.input_tipoDePago.setText(tipoPago)
    self.input_fechaDePago.setDate(fecha)
    
    self.actualizar_precio(name_discipl)
    
    self.tablePagos.clearSelection()  # Deseleccionar la fila eliminada

def tabla_pagos(self, cursor, result, QHeaderView, QTableWidget, QAbstractItemView, QTableWidgetItem, QDate, Qt):
    # Coloca los nomnbres de la cabecera en mayuscula
    header = [description[0].replace("_"," ").upper() for description in cursor.description]
    
    self.tablePagos.setRowCount(len(result))
    self.tablePagos.setColumnCount(len(result[0]))
    self.tablePagos.setHorizontalHeaderLabels(header)
    
    titulos = self.tablePagos.horizontalHeader()
    titulos.setSectionResizeMode(QHeaderView.ResizeMode.Stretch) # Se estira en toda el area del QTableWiget
    
    encavezado_vertical = self.tablePagos.verticalHeader()
    encavezado_vertical.setVisible(False)
    
    self.tablePagos.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows) # selecciona la fila
    self.tablePagos.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers) # Tabla no editable manualmente
    
    for i, row in enumerate(result):
        for j, val in enumerate(row):
            item = QTableWidgetItem(str(val))
            if j == 4: 
                fecha = QDate.fromString(str(val), "yyyy-MM-dd")  # Convertir la fecha a objeto QDate
                item.setText(fecha.toString("dd-MM-yyyy"))  # Establecer el formato de visualización
            if j in [0, 1, 3, 4]:  # Ajustar alineación para ciertas columnas
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            if j == 5:  # Ajustar alineación para ciertas columnas
                item.setTextAlignment(Qt.AlignmentFlag.AlignRight)
                # item.setText(f"$ {val}")
            self.tablePagos.setItem(i, j, item)   
            
    total_pagos = sum(int(row[5]) for row in result)
            
    # Agregar una fila al final de la tabla para mostrar la suma total
    total_row = self.tablePagos.rowCount()
    self.tablePagos.insertRow(total_row)
    
    motrar_total = QTableWidgetItem('TOTAL:')
    motrar_total.setFont(itemColor_TOTAL(motrar_total))  # Funcion para estilos de item
    motrar_total.setTextAlignment(Qt.AlignmentFlag.AlignRight)
    self.tablePagos.setItem(len(result), 4, motrar_total)
    
    suma_pagos = QTableWidgetItem(str(f"$ {total_pagos}"))
    suma_pagos.setFont(itemColor_RESULTADO(suma_pagos))  # Funcion para estilos de item
    suma_pagos.setTextAlignment(Qt.AlignmentFlag.AlignRight)
    self.tablePagos.setItem(len(result), 5, suma_pagos)       