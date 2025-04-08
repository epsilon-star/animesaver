# QT ========================================
from PySide6.QtCore import Qt
from PySide6.QtSvgWidgets import QSvgWidget
# Widget.Class ==============================
class QDynamicSvg(QSvgWidget):
    def __init__(self, svg_file, on_click=None, parent=None):
        super().__init__(parent)
        self.on_click = on_click
        self.setStyleSheet("background-color: rgba(0,0,0,0.0);")
        self.load(svg_file)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            if self.on_click: self.on_click()
        super().mousePressEvent(event)