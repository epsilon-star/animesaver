from PySide6 import *
from PySide6.QtGui import *
from PySide6.QtSvg import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *
import sys
import os
import time

import screeninfo
from math import sin

def gettime():
    ts = time.localtime()
    return f"{ts.tm_year:04d}/{ts.tm_mon:02d}/{ts.tm_mday:02d} | {ts.tm_hour:02d}:{ts.tm_min:02d}"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Anime Saver")
        self.setWindowFlags(Qt.FramelessWindowHint)
        _pos = [
            screeninfo.get_monitors()[0].x,
            screeninfo.get_monitors()[0].y
        ]
        self.move(*_pos)
        self.setFixedSize(1920, 1080)
        # self.setFixedSize(1600, 900)
        self.setStyleSheet("background-color: #121212;")

        # Central Widget
        self.central_widget = CentralWidget(self)
        self.setCentralWidget(self.central_widget)

class CentralWidget(QWidget):
    def __init__(self,parent):
        super().__init__(parent=parent)
        self.setFixedSize(parent.width(), parent.height())

        # Layouts
        # main_layout = QVBoxLayout(self)
        # main_layout.setAlignment(Qt.AlignCenter)

        # Title Label
        # self.title_label = TitleLabel("ANIME SAVER")
        # self.subtitle_label = SubtitleLabel("SHADOW TEAM")

        # Progress Bar Placeholder
        # self.progress_bar = ProgressBar()

        # Bottom Icon Placeholder
        self.bottom_icon = BottomBorders(self)
        self.windows_menu = WindowsMenu(self)
        self.date_menu = QTimeDateMenu(self)

        self.windows_menu.svgClose.on_click = parent.close
        self.windows_menu.svgMin.on_click = parent.showMinimized
        # self.progress_bar = ProgressBar(self)
        # self.progress_nail = ProgressNail(self)

        # Texts
        QFontDatabase.addApplicationFont("kontanter.otf")
        QFontDatabase.addApplicationFont("jetbrains.ttf")
        _size = [
            self.width()//1.6,400
        ]
        self.animTitle = AnimateTitle("ANiME SAVER",self)
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

class ProgressBar(QWidget):
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

class ProgressNail(QWidget):
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
        # self.timer.start(8) # ~60 FPS

    def update_bar(self):
        # simple fill
        # self.bar[2] += 0.2
        # if self.bar[2] >= self.width()-2:
        #     self.bar[2] = 0
        self.barangel += self.adder
        if self.barangel >= 360: self.barangel,self.loops = 0,1
        elif self.loops == 1 and self.barangel >= 90: self.timer.stop()
        elif self.loops == 1 and self.barangel > 75: self.adder = abs((90-self.barpercent)/100)

        self.bar[0] += sin(self.barangel*0.0174533)*self.adder

        os.system("cls")
        print(f"angle[{self.barangel}] loops[{self.loops}] adder[{self.adder}]")

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing, True)
        painter.setBrush(Qt.GlobalColor.white)
        # self.nail = painter.drawRoundedRect(QRect(
        #     # self.width()//2 - _size[0]//2 + _offset[0],
        #     0 + _offset[0],
        #     self.height()//2 - _size[1]//2 + _offset[1],
        #     self.barpercent,_size[1]
        # ),_radius,_radius)
        self.nail = painter.drawRoundedRect(QRect(
            *self.bar
        ),self.barradius,self.barradius)

class BottomBorders(QWidget):
    def __init__(self,parent):
        super().__init__(parent=parent)
        self.setFixedSize(parent.width(), parent.height())

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

def comp(value,min,max):
    output = value
    if value > min and value < max: output = value
    elif value > max: output = max
    elif value < min: output = min
    return output

class AnimateTitle(QLabel):
    def __init__(self,text,parent=None):
        super().__init__(text,parent=parent)

        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("font-family: Kontanter; font-size: 100px; background-color: rgba(0,0,0,0.0)")

        self.nailPos = -0.1
        self.nailWidth = 0.1
        self.nailSpeed = 0.005

        self.nailColor = "#fff"
        self.nailColors = [
            # "#ffc400",
            "#ffffff",
            "#6dccff",
            # "#1c33ff",
            # "#3cff00",
            "#ff9e62",
            "#bd72ff",
        ]
        self.nailCIndex = 0
        self.textColor = "#a0a0a0"

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_shine)
        self.timer.start(16)

    def update_shine(self):
        self.nailPos += self.nailSpeed  # Adjust for speed
        if self.nailPos > 1.1:  # Reset position for infinite loop
            self.nailCIndex +=1
            if self.nailCIndex == len(self.nailColors): self.nailCIndex = 0
            self.nailPos = -0.1
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        rect = self.rect()
        gradient = QLinearGradient(rect.left(), rect.top(), rect.right(), rect.bottom())
        gradient.setColorAt(comp(max(self.nailPos - self.nailWidth, 0),0,1), QColor(self.textColor))
        gradient.setColorAt(comp(self.nailPos,0,1), QColor(self.nailColors[self.nailCIndex]))
        gradient.setColorAt(comp(max(self.nailPos + self.nailWidth, 0),0,1), QColor(self.textColor))
        gradient_pen = QLinearGradient(rect.left(), rect.top(), rect.right(), rect.bottom())
        gradient_pen.setColorAt(comp(max(self.nailPos - self.nailWidth, 0),0,1), QColor(self.textColor))
        gradient_pen.setColorAt(comp(self.nailPos,0,1), QColor(self.nailColor))
        gradient_pen.setColorAt(comp(max(self.nailPos + self.nailWidth, 0),0,1), QColor(self.textColor))

        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(gradient)
        # painter.setBrush(QColor(self.textColor))

        path = QPainterPath()
        textWidth = self.fontMetrics().boundingRect(self.text()).width()
        textHeight = self.fontMetrics().boundingRect(self.text()).height()
        path.addText(QPoint(self.width()//2 - (textWidth)//2,self.height()//2 + textHeight//2), self.font(), self.text())
        painter.drawPath(path)

        painter.end()

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

# class QDynamicSvg(QWidget):
#     def __init__(self,filename,parent=None):
#         super().__init__(parent)

#         self.geo = {
#             "w":20,
#             "h":20,
#             "x":0,
#             "y":0
#         }

#         # self.setGeometry(
#         #     *list(self.geo.values())
#         # )

#         self.renderer = QSvgRenderer(filename)
#         self.origin = QImage(self.geo['w'],self.geo['h'],QImage.Format.Format_ARGB32)
#         self.painter = QPainter(self.origin)
#         self.renderer.render(self.painter)

#         image = self.origin.copy()
#         painter = QPainter(image)
#         painter.setCompositionMode( QPainter.CompositionMode.CompositionMode_SourceIn )
#         painter.fillRect( self.origin.rect(), QColor("black"))
#         painter.end()
#         self.pixmap = QPixmap.fromImage(image)
#         self.btn = QPushButton(self)
#         self.btn.setStyleSheet("""
#             QPushButton {
#                 background-color: #00000000;
#                 border: 0px solid white;
#             }
#             QPushButton:hover {
#                 background-color: #00000000;
#                 border: 0px solid white;
#             }
#         """)
#         self.btn.setIcon(QIcon(self.pixmap))

class WindowsMenu(QWidget):
    def __init__(self,parent):
        super().__init__(parent=parent)
        # self.setFixedSize(300,80)
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
        self.svgClose = QDynamicSvg("icons/close.svg",parent=self)
        self.svgClose.setGeometry(
            self.width()//2 - _size[0]//2 + _offset[0],
            self.height()//2 - _size[1]//2,
            *_size
        )
        _size = [
            15,15
        ]
        self.svgMax = QDynamicSvg("icons/solid.svg",parent=self)
        self.svgMax.setGeometry(
            self.width()//2 - _size[0]//2,
            self.height()//2 - _size[1]//2,
            *_size
        )
        _size = [
            15,15
        ]
        self.svgMin = QDynamicSvg("icons/solid_border.svg",parent=self)
        self.svgMin.setStyleSheet("background-color: rgba(0,0,0,0.0);")
        self.svgMin.setGeometry(
            self.width()//2 - _size[0]//2 - _offset[0],
            self.height()//2 - _size[1]//2,
            *_size
        )
        # _icon = QIcon("icons/close.svg")
        # _icon.
        # self.btn_close = QPushButton(parent=parent)
        # self.btn_close.setIcon()
        # self.btn_close.setStyleSheet("""
        #         QPushButton {
        #             background-color: none;
        #             border: 2px solid rgba(0,0,0,0.0);
        #             border-radius: 15px;
        #             color: white;
        #             font-size: 10px;
        #         }
        #         QPushButton:hover {
        #             border-color: #000000;
        #         }
        #     """)
        # self.btn_close.setGeometry(80,80,*_size)

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
        self.date = QLabel(gettime(),parent=self)
        self.date.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.date.setStyleSheet("background-color: rgba(0,0,0,0.0); color: black; font-family: 'JetBrains Mono NL'; font-size: 15px;")

        self.datetimer = QTimer()
        self.datetimer.timeout.connect(self.updateDate)
        self.datetimer.start(10000)

    def updateDate(self):
        self.date.setText(gettime())

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
       

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())