from PyQt6.QtGui import QColor

def itemColor_TOTAL(item_label):
    fuente = item_label.font()
    fuente.setBold(True)
    item_label.setBackground(QColor("#cdcdcd"))
    item_label.setForeground(QColor("#000000"))
    return fuente

def itemColor_RESULTADO(item_label):
    fuente = item_label.font()
    fuente.setBold(True)
    item_label.setBackground(QColor("#edaa7c"))
    item_label.setForeground(QColor("#000000"))
    return fuente