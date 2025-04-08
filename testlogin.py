from PySide6 import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
import sys
import os
import time

import screeninfo

from widgets.qanimatetitle import QAnimateTitle
from widgets.qwindowsmenu import QWindowsMenu
from widgets.qtimedatebar import QTimeDateMenu

class CustomLabel(QLabel):
    def __init__(self,parent,text,geos):
        super().__init__(parent=parent,text=text)

        self.setStyleSheet(f"background-color: white; color: black; border-radius: {geos[1]//2}px; font-family: Labora; font-size: 50px;")
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setFixedSize(*geos)

class CustomButton(QPushButton):
    def __init__(self,parent,text,geos):
        super().__init__(parent=parent,text=text)

        formater = f"border-radius: {geos[1]//2}px;"
        stylesheet = "QPushButton {background-color: white; color: black;  font-family: Labora; font-size: 28px;"
        stylesheet += formater 
        stylesheet += "border: none;} QPushButton::hover {background-color: black; color: white;}"

        self.setStyleSheet(stylesheet)
        # self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setFixedSize(*geos)

class CustomEntry(QLineEdit):
    def __init__(self,parent,text,geos):
        super().__init__(parent=parent)

        formater = f"border-radius: {geos[1]//2}px;"
        stylesheet = "QLineEdit {background-color: white; color: black;  font-family: Labora; font-size: 30px;"
        stylesheet += formater
        stylesheet += "border: none; padding: 0px 10px;}"

        self.setStyleSheet(stylesheet)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setPlaceholderText(text)
        self.setFixedSize(*geos)

class QRememberMe(QPushButton):
    def __init__(self,parent,text,geos):
        super().__init__(parent=parent,text=text)

        formater = f"border-radius: {geos[1]//2}px;"
        stylesheet = "QPushButton {background-color: none; color: white;  font-family: Labora; font-size: 30px;"
        stylesheet += formater
        stylesheet += "border: 1px solid white;} QPushButton::hover {background-color: white; color: black;}"

        self.setStyleSheet(stylesheet)
        # self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # self.setPlaceholderText(text)
        self.setFixedSize(*geos)

class LoginDialog(QWidget):
    def __init__(self,parent):
        super().__init__(parent=parent)
        # self.setFixedSize(parent.width(),parent.height())
        self.setStyleSheet("background-color: rgba(0,0,0,0.0)")
        _size = [
            1000,
            1000
        ]
        self.setGeometry(
            parent.width()//1.31 - _size[0]//2,
            parent.height()//1.95 - _size[1]//2,
            *_size
        )

        self.backpattern = QLabel(parent=self)
        pixmap = QPixmap("images/panel-back.png")
        self.backpattern.setPixmap(pixmap)
        self.backpattern.setScaledContents(True)
        _size = [
            1000,1000
        ]
        self.backpattern.setGeometry(
            self.width()//2 - _size[0]//2,
            self.height()//2 - _size[1]//2,
            *_size
        )

        _size = [
            230,
            55
        ]
        self.pageTitle = CustomLabel(self,'LOGIN',_size)
        self.pageTitle.setGeometry(
            self.width()//2 - _size[0]//2,
            self.height()//4.75 - _size[1]//2,
            *_size
        )

        self.backbutton = QLabel(parent=self)
        self.backbutton.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap("images/buttons.png")
        self.backbutton.setPixmap(pixmap)
        self.backbutton.setScaledContents(True)
        _size = [
            321,114
        ]
        self.backbutton.setGeometry(
            self.width()//2 - _size[0]//2,
            self.height()//1.22 - _size[1]//2,
            *_size
        )

        _size = [
            140,
            57
        ]
        self.btnLogin = CustomButton(self,"LOGIN",_size)
        self.btnLogin.setGeometry(
            self.width()//2.45 - _size[0]//2,
            self.height()//1.265 - _size[1]//2,
            *_size
        )
        _size = [
            180,
            57
        ]
        self.btnRegister = CustomButton(self,"REGISTER",_size)
        self.btnRegister.setGeometry(
            self.width()//1.7 - _size[0]//2,
            self.height()//1.265 - _size[1]//2,
            *_size
        )
        _size = [
            170,
            57
        ]
        self.btnCancel = CustomButton(self,"CANCEL",_size)
        self.btnCancel.setGeometry(
            self.width()//2 - _size[0]//2,
            self.height()//1.18 - _size[1]//2,
            *_size
        )

        _size = [
            320,
            60
        ]
        self.entryUsername = CustomEntry(self,"USERNAME",_size)
        self.entryUsername.setGeometry(
            self.width()//2 - _size[0]//2,
            self.height()//2.4 - _size[1]//2,
            *_size
        )
        _size = [
            320,
            60
        ]
        self.entryPassword = CustomEntry(self,"PASSWORD",_size)
        self.entryPassword.setGeometry(
            self.width()//2 - _size[0]//2,
            self.height()//2 - _size[1]//2,
            *_size
        )

        _size = [
            320,
            60
        ]
        self.checkremer = QRememberMe(self,"REMEMBER ME",_size)
        self.checkremer.setGeometry(
            self.width()//2 - _size[0]//2,
            self.height()//1.7 - _size[1]//2,
            *_size
        )

    # def paintEvent(self, event):
    #     painter = QPainter(self)
    #     painter.setRenderHints(QPainter.Antialiasing, True)
    #     painter.setPen(Qt.PenStyle.NoPen)
    #     painter.setBrush(QColor("rgba(0,0,0,0.0)"))
    #     _size = [
    #         400,
    #         600
    #     ]
    #     _radius = 20
    #     painter.drawRoundedRect(
    #         QRect(
    #            self.width()//2 - _size[0]//2,
    #            self.height()//2 - _size[1]//2,
    #            *_size
    #         ),
    #         _radius,_radius
    #     )
        

class LoginPage(QWidget):
    def __init__(self,parent):
        super().__init__(parent=parent)
        self.setFixedSize(parent.width(), parent.height())

        self.__parent = parent

        # Bottom Icon Placeholder
        self.borders = WindowShapes(self)
        self.windows_menu = QWindowsMenu(self)
        self.date_menu = QTimeDateMenu(self)

        self.login_dialog = LoginDialog(self)

        self.windows_menu.buttonClose.on_click = parent.close
        self.windows_menu.buttonMin.on_click = parent.showMinimized
        self.windows_menu.buttonMax.on_click = self.toggleFullscreen

        # fonts
        QFontDatabase.addApplicationFont("fonts/kontanter.otf")
        QFontDatabase.addApplicationFont("fonts/jetbrains.ttf")
        QFontDatabase.addApplicationFont("fonts/labora.ttf")
        QFontDatabase.addApplicationFont("fonts/vazir.ttf")

        # Texts
        # _size = [
        #     self.width()//1.6,400
        # ]
        # self.animTitle = QAnimateTitle("ANiME SAVER",self)
        # self.animTitle.setGeometry(
        #     self.width()//2 - _size[0]//2,
        #     self.height()//2 - _size[1]//2,
        #     *_size
        # )
        # _size_s = [
        #     800,200
        # ]
        # sb_wid = 9
        # mps = 'S H A D O W t E A M'.split()
        # sb_text = (" "*sb_wid).join(mps)
        # self.title_sub = QLabel(parent=self,text=sb_text)
        # self.title_sub.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # self.title_sub.setStyleSheet("font-family: Kontanter; font-size: 22px; background-color: rgba(0,0,0,0.0)")
        # self.title_sub.setGeometry(
        #     self.width()//2 - _size_s[0]//2,
        #     self.height()//2 - _size_s[1]//2 + _size[1]//4.5,
        #     *_size_s
        # )

    def toggleFullscreen(self):
        if self.__parent.isFullScreen():
            self.__parent.showNormal()
        else:
            self.__parent.showFullScreen()

class WindowShapes(QWidget):
    def __init__(self,parent):
        super().__init__(parent=parent)
        self.setFixedSize(parent.width(), parent.height())
        # print(parent.width(), parent.height())

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing, True)
        painter.setBrush(Qt.GlobalColor.white)
        _size = 130
        painter.drawEllipse(QPoint(
            self.width()//2.46 - _size//2,
            self.height()//1.165 - _size//2
        ),_size,_size)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(Qt.GlobalColor.black)
        _size = 570
        painter.drawEllipse(QPoint(
            self.width()//2.55 - _size//2,
            self.height()//2.65 - _size//2
        ),_size,_size)
        _size = 240
        painter.drawEllipse(QPoint(
            self.width()//5.05 - _size,
            self.height()//0.92 - _size
        ),_size,_size)
        painter.end()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setWindowTitle("Anime Saver")
        self.setWindowFlags(Qt.FramelessWindowHint)
        _pos = [
            screeninfo.get_monitors()[0].x,
            screeninfo.get_monitors()[0].y
        ]
        self.move(*_pos)
        self.setFixedSize(1920, 1080)
        # self.setFixedSize(1600, 900)
        self.setStyleSheet("background-color: #121212;")
        self.showFullScreen()

        # Central Widget
        self.central_widget = LoginPage(self)
        self.setCentralWidget(self.central_widget)

        self.mouse_offset = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            winX, winY = event.position().x(), event.position().y()
            if 0 < winX < self.width() // 3 and 0 < winY < 30:  # Check if the mouse is in the draggable area
                self.mouse_offset = event.globalPosition() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, event):
        if self.mouse_offset and self.isFullScreen() == False:
            new_position = event.globalPosition() - self.mouse_offset
            self.move(int(new_position.x()), int(new_position.y()))

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_offset = None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())