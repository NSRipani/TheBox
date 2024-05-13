def seleccionDeTablaPAGOS(self,QDate):
    fila = self.tablePagos.currentRow()
    
    id_user = self.tablePagos.item(fila,1).text()
    id_user = int(id_user)
    id_discipl = self.tablePagos.item(fila,2).text()
    tipoPago = self.tablePagos.item(fila,3).text()
    fecha = self.tablePagos.item(fila,4).text()
    fecha = QDate.fromString(fecha,"dd-MM-yyyy")
    
    self.idUser.setCurrentText(str(id_user))
    self.idDis.setCurrentText(id_discipl)
    self.input_tipoDePago.setCurrentText(tipoPago)
    self.input_fechaDePago.setDate(fecha)


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
            self.tablePagos.setItem(i, j, item)