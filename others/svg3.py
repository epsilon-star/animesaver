import sys
from PySide6 import *
from PySide6.QtGui import *
from PySide6.QtSvg import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *

# class QDynamicSvg(QLabel):
#     def __init__(self,parent=None):
#         super().__init__(parent=parent)

#         self.renderer = QSvgRenderer("icons/close.svg")
#         self.origin = QImage(50,50,QImage.Format.Format_ARGB32)
#         self.painter = QPainter(self.origin)
#         self.renderer.render(self.painter)

#         self.pix = QPixmap.fromImage(self.origin)
#         self.pixmap = self.pix

class QDynamicSvg(QWidget):
    def __init__(self,filename,parent=None):
        super().__init__(parent)

        self.renderer = QSvgRenderer(filename)
        self.origin = QImage(50,50,QImage.Format.Format_ARGB32)
        self.painter = QPainter(self.origin)
        self.renderer.render(self.painter)

        image = self.origin.copy()
        painter = QPainter(image)
        painter.setCompositionMode( QPainter.CompositionMode.CompositionMode_SourceIn )
        painter.fillRect( self.origin.rect(), QColor("white"))
        painter.end()
        self.pixmap = QPixmap.fromImage(image)
        self.btn = QPushButton(self)
        self.btn.setIcon(QIcon(self.pixmap))

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(600,600)

        # renderer = QSvgRenderer('icons/solid.svg')
        # self.orig_svg = QImage(200, 200, QImage.Format.Format_ARGB32)
        # painter = QPainter(self.orig_svg)
        # renderer.render(painter)

        # new_image = self.orig_svg.copy()
        # paint = QPainter()
        # paint.begin( new_image )        
        # paint.setCompositionMode( QPainter.CompositionMode_SourceIn )       
        # paint.fillRect( new_image.rect(), QColor("white") )
        # paint.end()

        # self.pixmap = QPixmap.fromImage( new_image )
        # # self.lbl = QLabel(self)
        # # self.lbl.setPixmap(self.pixmap)
        # # self.lbl.mousePressEvent
        # icon = QIcon(self.pixmap)
        # mps = QPushButton(parent=self)
        # mps.setIcon(icon)

        self.btns = QDynamicSvg("icons/solid.svg",self)

        # mps = QSvgWidget(self)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())