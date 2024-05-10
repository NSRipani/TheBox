from modulos.mensajes import mensaje_ingreso_datos
import re

def guardarACTIVIDAD(actividad,precio):
    patronA = re.compile(r'^[a-zA-ZáéíóúÁÉÍÓÚüÜ\'\s]+$') 
    if not isinstance(actividad, str) or actividad.isspace() or not patronA.match(actividad):
        mensaje_ingreso_datos("Registro de alumnos","Debe elegir una disciplina")
        return

    patron2 = re.compile(r'^[0-9]+$')
    if not (precio.isdigit() and patron2.match(precio)):
        mensaje_ingreso_datos("Registro de alumnos","El precio debe ser número entero. Sin coma ','.")
    if precio: 
        precio = int(precio)

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