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
        text-align: center;
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
        border-radius: 5px;
        font: 20px;
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
    }"""

estilo_lineedit = """
    QLineEdit{
        background-color: white;
        border: 1px solid black;
        border-radius: 4px;
        font-size: 15px;
        font-family: "Segoe UI";
    }
    QLineEdit:hover{
        background-color: #adb5bd;
    }"""

estilo_combo = """
        /* RECUADRO CON ITEMS*/
    QComboBox {
        background-color: #FFFFFF;
        color: #000000; 
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
        width: 25px;
        margin: 25.5px 0 25.5px 0;
        border-radius: 0px;
    }

    /* HANDLE BAR VERTICAL */
    QScrollBar::handle:vertical {    
        background-color: #ff8c00;
        border: 1px solid black;
    }
    QScrollBar::handle:vertical:hover {    
        background-color: rgba(255,140,0,0.5);
    }
    QScrollBar::handle:vertical:pressed {    
        background-color: #f6bd60;
    }

    /* BTN TOP - SCROLLBAR */
    QScrollBar::sub-line:vertical {
        border: 1px solid black;
        background: url("img/flecha-combo.png");
        height: 25px;
        subcontrol-position: top;
        subcontrol-origin: margin;
    }
    QScrollBar::sub-line:vertical:hover {    
        background-color: rgba(255,140,0,0.5);
    }
    QScrollBar::sub-line:vertical:pressed {    
        background-color: #f6bd60;
    }

    /* BTN BOTTOM - SCROLLBAR */
    QScrollBar::add-line:vertical {
        border: 1px solid black;
        background: url("img/flecha-combo.png");
        height: 25px;
        subcontrol-position: bottom;
        subcontrol-origin: margin;
    }
    QScrollBar::add-line:vertical:hover {    
        background-color: rgba(255,140,0,0.5);
    }
    QScrollBar::add-line:vertical:pressed {    
        background-color: #f6bd60;
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
estilo_fecha = """
    QDateEdit{
        background-color: #FFFFFF;
        color: #000000;
        border: 1px solid black;
        border-radius: 4px;
        font-size: 20px;
        height: 35px
        
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
        border: 2px solid #adb5bd;
        background-color: #ffffff; 
    }
    QCalendarWidget QAbstractItemView:enabled {
        color: #000000; 
    }

    QCalendarWidget QAbstractItemView:disabled {
        color: #808080; 
    }

    QCalendarWidget QAbstractItemView:selected {
        background-color: #d1e7b3;
        color: red;
    }
    
    QCalendarWidget QAbstractItemView:item:hover {
        background-color: #e0e0e0; 
    }

    QCalendarWidget QAbstractItemView:item:pressed {
        background-color: #b8b8b8;
        border: 4px solid #000000;
    }
    QCalendarWidget QHeaderView:section {
        background-color: green;
        font-weight: bold;
        border: none; 
    }

    QCalendarWidget QWidget#qt_calendar_navigationbar {
        background-color: #adb5bd; 
        color: #FFFFFF; 
        padding: 2px; 
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

    QCalendarWidget QMenu{ 
        font-size: 20px;
        border : 4px solid #e0e3e6;
        background-color: #ffffff; 
        color: #000000;
    }
    QCalendarWidget QMenu:hover {
        color: black;
        background-color: red;
    }
    QCalendarWidget QMenu::pressed{
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
    QHeaderView::section{
        background-color: #9a9a9a;
        color: black;
        font-weight: bold;
        font-size: 20px;
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
    QMenuBar::item:selected {
        background-color: #333333; 
    }
    QMenuBar::item:selected:disabled {
        background-color: #1a1a1a; 
    }   
    QAction {
        background-color: #1a1a1a;
        color: white;
        padding: 5px;
    }"""

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
        font-size: 25px;
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
        font-family: "Segoe UI";
        color: black;
        text-align: left;
    }"""

estilo_lineedit = """
    QLineEdit{
        background-color: white;
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
