from modulos.mensajes import mensaje_ingreso_datos,aviso_descargaExitosa,aviso_Advertencia_De_excel
import os

def tabla_registroUSUARIO(self,Workbook,Font,PatternFill,Border,Side,numbers,QFileDialog):
    if self.tablaRecord.rowCount() == 0:
        mensaje_ingreso_datos("Descarga de archivo","Primero debe mostrar una tabla antes de descargarla en un archivo Excel.")
        return
    
    workbook = Workbook()
    sheet = workbook.active

    # Obtener encabezados de la tabla y guardarlos en el archivo Excel
    for col in range(self.tablaRecord.columnCount()):
        header_item = self.tablaRecord.horizontalHeaderItem(col)
        if header_item is not None:
            header_cell = sheet.cell(row=1, column=col + 1)
            header_cell.value = header_item.text()
            # Establecer estilo personalizado a las celdas de encabezado
            header_cell.font = Font(name='Arial', bold=True)  # Cambiar el tipo de fuente aquí
            header_cell.fill = PatternFill(start_color="FFA500", end_color="FFA500", fill_type="solid")
            header_cell.border = Border(top=Side(style="thin"), bottom=Side(style="thin"), left=Side(style="thin"), right=Side(style="thin"))
    
    # Obtener datos de la tabla y guardarlos en el archivo Excel
    for row in range(self.tablaRecord.rowCount()):
        for col in range(self.tablaRecord.columnCount()):
            item = self.tablaRecord.item(row, col)
            if item is not None:
                cell = sheet.cell(row=row+2, column=col+1)
                cell.value = item.text()

                # Establecer estilo personalizado a las celdas
                cell.font = Font(name="Arial", bold=True)
                cell.fill = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")
                cell.border = Border(top=Side(style="thin"), bottom=Side(style="thin"), left=Side(style="thin"), right=Side(style="thin"))

                # Agregar formato de número y/o fecha a la celda si es necesario
                if col in [0,1,2,3,4,6,7,8]:
                    cell.number_format = numbers.FORMAT_TEXT
                elif col == 5:
                    cell.number_format = "0"
                    
        # Autoajustar el ancho de las columnas
    for col in sheet.columns:
        max_length = 0
        column = col[0].column_letter  # obtiene el nombre de la columna
        for cell in col:
            try:  # Necessary to avoid error on empty cells
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                pass
        adjusted_width = (max_length + 2) * 1.2
        sheet.column_dimensions[column].width = adjusted_width
        
    # Calcular la última fila de datos en la hoja de cálculo
    ultima_fila = self.tablaRecord.rowCount()

    # Construir la fórmula de autosuma
    formula_autosuma = f"=COUNTA(B2:B{ultima_fila})"

    # Asignar la fórmula de autosuma a la celda específica
    autosuma_cell = sheet.cell(row=ultima_fila+1, column=2)
    autosuma_cell.value = formula_autosuma

    # Aplicar un formato específico a la celda
    autosuma_cell.number_format = "0"

    file_path, _ = QFileDialog.getSaveFileName(self, "Guardar archivo Excel", "", "Archivos Excel (*.xlsx)")

    if file_path:
        if os.path.exists(file_path):
            file_name, file_extension = os.path.splitext(file_path)
            file_path = f"{file_name}_nuevo{file_extension}"

        try:
            workbook.save(file_path)
            aviso_descargaExitosa("Descarga exitosa","La tabla se ha descargado en un archivo Excel con éxito.")
        except Exception as e:
            aviso_Advertencia_De_excel("Advertencia", f"No se pudo guardar el archivo: {str(e)}.\nEL archivo que deseas reemplazar esta en uso, de2ebes cerrar el archivo y luego guardarlo. El nombre puede ser parecido pero no igual.")

def tabla_registroDISCIPLINA(self,Workbook,Font,PatternFill,Border,Side,numbers,QFileDialog):
        if self.tableActivi.rowCount() == 0:
            mensaje_ingreso_datos("Descarga de archivo","Primero debe mostrar una tabla antes de descargarla en un archivo Excel.")
            return
        
        workbook = Workbook()
        sheet = workbook.active

        # Obtener encabezados de la tabla y guardarlos en el archivo Excel
        for col in range(self.tableActivi.columnCount()):
            header_item = self.tableActivi.horizontalHeaderItem(col)
            if header_item is not None:
                header_cell = sheet.cell(row=1, column=col + 1)
                header_cell.value = header_item.text()
                # Establecer estilo personalizado a las celdas de encabezado
                header_cell.font = Font(name='Arial', bold=True)  # Cambiar el tipo de fuente aquí
                header_cell.fill = PatternFill(start_color="FFA500", end_color="FFA500", fill_type="solid")
                header_cell.border = Border(top=Side(style="thin"), bottom=Side(style="thin"), left=Side(style="thin"), right=Side(style="thin"))
        
        # Obtener datos de la tabla y guardarlos en el archivo Excel
        for row in range(self.tableActivi.rowCount()):
            for col in range(self.tableActivi.columnCount()):
                item = self.tableActivi.item(row, col)
                if item is not None:
                    cell = sheet.cell(row=row+2, column=col+1)
                    cell.value = item.text()

                    # Establecer estilo personalizado a las celdas
                    cell.font = Font(name="Arial", bold=True)
                    cell.fill = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")
                    cell.border = Border(top=Side(style="thin"), bottom=Side(style="thin"), left=Side(style="thin"), right=Side(style="thin"))
   
                    # Agregar formato de número y/o fecha a la celda si es necesario
                    if col == 0:
                        cell.number_format = numbers.FORMAT_NUMBER
                    elif col == 1:
                        cell.number_format = numbers.FORMAT_TEXT
                    elif col == 2:
                        cell.number_format = numbers.FORMAT_NUMBER_00
                        
         # Autoajustar el ancho de las columnas
        for col in sheet.columns:
            max_length = 0
            column = col[0].column_letter  # obtiene el nombre de la columna
            for cell in col:
                try:  # Necessary to avoid error on empty cells
                    if len(str(cell.value)) > max_length:
                        max_length = len(cell.value)
                except:
                    pass
            adjusted_width = (max_length + 2) * 1.2
            sheet.column_dimensions[column].width = adjusted_width
            
        # Calcular la última fila de datos en la hoja de cálculo
        ultima_fila = self.tableActivi.rowCount()

        # Construir la fórmula de autosuma
        formula_autosuma = f"=COUNTA(B2:B{ultima_fila})"

        # Asignar la fórmula de autosuma a la celda específica
        autosuma_cell = sheet.cell(row=ultima_fila+1, column=2)
        autosuma_cell.value = formula_autosuma

        # Aplicar un formato específico a la celda
        autosuma_cell.number_format = "0"
        
        file_path, _ = QFileDialog.getSaveFileName(self, "Guardar archivo Excel", "", "Archivos Excel (*.xlsx)")

        if file_path:
            if os.path.exists(file_path):
                file_name, file_extension = os.path.splitext(file_path)
                file_path = f"{file_name}_nuevo{file_extension}"

            try:
                workbook.save(file_path)
                aviso_descargaExitosa("Descarga exitosa","La tabla se ha descargado en un archivo Excel con éxito.")
            except Exception as e:
                aviso_Advertencia_De_excel("Advertencia", f"No se pudo guardar el archivo: {str(e)}.\nEL archivo que deseas reemplazar esta en uso, de2ebes cerrar el archivo y luego guardarlo. El nombre puede ser parecido pero no igual.") 