import sys
from PyQt6.QtWidgets import (QDialog, QLabel, QFileDialog, QTextEdit, QAbstractScrollArea, QHeaderView, QGridLayout, QHBoxLayout, QDateEdit, 
                             QMessageBox, QListWidget, QAbstractItemView, QTableWidgetItem, QPushButton, QLineEdit, QStatusBar, QWidget,
                             QVBoxLayout, QGroupBox, QMainWindow, QFrame, QTabWidget, QApplication)
from PyQt6.QtGui import QIcon, QKeySequence, QAction, QPixmap
from PyQt6.QtCore import *

from qss import style

class ArchivoTexto(QDialog):
    def __init__(self):
        super().__init__()
        self.archivos = []  # Lista para almacenar los nombres de archivos
        self.archivo_texto()
        self.show()
        
    def archivo_texto(self):
        self.setWindowTitle("Crear archivo de texto")
        self.setModal(True)
        self.setMinimumSize(1000, 600)
        self.setStyleSheet(style.fondo)
        self.setWindowIcon(QIcon("img/logo.png"))

        main_layout = QHBoxLayout()

        # Lado izquierdo (texto)
        left_layout = QVBoxLayout()
        
        # Agregar el título
        self.titulo_label = QLabel("Crear nuevo archivo de texto")
        self.titulo_label.setStyleSheet(style.label)
        left_layout.addWidget(self.titulo_label)
        
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("Escribe el contenido del archivo de texto aquí...")
        self.text_edit.setStyleSheet(style.textEdit)
        left_layout.addWidget(self.text_edit)

        button_layout = QHBoxLayout()
        self.save_button = QPushButton("Guardar")
        self.save_button.setStyleSheet(style.estilo_boton)
        self.save_button.clicked.connect(self.guardar_archivo)
        self.open_button = QPushButton("Abrir")
        self.open_button.setStyleSheet(style.estilo_boton)
        self.open_button.clicked.connect(self.abrir_archivo)
        self.delete_button = QPushButton("Eliminar")
        self.delete_button.setStyleSheet(style.estilo_boton)
        self.delete_button.clicked.connect(self.eliminar_archivo)
        self.cancel_button = QPushButton("Cancelar")
        self.cancel_button.setStyleSheet(style.estilo_boton)
        self.cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.open_button)
        button_layout.addWidget(self.cancel_button)
        left_layout.addLayout(button_layout)

        # Lado derecho (lista de archivos)
        right_layout = QVBoxLayout()
        self.archivo_list = QListWidget()
        self.archivo_list.setStyleSheet("QListWidget" 
                                        "{"
                                        "background-color: #333333;"
                                        "color: #f1f1f1;"
                                        "font-size: 14px;"
                                        "font-family: 'Courier New', monospace;"
                                        "padding: 10px;"
                                        "border: none;"
                                        "outline: none;"
                                        "}"
                                        "QListWidget::item" 
                                        "{"
                                        "padding: 5px 10px;"
                                        "border-radius: 5px;"
                                        "}"
                                        "QListWidget::item:hover" "{"
                                        "background-color: #444444;"
                                        "}"
                                        "QListWidget::item:selected" "{"
                                        "background-color: #4CAF50;"                color: #1f1f1f;
                                        "}"
                                        )
        self.archivo_list.itemClicked.connect(self.mostrar_contenido_archivo)
        right_layout.addWidget(self.archivo_list)

        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)
        
        self.setLayout(main_layout)

    def guardar_archivo(self):
        # Obtener el contenido del QTextEdit
        texto_contenido = self.text_edit.toPlainText()

        # Abrir el diálogo de guardado de archivo
        nombre_archivo, _ = QFileDialog.getSaveFileName(self, "Guardar archivo de texto", "", "Archivos de texto (*.txt)")

        if nombre_archivo:
            # Guardar el archivo de texto
            try:
                with open(nombre_archivo, "w") as archivo:
                    archivo.write(texto_contenido)
                if nombre_archivo not in self.archivos:
                    self.archivos.append(nombre_archivo)
                    self.text_edit.clear()  # Limpiar el QTextEdit después de guardar el archivo
                self.actualizar_lista_archivos()
            except Exception as e:
                print(f"Error al guardar el archivo: {e}")

    def abrir_archivo(self):
        # Abrir el diálogo de selección de archivo
        nombre_archivo, _ = QFileDialog.getOpenFileName(self, "Abrir archivo de texto", "", "Archivos de texto (*.txt)")

        if nombre_archivo:
            # Leer el contenido del archivo y mostrarlo en el QTextEdit
            try:
                with open(nombre_archivo, "r") as archivo:
                    contenido = archivo.read()
                    self.text_edit.setText(contenido)
                    if nombre_archivo not in self.archivos:
                        self.archivos.append(nombre_archivo)
                    self.actualizar_lista_archivos()
            except Exception as e:
                print(f"Error al abrir el archivo: {e}")

    def mostrar_contenido_archivo(self, item):
        # Obtener el nombre del archivo seleccionado
        nombre_archivo = item.text()

        # Leer el contenido del archivo y mostrarlo en el QTextEdit
        try:
            with open(nombre_archivo, "r") as archivo:
                contenido = archivo.read()
                self.text_edit.setText(contenido)
        except Exception as e:
            print(f"Error al leer el archivo: {e}")

    def eliminar_archivo(self):
        # Obtener el archivo seleccionado
        item_seleccionado = self.archivo_list.currentItem()
        if item_seleccionado:
            nombre_archivo = item_seleccionado.text()
            # Confirmar eliminación
            confirmacion = QMessageBox.question(self, "Eliminar archivo", f"¿Estás seguro de que deseas eliminar '{nombre_archivo}'?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if confirmacion == QMessageBox.StandardButton.Yes:
                self.archivos.remove(nombre_archivo)
                self.actualizar_lista_archivos()
                self.text_edit.clear()
                
    def actualizar_lista_archivos(self):
        self.archivo_list.clear()
        for archivo in self.archivos:
            self.archivo_list.addItem(archivo)

def main():
    app = QApplication(sys.argv)
    dialog = ArchivoTexto()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()


# # Librerías de PyQt6
# from PyQt6.QtWidgets import (QDialog, QLabel,QFileDialog, QTextEdit, QAbstractScrollArea, QHeaderView, QGridLayout, QHBoxLayout, QDateEdit, 
#                              QMessageBox, QListWidget, QAbstractItemView, QTableWidgetItem, QPushButton, QLineEdit, QStatusBar, QWidget,
#                              QVBoxLayout, QGroupBox, QMainWindow, QFrame, QTabWidget)
# from PyQt6.QtGui import QIcon, QKeySequence, QAction, QPixmap
# from PyQt6.QtCore import *

# # Módulo de Estilos
# from qss import style

# class ArchivoTexto(QDialog):
#     def __init__(self):
#         super().__init__()
#         self.archivos = []  # Lista para almacenar los nombres de archivos
#         self.archivo_texto()
#         self.show()
        
#     def archivo_texto(self):
#         self.setWindowTitle("Crear archivo de texto")
#         self.setModal(True)
#         self.setMinimumSize(600, 400)
#         self.setStyleSheet(style.fondo)
#         self.setWindowIcon(QIcon("img/logo.png"))

#         main_layout = QHBoxLayout()

#         # Lado izquierdo (texto)
#         left_layout = QVBoxLayout()
        
#         # Agregar el título
#         self.titulo_label = QLabel("Crear nuevo archivo de texto")
#         self.titulo_label.setStyleSheet(style.label)
#         left_layout.addWidget(self.titulo_label)
        
#         self.text_edit = QTextEdit()
#         self.text_edit.setPlaceholderText("Escribe el contenido del archivo de texto aquí...")
#         self.text_edit.setStyleSheet(style.textEdit)
#         left_layout.addWidget(self.text_edit)

#         button_layout = QHBoxLayout()
#         self.save_button = QPushButton("Guardar")
#         self.save_button.setStyleSheet(style.estilo_boton)
#         self.save_button.clicked.connect(self.guardar_archivo)
#         self.open_button = QPushButton("Abrir")
#         self.open_button.setStyleSheet(style.estilo_boton)
#         self.open_button.clicked.connect(self.abrir_archivo)
#         self.cancel_button = QPushButton("Cancelar")
#         self.cancel_button.setStyleSheet(style.estilo_boton)
#         self.cancel_button.clicked.connect(self.reject)
#         button_layout.addWidget(self.save_button)
#         button_layout.addWidget(self.open_button)
#         button_layout.addWidget(self.cancel_button)
#         left_layout.addLayout(button_layout)

#         # Lado derecho (lista de archivos)
#         right_layout = QVBoxLayout()
#         self.archivo_list = QListWidget()
#         self.archivo_list.setStyleSheet(style.estilo_lista)
#         self.archivo_list.itemClicked.connect(self.mostrar_contenido_archivo)
#         right_layout.addWidget(self.archivo_list)

#         main_layout.addLayout(left_layout)
#         main_layout.addLayout(right_layout)
        
#         self.setLayout(main_layout)

#     def guardar_archivo(self):
#         # Obtener el contenido del QTextEdit
#         texto_contenido = self.text_edit.toPlainText()

#         # Abrir el diálogo de guardado de archivo
#         # opciones_archivo = QFileDialog.options()
#         nombre_archivo, _ = QFileDialog.getSaveFileName(self, "Guardar archivo de texto", "", "Archivos de texto (*.txt)")

#         if nombre_archivo:
#             # Guardar el archivo de texto
#             try:
#                 with open(nombre_archivo, "w") as archivo:
#                     archivo.write(texto_contenido)
#                 if nombre_archivo not in self.archivos:
#                     self.archivos.append(nombre_archivo)
#                     self.text_edit.clear()  # Limpiar el QTextEdit después de guardar el archivo                    
#                 # self.archivo_list.addItem(nombre_archivo)
#                 self.actualizar_lista_archivos()
#                 # self.accept()
#             except Exception as e:
#                 print(f"Error al guardar el archivo: {e}")
#         # else:
#         #     self.reject()
        
        
#     def abrir_archivo(self):
#         # Abrir el diálogo de selección de archivo
#         nombre_archivo, _ = QFileDialog.getOpenFileName(self, "Abrir archivo de texto", "", "Archivos de texto (*.txt)")

#         if nombre_archivo:
#             # Leer el contenido del archivo y mostrarlo en el QTextEdit
#             try:
#                 with open(nombre_archivo, "r") as archivo:
#                     contenido = archivo.read()
#                     self.text_edit.setText(contenido)
#                     if nombre_archivo not in self.archivos:
#                         self.archivos.append(nombre_archivo)
#                     self.actualizar_lista_archivos()
#             except Exception as e:
#                 print(f"Error al abrir el archivo: {e}")

#     def mostrar_contenido_archivo(self, item):
#         # Obtener el nombre del archivo seleccionado
#         nombre_archivo = item.text()

#         # Leer el contenido del archivo y mostrarlo en el QTextEdit
#         try:
#             with open(nombre_archivo, "r") as archivo:
#                 contenido = archivo.read()
#                 self.text_edit.setText(contenido)
#         except Exception as e:
#             print(f"Error al leer el archivo: {e}")

#     def actualizar_lista_archivos(self):
#         self.archivo_list.clear()
#         for archivo in self.archivos:
#             self.archivo_list.addItem(archivo)