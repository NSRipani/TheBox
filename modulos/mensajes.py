# Librerías de PyQt6
from PyQt6.QtWidgets import QMessageBox, QFileDialog
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QTimer

# Módulo de Estilos
from qss import style

   
#THE_BOXING
def mensaje_ingreso_datos(win_title,message):
    mensaje = QMessageBox()
    mensaje.setWindowIcon(QIcon("img/icono-QMessage.png"))
    mensaje.setStyleSheet(style.message_box_estilos_eliminar_profesor)
    mensaje.setWindowTitle(win_title)
    mensaje.setText(message)
    mensaje.setIcon(QMessageBox.Icon.Warning)
    mensaje.setStandardButtons(QMessageBox.StandardButton.Ok)
    
    # Mostrar el mensaje durante 5 segundos
    mensaje.show()
    timer = QTimer()
    timer.singleShot(5000, mensaje.close)
    mensaje.exec()  
        
def ingreso_datos(win_title,message):
    mensaje = QMessageBox()
    mensaje.setWindowIcon(QIcon("img/icono-QMessage.png"))
    mensaje.setStyleSheet(style.message_box_estilos_eliminar_profesor)
    mensaje.setWindowTitle(win_title)
    mensaje.setText(message)
    mensaje.setIcon(QMessageBox.Icon.Information)
    mensaje.setStandardButtons(QMessageBox.StandardButton.Ok)
    
    # Mostrar el mensaje durante 5 segundos
    mensaje.show()
    timer = QTimer()
    timer.singleShot(5000, mensaje.close)
    mensaje.exec()

def ingreso_datos2(win_title,message):
    mensaje2 = QMessageBox()
    mensaje2.setWindowIcon(QIcon("img/icono-QMessage.png"))
    mensaje2.setStyleSheet(style.message_box_estilos_eliminar_profesor)
    mensaje2.setWindowTitle(win_title)
    mensaje2.setText(message)
    mensaje2.setIcon(QMessageBox.Icon.Critical)
    mensaje2.setStandardButtons(QMessageBox.StandardButton.Ok)
    
    # Mostrar el mensaje durante 5 segundos
    mensaje2.show()
    timer = QTimer()
    timer.singleShot(5000, mensaje2.close)
    mensaje2.exec()
    
def inicio(title,text):
    message_box = QMessageBox()
    message_box.setWindowIcon(QIcon("img/icono-QMessage.png"))
    message_box.setStyleSheet(style.message_box_estilos_eliminar_profesor)
    message_box.setWindowTitle(title)
    message_box.setText(text)
    message_box.setIcon(QMessageBox.Icon.Question)
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
    message_box.setIcon(QMessageBox.Icon.Warning)
    message_box.setDefaultButton(QMessageBox.StandardButton.Ok)
    
    # Mostrar el mensaje durante 5 segundos
    message_box.show()
    timer = QTimer()
    timer.singleShot(3000, message_box.close)
    message_box.exec()
    
def aviso_descarga_execl(): # BORRAR
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
    
    # Mostrar el mensaje durante 5 segundos
    aviso3.show()
    timer = QTimer()
    timer.singleShot(5000, aviso3.close)
    aviso3.exec()

# ASISTENCIA    
def mensaje_datos_ingresado(title, message):
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setStyleSheet(style.message_box_estilos_eliminar_profesor)
    msg.setText(message)

    # Mostrar el mensaje durante 5 segundos
    msg.show()
    timer = QTimer()
    timer.singleShot(5000, msg.close)
    msg.exec()