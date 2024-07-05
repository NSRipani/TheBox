import sys
import os
import json
from PyQt6.QtWidgets import QDialog, QLabel, QListWidgetItem, QFileDialog, QTextEdit, QHBoxLayout, QMessageBox, QListWidget, QPushButton, QVBoxLayout, QApplication
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import *

from qss import style
from modulos.mensajes import inicio

class ArchivoTexto(QDialog):
    CONFIG_FILE = "archivos_config.json"  # Definir la constante de clase correctamente

    def __init__(self):
        super().__init__()
        self.archivos = []  # Lista para almacenar los nombres de archivos
        self.cargar_archivos()  # Cargar los archivos guardados al iniciar
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
        self.save_button = QPushButton()
        self.save_button.setIcon(QIcon("img/disquete.png"))
        self.save_button.setIconSize(QSize(35,35))
        self.save_button.setStyleSheet(style.estilo_boton)
        self.save_button.clicked.connect(self.guardar_archivo)
        
        self.open_button = QPushButton()
        self.open_button.setIcon(QIcon("img/carpeta-abierta.png"))
        self.open_button.setIconSize(QSize(35,35))
        self.open_button.setStyleSheet(style.estilo_boton)
        self.open_button.clicked.connect(self.abrir_archivo)
        
        self.delete_button = QPushButton()
        self.delete_button.setIcon(QIcon("img/expediente.png"))
        self.delete_button.setIconSize(QSize(35,35))
        self.delete_button.setStyleSheet(style.estilo_boton)
        self.delete_button.clicked.connect(self.eliminar_archivo)
        
        self.limpiar_button = QPushButton()
        self.limpiar_button.setIcon(QIcon("img/cepillar.png"))
        self.limpiar_button.setIconSize(QSize(35,35))
        self.limpiar_button.setStyleSheet(style.estilo_boton)
        self.limpiar_button.clicked.connect(self.clear)
        # self.limpiar_button.clicked.connect(self.reject)
        
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.open_button)
        button_layout.addWidget(self.delete_button)
        button_layout.addWidget(self.limpiar_button)
        left_layout.addLayout(button_layout)

        # Lado derecho (lista de archivos)
        right_layout = QVBoxLayout()
        self.archivo_list = QListWidget()
        self.archivo_list.setStyleSheet(style.estilo_lista)
        self.archivo_list.setIconSize(QSize(32, 32))  # Cambiar el tamaño del icono
        self.archivo_list.itemClicked.connect(self.mostrar_contenido_archivo)
        right_layout.addWidget(self.archivo_list)

        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

        self.setLayout(main_layout)

        self.actualizar_lista_archivos()  # Actualizar la lista de archivos en la interfaz

    def guardar_archivo(self):
        texto_contenido = self.text_edit.toPlainText()
        nombre_archivo, _ = QFileDialog.getSaveFileName(self, "Guardar archivo de texto", "", "Archivos de texto (*.txt)")

        if nombre_archivo:
            try:
                with open(nombre_archivo, "w") as archivo:
                    archivo.write(texto_contenido)
                if nombre_archivo not in self.archivos:
                    self.archivos.append(nombre_archivo)
                    self.text_edit.clear()
                self.actualizar_lista_archivos()
            except Exception as e:
                print(f"Error al guardar el archivo: {e}")

    def abrir_archivo(self):
        nombre_archivo, _ = QFileDialog.getOpenFileName(self, "Abrir archivo de texto", "", "Archivos de texto (*.txt)")

        if nombre_archivo:
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
        nombre_archivo = item.data(Qt.ItemDataRole.UserRole)
        try:
            with open(nombre_archivo, "r") as archivo:
                contenido = archivo.read()
                self.text_edit.setText(contenido)
        except FileNotFoundError:
            print(f"El archivo '{nombre_archivo}' no se encuentra. Eliminándolo de la lista.")
            self.archivos.remove(nombre_archivo)
            self.actualizar_lista_archivos()
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
        # nombre_archivo = item.text()
        # try:
        #     with open(nombre_archivo, "r") as archivo:
        #         contenido = archivo.read()
        #         self.text_edit.setText(contenido)
        # except Exception as e:
        #     print(f"Error al leer el archivo: {e}")

    def eliminar_archivo(self):
        item_seleccionado = self.archivo_list.currentItem()
        if item_seleccionado:
            nombre_archivo = item_seleccionado.text()
            confirmacion = inicio("Eliminar archivo", f"¿Estás seguro de que deseas eliminar '{nombre_archivo}'?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if confirmacion == QMessageBox.StandardButton.Yes:
                self.archivos.remove(nombre_archivo)
                self.actualizar_lista_archivos()
                self.text_edit.clear()
                
    def clear(self):
        self.text_edit.clear()
        
    def actualizar_lista_archivos(self):
        self.archivo_list.clear()
        icono = QIcon("img/archivo.png")  # Asegúrate de tener este archivo en la ubicación correcta
        archivos_validos = [archivo for archivo in self.archivos if os.path.exists(archivo)]
        self.archivos = archivos_validos
        for archivo in self.archivos:
            item = QListWidgetItem(icono, os.path.basename(archivo))
            item.setData(Qt.ItemDataRole.UserRole, archivo)
            self.archivo_list.addItem(item)
        self.guardar_archivos()  # Guardar la lista de archivos en el archivo JSON
        # self.archivo_list.clear()
        # for archivo in self.archivos:
        #     self.archivo_list.addItem(archivo)
        # self.guardar_archivos()  # Guardar la lista de archivos en el archivo JSON

    def guardar_archivos(self):
        try:
            with open(ArchivoTexto.CONFIG_FILE, "w") as config_file:
                json.dump(self.archivos, config_file)
        except Exception as e:
            print(f"Error al guardar la configuración: {e}")

    def cargar_archivos(self):
        try:
            with open(ArchivoTexto.CONFIG_FILE, "r") as config_file:
                self.archivos = json.load(config_file)
        except FileNotFoundError:
            self.archivos = []
        except json.JSONDecodeError:
            print("Error al decodificar el archivo de configuración.")
            self.archivos = []
        except Exception as e:
            print(f"Error al cargar la configuración: {e}")
            self.archivos = []

def main():
    app = QApplication(sys.argv)
    dialog = ArchivoTexto()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
