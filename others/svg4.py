# Modules
# ------------------------------------------------------------------------------
import sys
from PySide6 import *
from PySide6.QtGui import *
from PySide6.QtSvg import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *
from random import randint

# widget
# ------------------------------------------------------------------------------
class Example(QWidget):

    def __init__(self,):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        # formatting
        self.setGeometry(300, 300, 600, 300)
        self.setWindowTitle("Example")

        # widgets
        self.itemList = QTreeWidget()
        self.itemList.setItemsExpandable(True)
        self.itemList.setAnimated(True)
        self.itemList.setItemsExpandable(True)
        self.itemList.setColumnCount(2)
        self.itemList.setHeaderLabels(['', ''])

        # Load the svg
        renderer = QSvgRenderer('icons/close.svg')        
        # Prepare a QImage with desired characteritisc
        self.orig_svg = QImage(500, 500, QImage.Format_ARGB32) 
        # Get QPainter that paints to the image
        painter = QPainter(self.orig_svg)
        renderer.render(painter)

        # add items
        color0 = QColor( 255, 35, 35 )
        item0 = QTreeWidgetItem(self.itemList, ['testing', ''])
        item0.setIcon(1, self.icon_colored( color0 ))  # 1 - we set image for second colomn

        color1 = QColor( 32, 255, 35 )
        item1 = QTreeWidgetItem(self.itemList, ['testing', ''])
        item1.setIcon(1, self.icon_colored( color1 ) )  # 1 - we set image for second colomn


        pixmap = QPixmap.fromImage( self.orig_svg )
        self.lbl = QLabel(self)
        self.lbl.setPixmap(pixmap)

        self.button = QPushButton("rand color")

        self.button.clicked.connect( self.changeColor )

        # layout
        self.mainLayout = QVBoxLayout(self)
        self.mainLayout.addWidget(self.button)
        self.mainLayout.addWidget(self.itemList)
        self.mainLayout.addWidget(self.lbl)
        self.show()

    @Slot()
    def changeColor( self ):

        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)

        # Copy the image
        new_image = self.orig_svg.copy()

        # We are going to paint a plain color over the alpha
        paint = QPainter()
        paint.begin( new_image )
        paint.setCompositionMode( QPainter.CompositionMode_SourceIn )
        paint.fillRect( new_image.rect(), QColor( r, g, b ) )

        paint.end()

        self.lbl.setPixmap( QPixmap.fromImage(new_image) )

    def icon_colored( self, color ):

        # Copy the image
        new_image = self.orig_svg.copy()

        # We are going to paint a plain color over the alpha
        paint = QPainter()
        paint.begin( new_image )        
        paint.setCompositionMode( QPainter.CompositionMode_SourceIn )       
        paint.fillRect( new_image.rect(), color )        
        paint.end()

        return QIcon( QPixmap.fromImage( new_image ) )


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())