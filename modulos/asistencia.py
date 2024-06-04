# Librería para uso de fechas
from datetime import date, timedelta, datetime

# Librerías de PyQt6
from PyQt6.QtWidgets import QCompleter,QFrame,QHBoxLayout,QSpacerItem,QSizePolicy, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt6.QtCore import Qt, QDateTime, QTimer
from PyQt6.QtGui import QPixmap, QFont,QIcon, QPalette, QBrush

# Librería de MySQL
import mysql.connector
from mysql.connector import Error

# Módulo de Estilos
from qss import style

from utilidades.completar_combobox import actualizar_combobox_disc

# Modulo de para las cajas de mensajes
from modulos.mensajes import mensaje_ingreso_datos
from conexion_DB.dataBase import conectar_base_de_datos
from modulos.mensajes import errorConsulta

class Asistencia(QMainWindow):
    def __init__(self):
        super().__init__()
        self.asistir()
        
    def asistir(self):
        self.showMaximized()
        self.setWindowTitle("Sistema de Registro de Asistencia")
        self.setWindowIcon(QIcon("img/logo.png"))
        self.setStyleSheet(style.fondo_asistencia)   
        self.central_widget = QWidget()        
        self.setCentralWidget(self.central_widget)
        
        layout1 = QVBoxLayout()
        layout1.setContentsMargins(250,0,50,0)
        
        self.layout_img = QHBoxLayout()
               
        spacer1 = QSpacerItem(20, 60, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        layout1.addItem(spacer1)

        # Imagen
        pixmap = QPixmap("img/logo.png")
        image_label = QLabel()
        image_label.setStyleSheet(style.label_logo)
        image_label.setFont(QFont("Segoe UI", 80))
        image_label.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
        image_label.setPixmap(pixmap)
                
        # Después de crear image_label
        texto = QLabel("Un espacio pensando en el movimiento, en todas sus formas")
        texto.setStyleSheet(style.estilo_texto)
        texto.setWordWrap(True)
        texto.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)

        # Agregar ambos labels a la misma disposición horizontal
        self.layout_img.addWidget(image_label,)
        self.layout_img.addWidget(texto)
        
        layout1.addLayout(self.layout_img)
        
        spacer2 = QSpacerItem(20, 100, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        layout1.addItem(spacer2)
        
        # Frame contendero de elementos
        frame1 = QFrame()
        frame1.setStyleSheet(style.frame)
        
        # Se agrega al layout vetical 'layout1' el frame
        layout1.addWidget(frame1)
        
        lV = QVBoxLayout(frame1)
        label_fecha_hoy = QLabel("Fecha de hoy:")
        label_fecha_hoy.setStyleSheet(style.label_fecha)
        lV.addWidget(label_fecha_hoy)

        # fechaHOY = date.today()
        fechaHOY = QDateTime.currentDateTime().toString("dd/MM/yyyy")
        fecha = fechaHOY #toString("dd/MM/yyyy") #strftime("%d/%m/%Y")
        label_fecha_actual = QLabel(fecha, self)
        label_fecha_actual.setStyleSheet(style.estiloFechaActual)
        lV.addWidget(label_fecha_actual)
        
        spacer3 = QSpacerItem(20, 120, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        lV.addItem(spacer3)
        
        label_numero_documento = QLabel("Número de documento:")
        label_numero_documento.setStyleSheet(style.label_documento)
        self.numero_documento = QLineEdit()
        self.numero_documento.setStyleSheet(style.estilo_lineedit)
        self.numero_documento.setMaxLength(8)
        self.numero_documento.textChanged.connect(self.set_focus)
        lV.addWidget(label_numero_documento)
        lV.addWidget(self.numero_documento)
        
        # Conexión a la base de datos MySQL
        conn = conectar_base_de_datos()
        cursor = conn.cursor()

        # Consulta para obtener los datos de una columna específica
        cursor.execute("SELECT dni FROM usuario")
        data = cursor.fetchall()
        suggestions = [str(item[0]) for item in data]

        completer = QCompleter(suggestions)
        completer.setFilterMode(Qt.MatchFlag.MatchStartsWith)
        completer.popup().setFont(QFont("Segoe UI", 18))
        self.numero_documento.setCompleter(completer)
        
        cursor.close()
        conn.close()

        button_registrar_asistencia = QPushButton("Registrar asistencia")
        button_registrar_asistencia.setStyleSheet(style.boton)
        button_registrar_asistencia.setCursor(Qt.CursorShape.PointingHandCursor)
        button_registrar_asistencia.clicked.connect(self.registrar_asistencia)
        lV.addWidget(button_registrar_asistencia)
        
        spacer4 = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        layout1.addItem(spacer4)
        
        layout_vertical = QVBoxLayout()
        layout_vertical.setContentsMargins(50,100,80,100)
        
        self.label_texto1 = QLabel()
        self.label_texto1.setFont(QFont("Segoe UI", 45))
        self.label_texto1.setFrameShadow(QFrame.Shadow.Plain)
        self.label_texto1.setFrameShape(QFrame.Shape.Panel)
        self.label_texto1.setWordWrap(True)
        self.label_texto1.setLineWidth(0)
        self.label_texto1.setFixedWidth(900)
        self.label_texto1.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
        
        layout_vertical.addWidget(self.label_texto1)
        
        spacer5 = QSpacerItem(20, 40, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        layout_vertical.addItem(spacer5)

        self.label_texto2 = QLabel()
        self.label_texto2.setFont(QFont("Segoe UI", 50))
        self.label_texto2.setFrameShadow(QFrame.Shadow.Plain)
        self.label_texto2.setFrameShape(QFrame.Shape.Panel)
        self.label_texto2.setWordWrap(True)
        self.label_texto2.setLineWidth(0)
        self.label_texto2.setFixedWidth(900)
        self.label_texto2.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
        
        layout_vertical.addWidget(self.label_texto2)
        
        layout_horizontal = QHBoxLayout()
        layout_horizontal.addLayout(layout1)
        layout_horizontal.addLayout(layout_vertical)
        
        self.central_widget.setLayout(layout_horizontal)
        
        # Configuración del temporizador para ocultar los mensajes después de unos segundos
        # self.timer = QTimer(self)
        # self.timer.timeout.connect(self.actualizar_fecha)
        # self.timer.start(30 * 24 * 60 * 60 * 1000)  # 30 días en milisegundos
    
    def set_focus(self):
        self.numero_documento.setFocus()
    
    # def ocultar_mensajes(self):
    #     self.label_texto1.clear()
    #     self.label_texto2.clear()
    #     self.timer.stop()
        
    #     self.label_texto1.setStyleSheet("")
    #     self.label_texto2.setStyleSheet("")
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter:
            self.registrar_asistencia()
              
    def registrar_asistencia(self):
        # Dato ingreado por teclado   
        dni = self.numero_documento.text()
        fecha_hoy = datetime.now().date() ##date.today()
        print(fecha_hoy)
        
        # patron = re.compile(r'^[0-9]+$')
        if not dni.isdigit() or len(dni) != 8:
            mensaje_ingreso_datos("Registro de asistecia","El número de documento debe contener 8 dígitos numéricos.")
            return
        
        # Conexión a la base de datos MySQL
        try:
            conn = conectar_base_de_datos()
            cursor = conn.cursor()
            
            cursor.execute(f"SELECT u.id_usuario FROM usuario AS u WHERE u.dni = '{dni}'")
            result = cursor.fetchone()
            print(result[0])
            
            cursor.execute(f"SELECT p.id_disciplina FROM pago AS p WHERE p.id_usuario = '{dni}' LIMIT 1")
            id_disciplina = cursor.fetchone()
            print(id_disciplina[0])       
            
            # Insertar el número de DNI y la fecha actual en la tabla correspondiente
            cursor.execute("INSERT INTO asistencia (asistencia, id_usuario, id_disciplina) VALUES (%s,%s,%s)", (fecha_hoy,result[0],id_disciplina[0]))
            conn.commit()               
        except Error as e:
            errorConsulta("Registro de asistecia", f"Error al registrar la asistencia: {str(e)}")
        finally:
            cursor.close()
            conn.close()   
            
        try:
            conn = conectar_base_de_datos()
            cursor = conn.cursor()
                 
            # Consultar el nombre y apellido del usuario
            cursor.execute(f"SELECT nombre, apellido, fecha_registro FROM usuario WHERE dni='{dni}'")
            resultUser = cursor.fetchone()
            print(f"{resultUser}\n")
            # if len(resultUser) > 0:
            nombre = resultUser[0]
            apellido = resultUser[1]                
            fecha_registro = resultUser[2]
            print(f"{fecha_registro}\n")
            print(type(fecha_registro))
            
            # Establecer datos 'nombre' y 'apellido', de la consulta en los QLabel    
            self.label_texto1.setText(f"¡En hora buena {nombre} {apellido}! \n\nSu asistencia fue registrada.")
            self.label_texto1.setStyleSheet("background-color: #DAD7CD; color: #000;")
        except Error as e:
                errorConsulta("Registro de asistecia", f"Error al registrar la asistencia: {str(e)}")
        finally:
            cursor.close()
            conn.close()           
      
            # diferencia_dias = (fecha_hoy - fecha_registro).days
            # print(f"Diferencia de días: {diferencia_dias}")
                    
            # fecha_registro += timedelta(days=30)
            
            # Mensajes a mostrar         
            
        while True:
            # diferencia_dias = (fecha_hoy - fecha_registro).days
            diferencia_dias = (fecha_registro - fecha_hoy).days
            
            texto_cuota = f"\nÚltimo pago: {fecha_registro.strftime('%d/%m/%Y')}. \n\nPróximo pago en {abs(diferencia_dias)} días.\n"
            texto_vencido2 = f"Cuota vencida hace {abs(diferencia_dias)} días. \n\nÚltimo pago: {fecha_registro.strftime('%d/%m/%Y')}.\n\nDebe abonar su cuota."
            print(f"{diferencia_dias}\n")
            
            # Condiciones basadas en la diferencia de días
            if 30 > abs(diferencia_dias) > 14:
                self.label_texto2.setText(texto_cuota)
                self.label_texto2.setStyleSheet("background-color: #7FFF00; color: #000;")
                # while 30 > diferencia_dias > 14:
                #     fecha_registro += timedelta(days=30)
                #     diferencia_dias = (fecha_hoy - fecha_registro).days
                # self.label_texto2.setText(texto_cuota)
                # self.label_texto2.setStyleSheet("background-color: #7FFF00; color: #000;") 
                print(f"Nueva fecha de registro: {fecha_registro}")
                print(f"Número de días transcurridos para 30 a 15 días: {diferencia_dias}")
                break
            elif 14 >= abs(diferencia_dias) > 4:
                self.label_texto2.setText(texto_cuota)
                self.label_texto2.setStyleSheet("background-color: #FFFF00;color: #000;")
                # while 14 >= diferencia_dias > 4:
                #     fecha_registro += timedelta(days=30)
                #     diferencia_dias = (fecha_hoy - fecha_registro).days
                # self.label_texto2.setText(texto_cuota)
                # self.label_texto2.setStyleSheet("background-color: #FFFF00;color: #000;")
                print(f"Número de días transcurridos para 14 a 5 días: {diferencia_dias}")
                break
            elif 4 >= abs(diferencia_dias) >= 0:
                self.label_texto2.setText(texto_cuota)
                self.label_texto2.setStyleSheet("background-color: #FF8000; color: #000;")
                # while 4 >= diferencia_dias >= 0:
                #     fecha_registro += timedelta(days=30)
                #     diferencia_dias = (fecha_hoy - fecha_registro).days
                # self.label_texto2.setText(texto_cuota)
                # self.label_texto2.setStyleSheet("background-color: #FF8000; color: #000;")
                print(f"Número de días transcurridos para 4 a 0 días: {diferencia_dias}")
                break
            else:
                abs(diferencia_dias) >= 30
                self.label_texto2.setText(texto_vencido2)
                self.label_texto2.setStyleSheet("background-color: #FF0000; color: #fff;")
                # while diferencia_dias > 30:
                #     fecha_registro += timedelta(days=30)
                #     diferencia_dias = (fecha_hoy - fecha_registro).days
                #     print(f"Nueva fecha de registro: {fecha_registro}")
                print("Se han superado los 30 días desde el último pago.")
                break  # Si diferencia_dias es menor o igual a 0, romper el bucle
            
        self.numero_documento.clear()
            
            # Actualizar la fecha de registro sumando 30 días
            # fecha_registro += timedelta(days=30)
            
            
            
        # if dni is None:
        #     fecha_registro += timedelta(days=30)
            

        
        
    