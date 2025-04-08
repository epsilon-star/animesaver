# Built-IN ==================================
import time
# QT ========================================
from PySide6.QtGui import QPainter
from PySide6.QtCore import Qt,QTimer,QRect
from PySide6.QtWidgets import QWidget,QLabel
# Widget.Class ==============================
class QTimeDateMenu(QWidget):
    def __init__(self,parent):
        super().__init__(parent=parent)
        # self.setFixedSize(300,80)
        _size = [
            190,80
        ]
        _offset = [
            5,
            -15   
        ]
        self.setGeometry(
            parent.width() - _size[0] - _offset[0],
            0 + _offset[1],
            *_size
        )
        self.date = QLabel(self.gettime(),parent=self)
        self.date.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.date.setStyleSheet("background-color: rgba(0,0,0,0.0); color: black; font-family: 'JetBrains Mono NL'; font-size: 15px;")

        self.datetimer = QTimer()
        self.datetimer.timeout.connect(self.updateDate)
        self.datetimer.start(10000)

    def gettime(self):
        ts = time.localtime()
        return f"{ts.tm_year:04d}/{ts.tm_mon:02d}/{ts.tm_mday:02d} | {ts.tm_hour:02d}:{ts.tm_min:02d}"

    def updateDate(self):
        self.date.setText(self.gettime())

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing, True)
        painter.setBrush(Qt.white)
        # borders
        _size = [
            180,29
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
        _offset = [
            -25,
            -3 
        ]
        _size = [
            self.date.fontMetrics().boundingRect(self.date.text()).width(),
            self.date.fontMetrics().boundingRect(self.date.text()).height()
        ]
        self.date.setGeometry(
            self.width()//2 - _size[0]//2 + _offset[0],
            self.height()//2 - _size[1]//2 + _offset[1],
            210,30
        )