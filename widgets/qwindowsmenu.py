# QT ========================================
from PySide6.QtGui import QPainter
from PySide6.QtCore import QRect,Qt
from PySide6.QtWidgets import QWidget
# Shadow.QT =================================
from widgets.qdynamicsvg import QDynamicSvg
# Widget.Class ==============================
class QWindowsMenu(QWidget):
    def __init__(self,parent):
        super().__init__(parent=parent)
        _size = [
            100,30
        ]
        _offset = [
            0,10
        ]
        self.setGeometry(
            parent.width()//2 - _size[0]//2 + _offset[0],
            0 + _offset[1],
            *_size
        )
        _size = [
            13,13
        ]
        _offset = [
            25,20
        ]
        self.buttonClose = QDynamicSvg("icons/close.svg",parent=self)
        self.buttonClose.setGeometry(
            self.width()//2 - _size[0]//2 + _offset[0],
            self.height()//2 - _size[1]//2,
            *_size
        )
        _size = [
            15,15
        ]
        self.buttonMax = QDynamicSvg("icons/solid.svg",parent=self)
        self.buttonMax.setGeometry(
            self.width()//2 - _size[0]//2,
            self.height()//2 - _size[1]//2,
            *_size
        )
        _size = [
            15,15
        ]
        self.buttonMin = QDynamicSvg("icons/solid_border.svg",parent=self)
        self.buttonMin.setStyleSheet("background-color: rgba(0,0,0,0.0);")
        self.buttonMin.setGeometry(
            self.width()//2 - _size[0]//2 - _offset[0],
            self.height()//2 - _size[1]//2,
            *_size
        )

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing, True)
        painter.setBrush(Qt.white)
        # borders
        _size = [
            95,29
        ]
        _radius = _size[-1]//2
        painter.drawRoundedRect(
            QRect(
                self.width()//2 - _size[0]//2,
                self.height()//2 - _size[1]//2,
                *_size
            ),_radius,_radius
        )
        painter.end()