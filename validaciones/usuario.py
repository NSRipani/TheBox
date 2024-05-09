from modulos.mensajes import mensaje_ingreso_datos
import re

def registroUSER(nombre1 , apellido1, dni, sexo, edad, celu):
    patron = re.compile(r'^[a-zA-ZáéíóúÁÉÍÓÚüÜ\'\s]+$') 
    if not isinstance(nombre1, str) or nombre1.isspace() or not patron.match(nombre1): #'match' -> verificar si la cadena coincide con este patrón.
        mensaje_ingreso_datos("Registro de alumnos","El 'nombre' debe contener:\n\n- Letras y/o espacios entre nombres(si tiene mas de dos).")
        return

    if not isinstance(apellido1, str) or apellido1.isspace() or not patron.match(apellido1):
        mensaje_ingreso_datos("Registro de alumnos","El 'apellido' debe contener:\n\n- Letras y/o espacios entre nombres(si tiene mas de dos).")
        return

    patron2 = re.compile(r'^[0-9]+$')
    if not dni.isdigit() or not len(dni) == 8 or not patron2.match(dni):
        mensaje_ingreso_datos("Registro de empleado","El 'DNI' debe ser:\n\n- Numérico y contener 8 números enteros")
        return
    dni = int(dni)    

    if not (isinstance(sexo, str) and patron.match(sexo)):
        mensaje_ingreso_datos("Registro de alumnos","Debe elegir una sexo")
        return
    
    if not edad.isdigit() or not len(edad) == 2 or not patron2.match(edad):
        mensaje_ingreso_datos("Registro de alumnos","La 'edad' debe ser:\n\n- Valores numéricos.\n- Contener 2 dígitos.\n- No contener puntos(.)")
        return
    edad = int(edad)

    if not (celu.isdigit() and len(celu) == 10 and patron2.match(celu)):
        mensaje_ingreso_datos("Registro de alumnos","El 'celular' debe ser:\n\n- Valores numéricos.\n- Contener 10 dígitos.\n- No contener puntos(.)")
        return
    
def limpiasElementosUser(self,QDate):
    self.input_nombre1.clear()
    self.input_apellido1.clear()
    self.input_dni.clear()
    self.input_sex.setCurrentIndex(0)
    self.input_age.clear()
    self.input_celular.clear()
    self.input_date.setDate(QDate.currentDate())
    
def limpiar_campos(self):
    # Guardar temporalmente el valor del QComboBox
    valor_sexo = self.input_sex2.currentIndex(0)
    
    # self.id2.clear()
    self.input_nombre2.clear()
    self.input_apellido2.clear()
    self.input_age2.clear()
    self.input_dni2.clear()
    self.input_celular2.clear()
    
    self.input_apellido2.setEnabled(False)
    self.input_dni2.setEnabled(False)
    self.input_sex2.setEnabled(False)
    self.input_age2.setEnabled(False)
    self.input_date2.setEnabled(False)
    self.input_celular2.setEnabled(False)  
    
    # Restaurar el valor guardado del QComboBox
    self.input_sex2.setCurrentText(valor_sexo)
    
def actualizarUSER(nombre2 , apellido2, dni2, sexo2, edad2, celu2):
    patron_Letras = re.compile(r'^[a-zA-ZáéíóúÁÉÍÓÚüÜ\'\s]+$') 
    if not isinstance(nombre2, str) or nombre2.isspace() or not patron_Letras.match(nombre2):
        mensaje_ingreso_datos("Registro de alumnos","El 'nombre' solo debe contener letras y/o espacios")
        return

    if not isinstance(apellido2, str) or apellido2.isspace() or not patron_Letras.match(apellido2):
        mensaje_ingreso_datos("Registro de alumnos","El 'apellido' solo debe contener letras y/o espacios")
        return
    
    patronNum = re.compile(r'^[0-9]+$')
    if not (dni2.isnumeric() and len(dni2) == 8 and patronNum.match(dni2)):
        mensaje_ingreso_datos("Registro de alumnos","El 'DNI' debe ser:\n- Valores numéricos.\n- Contener 8 dígitos.\n- No contener puntos(.)")
        return
    dni2 = int(dni2)    

    if not (isinstance(sexo2, str) and patron_Letras.match(sexo2)):
        mensaje_ingreso_datos("Registro de alumnos","Debe elegir una sexo")
        return
    
    if not (edad2.isnumeric() and len(edad2) == 2 and patronNum.match(edad2)):
        mensaje_ingreso_datos("Registro de alumnos","El 'edad' debe ser:\n- Valores numéricos.\n- Contener 2 dígitos.\n- No contener puntos(.)")
        return
    edad2 = int(edad2)
    
    if not (celu2.isnumeric() and patronNum.match(celu2)):
        mensaje_ingreso_datos("Registro de alumnos","El 'celular' debe ser: \n- Valores numéricos. \n- Contener 10 dígitos.\n- No contener puntos(.)")
        return
    
def limpiasElementosUseraActualizar(self,QDate):
    self.input_nombre2.clear()
    self.input_apellido2.clear()
    self.input_dni2.clear()
    self.input_sex2.setCurrentIndex(0)
    self.input_age2.clear()
    self.input_celular2.clear()
    self.input_date2.setDate(QDate.currentDate())