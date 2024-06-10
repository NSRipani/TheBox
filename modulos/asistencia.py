# Librería para uso de fechas
from datetime import datetime, date, timedelta

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
        # Dato ingresado por teclado   
        dni = self.numero_documento.text()
        fecha_hoy = date.today()
        print(fecha_hoy)
        
        # Validar formato de número de documento
        if not dni.isdigit() or len(dni) != 8:
            mensaje_ingreso_datos("Registro de asistencia", "El número de documento debe contener 8 dígitos numéricos.")
            return
        
        try:
            # Conexión a la base de datos MySQL
            conn = conectar_base_de_datos()
            cursor = conn.cursor()
                #---------------------------------------------------
            # Paso 1: Realizar la consulta y obtener todos los registros
            cursor.execute("SELECT u.id_usuario, p.id_disciplina FROM usuario u JOIN pago p ON u.dni = %s", (dni,))
            result = cursor.fetchall()

            # Paso 2: Comprobar si se obtuvieron resultados
            if len(result) > 0:
                # Crear un diccionario para contar las combinaciones
                combinaciones = {}
                
                for registro in result:
                    id_usuario = registro[0]
                    id_disciplina = registro[1]
                    if id_usuario in combinaciones:
                        combinaciones[id_usuario].append(id_disciplina)
                    else:
                        combinaciones[id_usuario] = [id_disciplina]
                
                # Paso 3: Identificar los id_usuario con más de una combinación
                usuarios_con_multiples_disciplina = {usuario: disciplinas for usuario, disciplinas in combinaciones.items() if len(disciplinas) > 1}
                
                # Imprimir los usuarios y sus disciplinas
                for usuario, disciplinas in usuarios_con_multiples_disciplina.items():
                    print(f"ID Usuario: {usuario}, ID Disciplinas: {disciplinas}")
                    
                    # Paso 4: Insertar las combinaciones en otra tabla
                    for disciplina in disciplinas:
                        cursor.execute("INSERT INTO asistencia (asistencia, id_usuario, id_disciplina) VALUES (%s, %s, %s)", (fecha_hoy, usuario, disciplina))
                    conn.commit()
                    print(disciplinas)
            else:
                print("No se encontraron registros.")

                
            # Consultar nombre y apellido del usuario
            cursor.execute("SELECT nombre, apellido FROM usuario WHERE dni = %s", (dni,))
            result_usuario = cursor.fetchone()
            print(result_usuario)
            if len(result_usuario) > 0:
                nombre = result_usuario[0]
                apellido = result_usuario[1]
            
            # Mostrar mensaje en la interfaz
            self.label_texto1.setText(f"¡En hora buena {nombre} {apellido}! \n\nSu asistencia fue registrada.")
            self.label_texto1.setStyleSheet("background-color: #DAD7CD; color: #000;")
            print(nombre)
            
            # Subconsulta para obtener una única fecha por combinación de id_usuario y id_disciplina
            # cursor.execute("""SELECT DISTINCT p.fecha FROM pago p WHERE p.id_usuario IN (SELECT u.id_usuario FROM usuario u WHERE u.dni = %s) AND p.id_disciplina IN
            #                (SELECT p.id_disciplina FROM pago p JOIN usuario u ON p.id_usuario = u.dni WHERE u.dni = %s)""", (dni, dni,))
            # fechas = cursor.fetchall()
            # print(fechas)
            # for fecha in fechas:
            #     fecha_pago = fechas[0]
            #     dias_desde_pago = (fecha_hoy - fecha_pago).days
            #     dias_hasta_30 = 30 - dias_desde_pago
            #     fecha_limite_30_dias = fecha_pago + timedelta(days=30)
            
            # print(fecha_pago)
            # print(dias_desde_pago)
            # print(dias_hasta_30)
            # print(fecha_limite_30_dias)
            # Calcular diferencia de días y mostrar mensajes
            # texto_cuota = f"\nÚltimo pago: {fecha_pago}. \n\nPróximo pago en {dias.days} días.\n"
            # texto_vencido = f"Cuota vencida hace {dias.days} días. \n\nÚltimo pago: {fecha_pago}.\n\nDebe abonar su cuota."
            
            # if 30 > dias.days > 14:
            #     self.label_texto2.setText(texto_cuota)
            #     self.label_texto2.setStyleSheet("background-color: #7FFF00; color: #000;")
            # elif 14 >= dias.days > 4:
            #     self.label_texto2.setText(texto_cuota)
            #     self.label_texto2.setStyleSheet("background-color: #FFFF00;color: #000;")
            # elif 4 >= dias.days >= 0:
            #     self.label_texto2.setText(texto_cuota)
            #     self.label_texto2.setStyleSheet("background-color: #FF8000; color: #000;")
            # else:
            #     self.label_texto2.setText(texto_vencido)
            #     self.label_texto2.setStyleSheet("background-color: #FF0000; color: #fff;")
                
                # Actualizar la fecha de registro para el siguiente ciclo
                # fecha_registro = fecha_limite
                
                # Esperar hasta la medianoche del siguiente día
                # siguiente_dia = datetime.datetime.now() + datetime.timedelta(days=1)
                # siguiente_dia = siguiente_dia.replace(hour=0, minute=0, second=0, microsecond=0)
                # while datetime.datetime.now() < siguiente_dia:
                #     continue
                # break
            self.numero_documento.clear()

        except Error as e:
            errorConsulta("Registro de asistencia", f"Error al registrar la asistencia: {str(e)}")
            print(e)
        finally:
            cursor.close()
            conn.close()
            