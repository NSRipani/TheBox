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
            # cursor.execute("SELECT u.id_usuario, p.id_disciplina FROM usuario u JOIN pago p ON u.dni = %s", (dni,))
            cursor.execute("SELECT p.id_usuario, p.id_disciplina FROM pago p WHERE p.id_usuario = %s", (dni,))
            result = cursor.fetchall()

            # Paso 2: Comprobar si se obtuvieron resultados
            # if len(result) > 0:
            #     u_dni = result[0]
            #     id_disciplina = result[1]
                # print(f"ID: {id_usuario[0]}, ID DIS: {id_disciplina[1]}")
                # Chequear si la combinación ya existe en la tabla 'asistencia'
                # cursor.execute("SELECT COUNT(*) FROM asistencia WHERE id_usuario = %s AND id_disciplina = %s", (u_dni, id_disciplina))
                # if cursor.fetchone()[0] == 0:
            if len(result) > 0:
                disciplinas_registradas = []
                for row in result:
                    u_dni = row[0]
                    id_disciplina = row[1]

                    # Verificar si ya existe un registro de asistencia para el usuario y la disciplina en la fecha actual
                    fecha_hoy = date.today()
                    cursor.execute("SELECT COUNT(*) FROM asistencia WHERE dni = %s AND id_disciplina = %s AND asistencia = %s", (u_dni, id_disciplina, fecha_hoy))
                    registros_existentes = cursor.fetchone()[0]

                    if registros_existentes == 0:
                        # Insertar los datos de asistencia
                        cursor.execute("INSERT INTO asistencia (asistencia, dni, id_disciplina) VALUES (%s, %s, %s)", (fecha_hoy, u_dni, id_disciplina))
                        conn.commit()
                        print(f"Se ha insertado un registro de asistencia para el usuario con DNI {u_dni} y la disciplina {id_disciplina} en la fecha {fecha_hoy}.")
                        disciplinas_registradas.append(id_disciplina)
                    else:
                        print(f"Ya existe un registro de asistencia para el usuario con DNI {u_dni} y la disciplina {id_disciplina} en la fecha {fecha_hoy}. No se registrará de nuevo.")

                # Verificar si se registraron todas las disciplinas
                if len(result) == len(disciplinas_registradas):
                    print(f"Se han registrado todas las disciplinas relacionadas al DNI {dni}.")
                else:
                    print(f"No se han podido registrar todas las disciplinas relacionadas al DNI {dni}.")
            else:
                print(f"No se encontraron resultados para el usuario con DNI {dni}.")
                
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
            
            # Paso 1: Obtener la última fecha registrada para el usuario
            cursor.execute("SELECT p.fecha FROM pago p WHERE p.id_usuario = %s ORDER BY p.fecha DESC LIMIT 1", (dni,))
            ultima_fecha = cursor.fetchone()
            ultima_fecha = ultima_fecha[0]
            print(ultima_fecha)

            # Paso 2: Calcular la diferencia de días entre la fecha actual y la última fecha registrada
            fecha_actual = datetime.now().date()
            diferencia_dias = (ultima_fecha + timedelta(days=30))
            dias = diferencia_dias - fecha_actual
            print(diferencia_dias)
            
            ultima = ultima_fecha.strftime("%d/%m/%Y")
            
            texto_cuota = f"\nÚltimo pago: {ultima}. \n\nPróximo pago en {dias} días.\n"
            texto_vencido = f"Cuota vencida hace {dias} días. \n\nÚltimo pago: {ultima}.\n\nDebe abonar su cuota."
            
            if 30 < dias.days < 14:
                self.label_texto2.setText(texto_cuota)
                self.label_texto2.setStyleSheet("background-color: #7FFF00; color: #000;")
            elif dias.days < 14:
                self.label_texto2.setText(texto_cuota)
                self.label_texto2.setStyleSheet("background-color: #FFFF00;color: #000;")
            elif 4 >= dias.days <= 0:
                self.label_texto2.setText(texto_cuota)
                self.label_texto2.setStyleSheet("background-color: #FF8000; color: #000;")
            else:
                self.label_texto2.setText(texto_vencido)
                self.label_texto2.setStyleSheet("background-color: #FF0000; color: #fff;")
                
            self.numero_documento.clear()

        except Error as e:
            errorConsulta("Registro de asistencia", f"Error al registrar la asistencia: {str(e)}")
            print(e)
        finally:
            cursor.close()
            conn.close()
            




#-------------------------------------------------
# Paso 2: Comprobar si se obtuvieron resultados
# if len(result) > 0:
#     # Crear un diccionario para contar las combinaciones
#     combinaciones = {}
    
#     for registro in result:
#         id_usuario = registro[0]
#         id_disciplina = registro[1]
#         if id_usuario in combinaciones:
#             combinaciones[id_usuario].append(id_disciplina)
#         else:
#             combinaciones[id_usuario] = [id_disciplina]
    
#     # Paso 3: Identificar los id_usuario con más de una combinación
#     usuarios_con_multiples_disciplina = {usuario: disciplinas for usuario, disciplinas in combinaciones.items() if len(disciplinas) > 1}
#     print(usuarios_con_multiples_disciplina)
#     # Imprimir los usuarios y sus disciplinas
#     for usuario, disciplinas in usuarios_con_multiples_disciplina.items():
#         print(f"ID Usuario: {usuario}, ID Disciplinas: {disciplinas}")
        
#         # Paso 4: Insertar las combinaciones en otra tabla sin repetir 'id_disciplina'
#         for disciplina in disciplinas:
#             # Chequear si la combinación ya existe en la tabla 'asistencia'
#             cursor.execute("SELECT COUNT(*) FROM asistencia WHERE id_usuario = %s AND id_disciplina = %s", (usuario, disciplina))
#             if cursor.fetchone()[0] == 0:
#                 cursor.execute("INSERT INTO asistencia (asistencia, id_usuario, id_disciplina) VALUES (%s, %s, %s)", (fecha_hoy, usuario, disciplina))
#         conn.commit()
#         print(disciplinas)