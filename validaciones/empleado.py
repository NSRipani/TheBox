from modulos.mensajes import mensaje_ingreso_datos
import re
def variables(nom_emp,apell_emp,sex_emp,edad_emp,dni_emp,cel):
    espacio = " "
    if (nom_emp.isalpha() and isinstance(nom_emp, str) and re.findall(r'^[a-zA-ZáéíóúÁÉÍÓÚüÜ\'\s]+$',nom_emp)) or nom_emp.isalnum() or re.findall(r'[!@#$%^&*()_+-={};:"\|,.<>/?~`]', nom_emp):
        mensaje_ingreso_datos("Registro de empleado","El 'nombre' debe contener:\n\n- Letras y/o espacios entre nombres(si tiene mas de dos).")
        print(nom_emp)
        return
    try:
        if nom_emp or re.sub(r'" "',espacio, nom_emp):
            print("Validación",f"'{nom_emp}' válido")
    except ValueError:
        mensaje_ingreso_datos("Registro de empleado", "'Nombre' mal escrito. Vuelva a intentar")
        
    if (apell_emp.isalpha() and isinstance(apell_emp, str) and re.findall(r'^[a-zA-ZáéíóúÁÉÍÓÚüÜ\'\s]+$',apell_emp)) or apell_emp.isalnum() or re.findall(r'[!@#$%^&*()_+-={};:"\|,.<>/?~`]', apell_emp):
        mensaje_ingreso_datos("Registro de empleado","El 'apellido' debe contener:\n\n- Letras y/o espacios entre nombres(si tiene mas de dos).")
        return
    try:
        if apell_emp or re.sub(r'" "',espacio, apell_emp):
            print("Validación",f"'{apell_emp}' válido")
    except ValueError:
        mensaje_ingreso_datos("Registro de empleado", "'apellido' mal escrito. Vuelva a intentar")
    # patron = re.compile(r'^[a-zA-ZáéíóúÁÉÍÓÚüÜ\'\s]+$') 
    # if not isinstance(nom_emp, str) or nom_emp.isspace() or not patron.match(nom_emp) or not nom_emp.isalpha(): #'match' -> verificar si la cadena coincide con este patrón.
    #     mensaje_ingreso_datos("Registro de empleado","El 'nombre' debe contener:\n\n- Letras y/o espacios entre nombres(si tiene mas de dos).")
    #     return
    
    # if not isinstance(apell_emp, str) or apell_emp.isspace() or not patron.match(apell_emp) or not apell_emp.isalpha():
    #     mensaje_ingreso_datos("Registro de empleado","El 'apellido' debe contener:\n\n- Letras y/o espacios entre nombres(si tiene mas de dos).")
    #     return
    
    if not isinstance(sex_emp, str) or not sex_emp.isalpha():
        mensaje_ingreso_datos("Registro de empleado","Debe elegir un sexo.\n\nEl sexo es 'Hombre' o 'Mujer'")
        return
    if sex_emp:
        sex_emp = sex_emp.capitalize()
     
    # Validar edad: debe ser un entero
    patron_mun = re.compile(r'^[0-9]+$')
    if not edad_emp.isdigit() or not len(edad_emp) == 2 or not patron_mun.match(edad_emp):
        mensaje_ingreso_datos("Registro de empleado","La Edad debe contener:\n\n- Contener 2 (DOS) números enteros.\n- No contener puntos(.)")
        return
    try:
        edad_emp and len(str(edad_emp))==2
        edad_emp = int(edad_emp)
    except ValueError:
        mensaje_ingreso_datos("Registro de empleado","La Edad debe contener:\n\n- Contener 2 (DOS) números enteros.\n- No contener puntos(.)")
        return
      
    if not (isinstance(dni_emp, str) and dni_emp.isdigit() and patron_mun.match(dni_emp) and len(str(dni_emp)) == 8):# and len(str(dni_emp))==8 
        mensaje_ingreso_datos("Registro de empleado","El DNI debe contener:\n\n- Números enteros.\n - No contener puntos(.)")
        return
    try:
        if dni_emp:# and len(str(dni_emp))==8
            dni_emp = int(dni_emp)
    except ValueError:
        mensaje_ingreso_datos("Registro de empleado","El DNI debe contener: \n\n- Números enteros.\n - No contener puntos(.)")
        return
    
    if not (cel.isdigit() and patron_mun.match(cel)):
        mensaje_ingreso_datos("Registro de empleado","El Celular debe ser:\n\n- Números enteros.\n- No contener puntos(.)")
        return
    try:
        if cel:
            print(f"El celular es {cel}")
    except ValueError:
        mensaje_ingreso_datos("Registro de empleado","El celular debe ser numérico")
        return

    return "Validación exitosa."
    
def lim_campos(self,QDate):
    self.nombre.clear()
    self.apellido.clear()
    self.sex.setCurrentIndex(0)
    self.edad.clear()
    self.dni.clear()
    self.celular.clear()
    self.fecha.setDate(QDate.currentDate())
    
def seleccion_DeTabla(self,QDate):
    fila = self.tablaEmp.currentRow()
    
    nom_emp = self.tablaEmp.item(fila,1).text()
    apell_emp = self.tablaEmp.item(fila,2).text()
    sex_emp = self.tablaEmp.item(fila,3).text()
    edad_emp = self.tablaEmp.item(fila,4).text()
    dni_emp = self.tablaEmp.item(fila,5).text()
    cel = self.tablaEmp.item(fila,6).text()
    fecha = self.tablaEmp.item(fila,7).text()
    fecha = QDate.fromString(fecha,"dd-MM-yyyy")
    
    self.nombre.setText(nom_emp)
    self.apellido.setText(apell_emp)
    self.sex.setCurrentText(str(sex_emp))
    self.edad.setText(edad_emp)
    self.dni.setText(dni_emp)
    self.celular.setText(cel)
    self.fecha.setDate(fecha)

    self.tablaEmp.clearSelection() # Deselecciona la fila

def verTabla(self,cursor,busqueda,QHeaderView,QTableWidget,QAbstractItemView,QTableWidgetItem,QDate,Qt):
    headers = [description[0].replace('_', ' ').upper() for description in cursor.description]
    
    self.tablaEmp.setRowCount(len(busqueda))
    self.tablaEmp.setColumnCount(len(busqueda[0]))
    self.tablaEmp.setHorizontalHeaderLabels(headers)
    
    # Establecer la propiedad de "stretch" en el encabezado horizontal
    header = self.tablaEmp.horizontalHeader()
    header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    header.setAutoScroll(True)
    
    titulosV = self.tablaEmp.verticalHeader()
    titulosV.setVisible(False)
    
    # Ajustar el tamaño de las filas para que se ajusten al contenido
    self.tablaEmp.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
    self.tablaEmp.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
    self.tablaEmp.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        
    for i, row in enumerate(busqueda):
        for j, val in enumerate(row):
            item = QTableWidgetItem(str(val))
            
            # Indices de las columnas que contienen fechas
            if j == 7:  
                fecha = QDate.fromString(str(val), "yyyy-MM-dd")  # Convertir la fecha a objeto QDate
                item.setText(fecha.toString("dd-MM-yyyy"))  # Establecer el formato de visualización
            
            if j in [0,4,5,6,7]:  # Ajustar alineación para ciertas columnas
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)   
            self.tablaEmp.setItem(i, j, item)
            
