# QT ========================================
from PySide6.QtGui import QPainter,QColor
from PySide6.QtCore import Qt,QTimer,QRect
from PySide6.QtWidgets import QWidget
# Widget.Class ==============================
class QProgressBar(QWidget):
    def __init__(self,parent):
        super().__init__(parent=parent)
        self.__parent = parent
        self.setFixedSize(parent.width(), parent.height())
        self.setStyleSheet("background-color: rgba(1,1,1,1);")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing, True)
        painter.setBrush(Qt.white)
        _size = [
            328,
            38
        ]
        _offset = [
            0,
            self.height()//5.2
        ]
        _radius = _size[1]//2
        painter.drawRoundedRect(QRect(
            self.width()//2 - _size[0]//2 + _offset[0],
            self.height()//2 - _size[1]//2 + _offset[1],
            *_size
        ),_radius,_radius)
        painter.setBrush(QColor("#151515"))
        _size = [
            314,
            24
        ]
        _offset = [
            0,
            self.height()//5.19
        ]
        _radius = _size[1]//2
        painter.drawRoundedRect(QRect(
            self.width()//2 - _size[0]//2 + _offset[0],
            self.height()//2 - _size[1]//2 + _offset[1],
            *_size
        ),_radius,_radius)
class QProgressNail(QWidget):
    def __init__(self,parent):
        super().__init__(parent=parent)

        _size = [
            300,
            41
        ]
        _offset = [
            0,
            parent.height()//5.19
        ]
        _radius = _size[1]//2
        self.setFixedSize(*_size)
        self.move(
            parent.width()//2 - _size[0]//2 + _offset[0],
            parent.height()//2 - _size[1]//2 + _offset[1],
        )
        self.setStyleSheet(f"background-color: rgb(0,0,0); border-radius:{_radius}; padding: 2px;")

        # Bar Config
        self.percent = 0.5
        self.barpercent = (_size[0]*self.percent)-2
        _size = [
            150,
            12
        ]
        _offset = [
            1,0
        ]
        _radius = _size[1]//2
        self.bar = [
            self.width()//2 - _size[0]//2 + _offset[0],
            self.height()//2 - _size[1]//2 + _offset[1],
            _size[0],_size[1]
        ]
        self.barradius = _radius
        self.barangel = 90
        self.loops = 0
        self.adder = 1

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_bar)