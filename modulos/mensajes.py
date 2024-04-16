# Librerías de PyQt6
from PyQt6.QtWidgets import QMessageBox, QFileDialog
from PyQt6.QtGui import QIcon

# Módulo de Estilos
from qss import style

   
#THE_BOXING
def mensaje_ingreso_datos(win_title,message):
    mensaje = QMessageBox()
    mensaje.setWindowIcon(QIcon("img/icono-QMessage.png"))
    mensaje.setStyleSheet(style.message_box_estilos_eliminar_profesor)
    mensaje.setWindowTitle(win_title)
    mensaje.setText(message)
    mensaje.setStandardButtons(QMessageBox.StandardButton.Ok)
    mensaje.exec()
    
def inicio(title,text):
    message_box = QMessageBox()
    message_box.setWindowIcon(QIcon("img/icono-QMessage.png"))
    message_box.setStyleSheet(style.message_box_estilos_eliminar_profesor)
    message_box.setWindowTitle(title)
    message_box.setText(text)
    message_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    message_box.setDefaultButton(QMessageBox.StandardButton.No)
    consulta = message_box.exec()
    return consulta

def errorConsulta(mensaje,ex):
    message_box = QMessageBox()
    message_box.setStyleSheet(style.message_box_estilos_eliminar_profesor)
    message_box.setWindowIcon(QIcon("img/icono-QMessage.png"))
    message_box.setWindowTitle(mensaje)
    message_box.setText(ex)
    message_box.setDefaultButton(QMessageBox.StandardButton.Ok)
    message_box.exec()

def aviso_resultado(mensaje,results):
    aviso2 = QMessageBox()
    aviso2.setWindowIcon(QIcon("img/icono-QMessage.png"))
    aviso2.setStyleSheet(style.message_box_estilos_eliminar_profesor)
    aviso2.setWindowTitle(mensaje)
    aviso2.setText(results)
    aviso2.setDefaultButton(QMessageBox.StandardButton.Ok)
    aviso2.exec()
    
def resultado_empleado(mensaje1,busqueda):
    aviso2 = QMessageBox()
    aviso2.setWindowIcon(QIcon("img/icono-QMessage.png"))
    aviso2.setStyleSheet(style.message_box_estilos_eliminar_profesor)
    aviso2.setWindowTitle(mensaje1)
    aviso2.setText(busqueda)
    aviso2.setDefaultButton(QMessageBox.StandardButton.Ok)
    aviso2.exec()
    
def aviso_resultado_asistencias(referenicia,alumno):
    aviso3 = QMessageBox()
    aviso3.setWindowIcon(QIcon("img/icono-QMessage.png"))
    aviso3.setStyleSheet(style.message_box_estilos_eliminar_profesor)
    aviso3.setWindowTitle(referenicia)
    aviso3.setText(alumno)
    aviso3.setDefaultButton(QMessageBox.StandardButton.Ok)
    aviso3.exec()

def aviso_descarga_execl():
    excel = QFileDialog()
    excel.setStyleSheet(style.message_box_estilos_eliminar_profesor)
    excel.getSaveFileName()
    excel.setWindowIcon(QIcon("img/excel.png"))
    
def aviso_Advertencia_De_excel(encabezado,file_path):
    aviso3 = QMessageBox()
    aviso3.setStyleSheet(style.message_box_estilos_eliminar_profesor)
    aviso3.setWindowTitle(encabezado)
    aviso3.setText(file_path)
    aviso3.setWindowIcon(QIcon("img/excel.png"))
    aviso3.setDefaultButton(QMessageBox.StandardButton.Ok)
    aviso3.exec()
    
def aviso_descargaExitosa(encabezado,muestra):
    aviso3 = QMessageBox()
    aviso3.setStyleSheet(style.message_box_estilos_eliminar_profesor)
    aviso3.setWindowTitle(encabezado)
    aviso3.setText(muestra)
    aviso3.setWindowIcon(QIcon("img/excel.png"))
    aviso3.setDefaultButton(QMessageBox.StandardButton.Ok)
    aviso3.exec()
    
def mensaje_horas_empleados(win_title2,message2):
    mensaje = QMessageBox()
    mensaje.setStyleSheet(style.message_box_estilos_eliminar_profesor)
    mensaje.setWindowTitle(win_title2)
    mensaje.setText(message2)
    mensaje.setWindowIcon(QIcon("img/icono-QMessage.png"))
    mensaje.setStandardButtons(QMessageBox.StandardButton.Ok)
    mensaje.exec()
    