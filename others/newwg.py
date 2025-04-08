import sys
import os

from screeninfo import get_monitors as monitors

from PySide6 import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class borders(QLabel):
    def __init__(self,parent,geo):
        super().__init__(parent=parent) 
        self.__parent = parent
        self.__geo = geo

        # self.gpscene = QGraphicsScene(parent=self,sceneRect=QRectF(0,0,200,100))
        # self.gpview = QGraphicsView(self.gpscene,
        #     alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter
        # )
        # self.gpview.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        # self.gpview.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        # self.gpview.setBackgroundBrush(QPalette().base())

        # rect = self.gpscene.addRect(QRectF(QPointF(50, 25), QPointF(150, 75)))
        # rect.setBrush(QColor("blue"))

        self.painter = QPainter(self)
        self.pen = QPainterPath()
        self.pen.addRect(10,10,100,200)
        self.painter.drawPath(self.pen)

class ShapeWidget(QWidget):  
    def __init__(self):  
        super().__init__()  

    def paintEvent(self, event):  
        painter = QPainter(self)  
        path = QPainterPath()  
        path.addRect(10, 10, 100, 100)  # Adding a rectangle  
        painter.drawPath(path) 

class twindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # getting monitors
        self.Monitor = monitors()[0]

        # mainWindow Settings
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(self.Monitor.width,self.Monitor.height)
        self.move(self.Monitor.x,self.Monitor.y)

        self.geo = {
            "x":self.geometry().x(),
            "x":self.geometry().y(),
            "w":self.geometry().width(),
            "h":self.geometry().height(),
        }

        # self.borders = borders(self,{})
        # main wdiget and layout
        self.centeralwidget = QWidget(self)
        self.centeralwidget.setMouseTracking(False)
        self.centeralwidget.setTabletTracking(False)
        self.centeralwidget.setGeometry(
            QRect(0,0,
            self.geo['w'],
            self.geo['h'])
        )
        self.mainLayoutWidget = QWidget(self.centeralwidget)
        self.mainLayoutWidget.setGeometry(
            QRect(5,5,
            self.centeralwidget.geometry().width()-5*2,
            self.centeralwidget.geometry().height()-5*2)
        )

        self.scene = QGraphicsScene(self.centeralwidget)
        self.view = QGraphicsView(self.scene)
        self.view.setFixedSize(self.geo['w'],self.geo['h'])

        blue_brush = QBrush(Qt.GlobalColor.white)

        # self.rect = self.scene.addRect(50,50,100,100,brush=blue_brush)
        poly_point = [
            QPoint(-self.geo['w']//2,self.geo['h']//1.9),
            QPoint(-self.geo['w']//1.8,self.geo['h']//2),
            QPoint(-self.geo['w']//2,self.geo['h']//2)
        ]

        self.polys = QPolygon(poly_point)
        self.rect = self.scene.addPolygon(self.polys,brush=blue_brush)

        print(poly_point)
        self.setCentralWidget(self.centeralwidget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = twindow()
    window.show()

    sys.exit(app.exec())