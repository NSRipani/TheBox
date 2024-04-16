# Libreria para manejar directorios
from pathlib import Path

def obtener_ruta_imagen(nombre_imagen):
    base_path = Path.cwd()  # Obtiene el directorio actual como base para las rutas relativas
    image_folder = "img"  # Carpeta que contiene las imágenes
    return str(base_path / image_folder / nombre_imagen)  # Retorna el path completo de la imagen

