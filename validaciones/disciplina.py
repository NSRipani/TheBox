from modulos.mensajes import mensaje_ingreso_datos
import re
   

def completar_CAMPOS_ACTIVIDAD(self):
    row = self.tableActivi.currentRow()
    
    id_dis = self.tableActivi.item(row,0).text()
    id_dis = int(id_dis)
    disc6 = self.tableActivi.item(row, 1).text()
    pesos = self.tableActivi.item(row, 2).text()
    pesos = int(pesos)  # Convertir a entero
    
    self.input_disciplina4.setText(disc6)
    self.input_precio.setText(str(pesos))  # Convertir a texto antes de asignar al QLineEdit 
    
    self.tableActivi.clearSelection()  # Deseleccionar la fila eliminada
    
def clear_tabla_disciplina(self):
    # Obtener el número de filas de la tabla
    num_filas = self.tableActivi.rowCount()

    # Eliminar todas las filas de la tabla
    for i in range(num_filas):
        self.tableActivi.removeRow(0) 
    
def tabla_DISCIPLINA(self, resultados, cursor, QHeaderView, QTableWidget, QAbstractItemView, QTableWidgetItem, Qt):
    # Coloca los nomnbres de la cabecera en mayuscula
    header = [description[0].replace("_"," ").upper() for description in cursor.description]
    
    self.tableActivi.setRowCount(len(resultados))
    self.tableActivi.setColumnCount(len(resultados[0]))
    self.tableActivi.setHorizontalHeaderLabels(header)
    
    titulos = self.tableActivi.horizontalHeader()
    titulos.setSectionResizeMode(QHeaderView.ResizeMode.Stretch) # Se estira en toda el area del QTableWiget
    
    encavezado_vertical = self.tableActivi.verticalHeader()
    encavezado_vertical.setVisible(False)
    
    self.tableActivi.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows) # selecciona la fila
    self.tableActivi.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers) # Tabla no editable manualmente
    self.tableActivi.setAutoScroll(True)
    
    for i, row in enumerate(resultados):
        for j, val in enumerate(row):
            item = QTableWidgetItem(str(val))
            if j in [0, 2]:  # Ajustar alineación para ciertas columnas
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)   
            if j == 2:   
                item.setText(f"$ {val}")
                item.setTextAlignment(Qt.AlignmentFlag.AlignRight)   
            self.tableActivi.setItem(i, j, item)