##################################################################
# 
#           ESTILOS PARA OBJETOS
#
##################################################################

windowsTitle = """
    QMainWindow {
        background-color: #333;
    }
    QMainWindow::title {
        background-color: #444;
        color: white;
        padding: 6px;
    }
    QMainWindow::title:hover {
        background-color: #555;
    }
    """
# LOGIN
fondo_logo = """
    Login{
        background-color: QLinearGradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #ffffff, stop: 0.45 #fcb045,stop: 0.66 #ff9500, stop: 1 #000000);
    }"""

logo_label = """
    QLabel{
        background-color: transparent;
    }"""
est = """
    QLabel{
        color: #333;
        font-size: 16px;
        font-weight: bold;
    }"""
lineedit_logo = """
    QLineEdit{
        border: 2px solid #3498db; 
        border-radius: 4px; 
        background-color: #f2f2f2; 
        color: #333;
    }
    QLineEdit:hover{
        background-color: #adb5bd;
    }"""
checkbox_style = """
    QCheckBox {
        color: #333333;
        font-size: 14px;
    }
    
    QCheckBox::indicator {
        width: 16px;
        height: 16px;
        background-color: #ffffff;
        border: 2px solid #000000;
        border-radius: 3px;
    }
    
    QCheckBox::indicator:unchecked {
        background-color: #ffffff;
    }
    
    QCheckBox::indicator:checked {
        image: url("img/controlar.png");
        background-color: #0291fe;
        border-color: #0291fe;
    }
    
    QCheckBox::indicator:hover {
        border-color: #999999;
    }
    
    QCheckBox::indicator:pressed {
        background-color: #e6e6e6;
    }
"""

estBo = """
    QPushButton{
        color: white;
        border:1px solid #e85d04;
        border-radius:5px;
        background-color: #e85d04;
        font-weight: bold;
        font-style: "Segoe UI";
        font-size: 15px
    }
    QPushButton:hover {
        background-color: #d3d3d3;
        color: black;
    }
    QPushButton:pressed {
        background-color: #ff9a2e;
    }"""

# REGISTRO DE PROFESOR
fondo = """
    QDialog{
        background-color: QLinearGradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #ffffff, stop: 0.45 #fcb045,stop: 0.66 #ff9500, stop: 1 #000000);
    }"""

label_titulo_profesor = """
    QLabel{
        background-color: transparent;
        font-size: 20px;
        font-family: "Segoe UI";
        font-weight: bold;
        color: #000000;
    }"""
    
botones_profesores = """
    QPushButton {
        background-color: #e85d04;
        color: white;
        border: 1px solid #e85d04;
        border-radius: 5px;
        padding: 5px 10px;
        font-weight: bold;
        font-size: 16px;
    }
    QPushButton:hover {
        color: black;
        background-color: #d3d3d3;
    }
    QPushButton:pressed {
        background-color: #ff9a2e;
    }"""

qgrupo_profesor = """
    QGroupBox{
        border: 2px solid black;
        color: black;
        border-radius: 5px;
        font: 15px;
        font-weight: bold;
        font-family: "Segoe UI";
        background-color: #ffb268;
        margin-top: 5px;
        padding: 5px 0px; 
    }
    QGroupBox:title { 
        subcontrol-origin: margin; 
        subcontrol-position: top left;
        padding: 5px 0px;
        margin-top: -10px;
    }"""
    
label_profesor = """
    QLabel{
        background-color: transparent;
        color: black;
        font-size: 12px;
        font-family: "Segoe UI";
    }"""
    
lineedit_profesor = """
    QLineEdit{
        color: black;
        background-color: white;
        border: 1px solid black;
        border-radius: 4px;
        font-size: 12px;
        font-family: "Segoe UI";
    }
    QLineEdit:hover{
        background-color: #adb5bd;
    }"""
    
tabla_profesor = """
    QTableWidget{
        background-color: #f5ebe0;
        color: black;
        gridline-color: black;
        font-size: 13px;/*20*/
        font-family: "Segoe UI";
    }
    QHeaderView::section{
        background-color: #9a9a9a; /*#9a9a9a;*/
        color: black;
        font-weight: bold;
        font-size: 13px;/*20*/
    }
    QScrollBar:vertical {
        background-color: #808080; 
        width: 15px; 
    }
    QScrollBar:horizontal {
        background-color: #808080; 
        height: 15px; 
    }
    """

# ELIMINAR PROFESOR

    # SE USA PARA TODOS LOS MODULOS
message_box_estilos_eliminar_profesor = """
    QMessageBox {
        background-color: #F5F5DC;
    }
    QMessageBox QLabel {
        color: black;
        text-align: start;
        margin: 1px 5px;
        padding: 5px;
        font: 15px;
    }
    QMessageBox QPushButton {
        background-color: #e85d04;
        color: black;
        font-weight: bold;
        border: 1px solid e85d04;
        padding: 5px 40px;
        border-radius: 6px;
    }
    QMessageBox QPushButton:hover{
        background-color: #737272;
    }
    QMessageBox QPushButton:pressed {
        background-color: #be4e0c;
    }"""

# VENTANA PRINCIPAL
fondo2 = """
    QWidget{
        background-color: QLinearGradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #ffffff, stop: 0.45 #fcb045,stop: 0.66 #ff9500, stop: 1 #000000);
    }"""


estilo_statusbar = """
    QStatusBar{
        background-color: #7f7f7f; 
        color: black; 
        font: 15px;
        font-weight: bold;
    }"""

estilo = """
    QPushButton{
        background-color: #fff;
        color: #000;
        border: 5px solid #ff8000;
        border-radius:20px;
        font-weight: bold;
        font-size: 20px;
    }
    QPushButton:hover {
        background-color: #a9a9a9;
    }
    QPushButton:pressed {
        background-color: #be4e0c;
    }"""

estilo_tab = """
    QTabWidget{
        font-size: 25px;
        font-family: "Segoe UI";
    }
    QTabWidget::pane { 
        background-color: blue;
    }
    QTabBar::tab { 
        background-color: #e85d04; 
        color: white;
        border: 1px solid black;
        border-top-left-radius: 5px;
        border-top-right-radius: 5px;
        width: 200px;
    } 
    QTabBar::tab:selected { 
        background-color: red; color: white;
        font: bold;
    }
    QTabBar::tab:hover {
        background-color: #c2c1c1; 
        color: black;
    }"""

estilo_grupo = """
    QGroupBox{
        border: 1px solid black;
        color: black;
        border-radius: 5px;
        font: 20px;
        font-weight: bold;
        margin-top: 1ex;
        font-family: "Segoe UI";
        background-color: #ffb268;
        margin-top: 5px;
        padding: 5px 0px; 
    }
    QGroupBox:title { 
        subcontrol-origin: margin; 
        subcontrol-position: top left;
        padding: 5px 0px;
        margin-top: -15px;
    }"""

label = """
    QLabel{
        background-color: transparent;
        font-size: 20px;
        font-family: "Segoe UI";
        color: black;
    }"""

label_contable = """
QLabel{
    background-color: transparent;
    color: black;
    font-size: 20px;
    font-family: "Segoe UI";
    font-weight: bold;
}"""

estilo_combo = """
        /* RECUADRO CON ITEMS*/
    QComboBox {
        background-color: #FFFFFF;
        color: black; 
        border: 1px solid black;
        border-radius: 4px;
        font-size: 20px;
        height: 35px;
    }
    QComboBox::drop-down {
        width: 30px;
        subcontrol-origin: padding;
        subcontrol-position: top right;
    }  
    QComboBox::down-arrow {
        background: url("img/flecha-combo.png");
    }
    QComboBox QAbstractItemView {
        background-color: #e3e4e5;
        color: #000000; 
        selection-background-color: #7BA517;
    }
    QScrollBar:vertical {
        border-left-color: 1px solid black;
        background: #c0c0c0;
        width: 30px;
        margin: 30.5px 0 30.5px 0;
        border-radius: 0px;
    }

    /* HANDLE BAR VERTICAL */
    QScrollBar::handle:vertical {    
        background-color: #fcfcfc;
        border: 1px solid black;
    }
    QScrollBar::handle:vertical:hover {    
        background-color: #cccccc;
    }
    QScrollBar::handle:vertical:pressed {    
        background-color: #999999;
    }

    /* BTN TOP - SCROLLBAR */
    QScrollBar::sub-line:vertical {
        border: 1px solid black;
        background: url("img/flecha-combo.png");
        background-color: #fcfcfc;
        height: 30px;
        subcontrol-position: top;
        subcontrol-origin: margin;
    }
    QScrollBar::sub-line:vertical:hover {    
        background-color: #cccccc;
    }
    QScrollBar::sub-line:vertical:pressed {    
        background-color: #999999;
    }

    /* BTN BOTTOM - SCROLLBAR */
    QScrollBar::add-line:vertical {
        border: 1px solid black;
        background: url("img/flecha-combo.png");
        background-color: #fcfcfc;
        height: 30px;
        subcontrol-position: bottom;
        subcontrol-origin: margin;
    }
    QScrollBar::add-line:vertical:hover {    
        background-color: #cccccc;
    }
    QScrollBar::add-line:vertical:pressed {    
        background-color: #999999;
    }

    /* RESET ARROW */
    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
        background: none;
    }
    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
        background: none;
    }"""
completer = """
    QListView { 
        background-color: #f0f0f0; 
        font-size: 25px;
        color: #000000;
    } 
    QListView::item:selected {
        background-color: #7BA517; 
        color: #FFFFFF;
    }
"""
fecha = """
    QDateEdit {
        background-color: #FFFFFF;
        color: #000000;
        border: 1px solid black;
        border-radius: 4px;
        font-size: 20px;
        height: 35px;
    }

    QDateEdit::drop-down {
        height: 35px;
        width: 30px;
    }

    QDateEdit::down-arrow {
        background: url("img/flecha-combo.png");
    }

    QCalendarWidget {
        font-size: 23px;
        background-color: transparent;
    }

    QCalendarWidget QAbstractItemView {
        background-color: #f0f0f0;
        selection-background-color: #4d90fe;
        selection-color: #ffffff;
        alternate-background-color: #e0e0e0;
        border: 2px solid #adb5bd;
        background-color: #ffffff;
    }

    QCalendarWidget QAbstractItemView:item {
        color: #333333;
    }

    /* Cambia el color de los días de sábado y domingo a rojo */
    QCalendarWidget QAbstractItemView:item[isWeekend="true"] {
        color: #ff0000; /* Color rojo */
    }

    QCalendarWidget QAbstractItemView:enabled {
        color: #000000;
    }

    QCalendarWidget QAbstractItemView:disabled {
        color: #808080;
    }

    QCalendarWidget QAbstractItemView:item:current-date {
        background-color: #FFFFFF;
        color: #000000;
    }

    QCalendarWidget QAbstractItemView:selected {
        background-color: #6f6f6f;
        color: #FFFFFF;
    }

    QCalendarWidget QAbstractItemView:item:hover {
        background-color: #e0e0e0;
    }

    QCalendarWidget QAbstractItemView:item:pressed {
        background-color: #b8b8b8;
        border: 4px solid #000000;
    }

    QCalendarWidget QHeaderView:section {
        background-color: transparent;
        font-weight: bold;
        border: none;
    }

    QCalendarWidget QHeaderView:section:Saturday,
    QCalendarWidget QHeaderView:section:Sunday {
        color: red;
    }

    QCalendarWidget QWidget#qt_calendar_navigationbar {
        background-color: #adb5bd;
        color: #FFFFFF;
        padding: 2px;
    }

    QCalendarWidget QWidget#qt_calendar_yearbutton,
    QCalendarWidget QWidget#qt_calendar_monthbutton {
        background-color: #adb5bd;
        color: white;
        border-radius: 4px;
        min-width: 20px;
        min-height: 20px;
        padding: 2px;
    }

    QCalendarWidget QWidget#qt_calendar_yearbutton:hover,
    QCalendarWidget QWidget#qt_calendar_monthbutton:hover {
        background-color: #e0e3e6;
        color: #000000;
        border: 2px solid #e0e3e6;
    }

    QCalendarWidget QToolButton {
        background-color: #adb5bd;
        color: white;
        border-radius: 4px;
        min-width: 20px;
        min-height: 20px;
        padding: 2px;
    }

    QCalendarWidget QToolButton:hover {
        background-color: #e0e3e6;
        color: #000000;
        border: 2px solid #e0e3e6;
    }

    QCalendarWidget QMenu {
        font-size: 20px;
        border: 4px solid #e0e3e6;
        background-color: #ffffff;
        color: #000000;
    }

    QCalendarWidget QMenu:hover {
        color: black;
        background-color: red;
    }

    QCalendarWidget QMenu::pressed {
        color: #ffffff;
        background-color: #6f6f6f;
    }

    QCalendarWidget QSpinBox {
        background-color: #e0e3e6;
        color: #000000;
        border: 2px solid #000000;
        border-radius: 4px;
        padding: 2px;
    }
"""
esttabla = """
    QTableWidget{
        background-color: #f5ebe0;
        color: black;
        gridline-color: black;
        font-size: 20px;
        font-family: "Segoe UI";
    }
    
    QTableWidget::item:selected {
        background-color: #d4a373;
        color: black;
    }
    QHeaderView{
        background-color: #9a9a9a;
        color: black;
        font-weight: bold;
        gridline-color: #000000;
        font-size: 17px;
    }
    QScrollBar:vertical {
        background-color: #808080; 
        width: 15px; 
    }
    """

estilo_boton = """
    QPushButton {
        background-color: #e85d04;
        color: white;
        border: 1px solid black;
        border-radius: 5px;
        padding: 5px 10px;
        font-weight: bold;
        font-size: 16px;
    }
    QPushButton:hover {
        background-color: #737272;
    }
    QPushButton:pressed {
        background-color: #be4e0c;
    }"""
boton_excel_icon = """
    QPushButton {
        background-color: #34b625;
        color: white;
        border: 2px solid black;
        border-radius: 5px;
        padding: 5px 10px;
        font-weight: bold;
        font-size: 16px;
    }
    QPushButton:hover {
        background-color: #6ca15f;
    }
    QPushButton:pressed {
        background-color: #0d730d;
    }"""
boton_excel = """
    QPushButton {
        background-color: #008000;
        color: white;
        border: 1px solid black;
        border-radius: 5px;
        padding: 5px 10px;
        font-weight: bold;
        font-size: 16px;
    }
    QPushButton:hover {
        background-color: #6ca15f;
    }
    QPushButton:pressed {
        background-color: #0d730d;
    }"""

estilo_menubar = """
    QMenuBar {
        background-color: #1a1a1a;
        color: white;
        font: 15px;
        font-weight: bold;
        border-bottom: 2px solid #808080;
    }
    QAction::item:selected {
        background-color: #333333; 
    }
    QAction::item:selected:disabled {
        background-color: #1a1a1a; 
    }   
    QAction:hover {
        background-color: #333333;
    }
"""
# ASISTENCIA
fondo_asistencia = """
    QMainWindow{
        background-image: url("img/asistencia.png");
        background-repeat: no-repeat;
    }"""

frame = """
    QFrame{
        background-color: rgba(242,242,242,0.45);
        border-radius: 10px; 
        padding: 20px;
    }
    """

label_logo = """
    QLabel{
        background-color: transparent;
    }"""    

estilo_texto = """
    QLabel{
        background-color: transparent;
        padding: 15px; 
        text-align: justify;
        font-size: 28px;
        font-family: "Segoe UI";
        color: white;
        font-weight: bold;
    }"""

label_fecha = """
    QLabel{
        background-color: transparent;
        font-size: 30px;
        width: 300px;
        padding: 0px;
        text-decoration: underline;
        text-align: left;
        font-family: "Segoe UI";
        font-weight: bold;            
        color: black;
    }"""
    
estiloFechaActual = """
    QLabel{
        background-color: transparent;
        font-size: 30px;
        padding: 0px;
        width: 150px;
        font-family: "Segoe UI";   
        color: black;
        text-align: left;
    }""" 

label_documento = """
    QLabel{
        background-color: transparent;
        font-size: 35px;
        padding: 0px;
        width: 200px;
        font-weight: bold;            
        font-family: "Segoe UI";
        color: black;
        text-align: left;
    }"""
    
estilo_lineedit = """
    QLineEdit{
        background-color: white;
        color: black;
        border: 1px solid black;
        border-radius: 4px;
        font-size: 20px;
        font-family: "Segoe UI";
        width:80px;
        height: 35px;
        }
    QLineEdit:hover{
        background-color: #adb5bd;
        }"""

boton = """
    QPushButton {
        background-color: #e85d04;
        color: white;
        border: 1px solid black;
        border-radius: 5px;
        font-weight: bold;
        font-size: 20px;
        width:50px;
        padding: 5px;
        text-align: center;
    }
    QPushButton:hover {
        background-color: #737272;
    }
    QPushButton:pressed {
        background-color: #be4e0c;
    }"""

textEdit = """
    QTextEdit {
        background-color: #fff9e0;
        color: #000;
        font-size: 14px;
        font-family: 'Courier New', monospace;
        padding: 10px;
        border: 1px solid #333333;
        border-radius: 5px;
    }
    QTextEdit:focus {
        border: 1px solid #4CAF50;
    }
"""
estilo_lista = """
    QListWidget {
        background-color: #333333;
        color: #f1f1f1;
        font-size: 14px;
        font-family: 'Courier New', monospace;
        padding: 10px;
        border-radius: 5px;
        outline: none;
    }
    QListWidget::item {
        padding: 5px 10px;
        border-radius: 5px;
    }
    QListWidget::item:hover {
        background-color: #444444;
    }
    QListWidget::item:selected {
        background-color: #4CAF50;
        color: #1f1f1f;
    }
"""