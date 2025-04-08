from PySide6 import *
from PySide6.QtGui import *
from PySide6.QtSvg import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *

from widgets.qanimatetitle import QAnimateTitle
from widgets.qwindowsmenu import QWindowsMenu
from widgets.qtimedatebar import QTimeDateMenu

class FirstLoading(QWidget):
    def __init__(self,parent):
        super().__init__(parent=parent)
        self.setFixedSize(parent.width(), parent.height())

        self.__parent = parent

        # Bottom Icon Placeholder
        self.borders = BottomBorders(self)
        self.windows_menu = QWindowsMenu(self)
        self.date_menu = QTimeDateMenu(self)

        self.windows_menu.buttonClose.on_click = parent.close
        self.windows_menu.buttonMin.on_click = parent.showMinimized
        self.windows_menu.buttonMax.on_click = self.toggleFullscreen

        # fonts
        QFontDatabase.addApplicationFont("fonts/kontanter.otf")
        QFontDatabase.addApplicationFont("fonts/jetbrains.ttf")
        QFontDatabase.addApplicationFont("fonts/labora.ttf")
        QFontDatabase.addApplicationFont("fonts/vazir.ttf")

        # Texts
        _size = [
            self.width()//1.6,400
        ]
        self.animTitle = QAnimateTitle("ANiME SAVER",self)
        self.animTitle.setGeometry(
            self.width()//2 - _size[0]//2,
            self.height()//2 - _size[1]//2,
            *_size
        )
        _size_s = [
            800,200
        ]
        sb_wid = 9
        mps = 'S H A D O W t E A M'.split()
        sb_text = (" "*sb_wid).join(mps)
        self.title_sub = QLabel(parent=self,text=sb_text)
        self.title_sub.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_sub.setStyleSheet("font-family: Kontanter; font-size: 22px; background-color: rgba(0,0,0,0.0)")
        self.title_sub.setGeometry(
            self.width()//2 - _size_s[0]//2,
            self.height()//2 - _size_s[1]//2 + _size[1]//4.5,
            *_size_s
        )

    def toggleFullscreen(self):
        if self.__parent.isFullScreen():
            self.__parent.showNormal()
        else:
            self.__parent.showFullScreen()

class BottomBorders(QWidget):
    def __init__(self,parent):
        super().__init__(parent=parent)
        self.setFixedSize(parent.width(), parent.height())
        # print(parent.width(), parent.height())

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing, True)
        painter.setBrush(Qt.white)
        # borders
        painter.drawPolygon(
            [
                QPoint(0, self.height()//1.44),
                QPoint(+28, self.height()-21),
                QPoint(self.width()//4.35, self.height()),
                QPoint(0, self.height()),
            ]
        )
        painter.drawPolygon(
            [
                QPoint(self.width(), self.height()//1.44),
                QPoint(self.width()-28, self.height()-21),
                QPoint(self.width() - self.width()//4.35, self.height()),
                QPoint(self.width(), self.height()),
            ]
        )
        #centeral poly
        painter.drawPolygon(
            [
                QPoint(self.width()//2,self.height()//1.2),
                QPoint(self.width()//2+self.width()//8.5,self.height()),
                QPoint(self.width()//2-self.width()//8.5,self.height()),
            ]
        )
