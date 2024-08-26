# setup.py

from distutils.core import setup, find_packages
import py2exe

setup(
    console=['theBox.py'],  # Cambia 'mi_app.py' por el nombre de tu archivo
    options={
        'py2exe': {
            'bundle_files': 1,  # Agrupa todo en un solo archivo
            'compressed': True,  # Comprime el ejecutable
        }
    },
    data_files=[  # Archivos adicionales a incluir
        ('',['actualizar-alumno.png', 'archivo.png','asistencia.png','balance.png','buscar-alumno.png','carpeta-abierta.png','cepillar.png','cobrar.png','contabilidad.png','controlar.png','disciplina.png','disquete.png','eliminar-alumno.png','empleado.png','excel.png','expediente.png','flecha-combo.png','hora.png','icono-QMessage.png','logo.png','registro-alumno.png','resumen.png'])
    ],
    zipfile=None,  # No crea un archivo zip adicional
    packages=find_packages(include=['db', 'img', 'qss', 'backup', 'modulos', 'conexion_DB', 'validaciones']),
)
