from modulos.mensajes import mensaje_ingreso_datos
from qss.style_item import itemColor_RESULTADO, itemColor_TOTAL
import re
   
def guardarACTIVIDAD(self, actividad, precio):
    actividad = actividad.strip()
    if not (actividad != "" and actividad.replace("", " ") and isinstance(actividad, str) and re.findall(r'^[a-zA-ZáéíóúÁÉÍÓÚüÜ\s]+$',actividad)):
        mensaje_ingreso_datos("Registro de disciplina","La 'Disciplina' debe contener:\n\n- Letras y/o espacios entre nombres(si tiene mas de dos).")
        self.input_disciplina4.setFocus()
        return
    
    precio = precio.stirp()
    patron2 = re.compile(r'^[0-9]+$')
    if not (precio.isdigit() and patron2.match(precio)):# and len(precio) > 0):
        mensaje_ingreso_datos("Registro de disciplina","El precio debe ser número entero. Sin coma ','.")
        self.input_precio.setFocus()
        return
    if precio: 
        precio = int(precio)
        
    return "Carga de datos correcta"

def completar_CAMPOS_ACTIVIDAD(self):
    fila = self.tableActivi.currentRow()
    if fila == -1:  # Verifica si no se ha seleccionado ninguna fila
        return
    # Verifica si la fila seleccionada es la última fila de la tabla
    if fila == self.tableActivi.rowCount() - 1:
        mensaje_ingreso_datos("Registro de disciplinas","La última fila no debe ser precionada")
        return
    
    row = self.tableActivi.currentRow()
    
    id_dis = self.tableActivi.item(row,0).text()
    id_dis = int(id_dis)
    disc6 = self.tableActivi.item(row, 1).text()
    pesos = self.tableActivi.item(row, 2).text()
    # pesos = int(pesos)  # Convertir a entero
    
    self.input_disciplina4.setText(disc6)
    self.input_precio.setText(str(pesos))  # Convertir a texto antes de asignar al QLineEdit 
    
    # self.tableActivi.clearSelection()  # Deseleccionar la fila eliminada
    
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
                item.setTextAlignment(Qt.AlignmentFlag.AlignRight)   
            self.tableActivi.setItem(i, j, item)
            
    # Después de mostrar los resultados en la tabla
    if self.tableActivi.rowCount() == len(resultados):
        total_precios = sum(row[2] for row in resultados)  # para cada fila en results, se toma el valor que está en la posición 4 (quinta columna, considerando que la indexación comienza en 0) y se suma a un acumulador.

        # Agregar una fila al final de la tabla para mostrar la suma total
        total_row = self.tableActivi.rowCount()
        self.tableActivi.insertRow(total_row)

        # Mostrar la etiqueta "Total" en la primera celda de la fila de total
        item_total_label = QTableWidgetItem("TOTAL: ")
        item_total_label.setFont(itemColor_TOTAL(item_total_label))  # Funcion para estilos de item
        item_total_label.setTextAlignment(Qt.AlignmentFlag.AlignRight)
        self.tableActivi.setItem(total_row, 1, item_total_label)

        # Mostrar la suma total en la celda debajo de la columna 'precios'
        item_total_precio = QTableWidgetItem(str(f"$ {total_precios}"))
        item_total_precio.setFont(itemColor_RESULTADO(item_total_precio))  # Funcion para estilos de item
        self.tableActivi.setItem(total_row, 2, item_total_precio)
        item_total_precio.setTextAlignment(Qt.AlignmentFlag.AlignRight)