# import sys  
# from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel  
# from PySide6.QtGui import QPixmap, QPainter, QColor  
# from PySide6.QtCore import Qt  

# class BlurBackground(QWidget):  
#     def __init__(self):  
#         super().__init__()  

#         self.setWindowFlags(Qt.FramelessWindowHint)  
#         self.setAttribute(Qt.WA_TranslucentBackground)  

#         layout = QVBoxLayout()  
#         label = QLabel("This is a blurred background window")  
#         layout.addWidget(label)  
#         self.setLayout(layout)  
        
#         self.pixmap = QPixmap("buttons.png")  # Load your background image  
        
#     def paintEvent(self, event):  
#         painter = QPainter(self)  
#         painter.setRenderHint(QPainter.Antialiasing)  
#         painter.setOpacity(1)  # Adjust transparency as needed  
#         painter.drawPixmap(0, 0, self.pixmap)  
#         painter.setCompositionMode(QPainter.CompositionMode_SourceIn)  
#         painter.fillRect(event.rect(), QColor(0, 0, 0, 150))  # Adjust color and opacity  
#         painter.end()  

# if __name__ == "__main__":  
#     app = QApplication(sys.argv)  
#     window = BlurBackground()  
#     window.resize(800, 600)  
#     window.show()  
#     sys.exit(app.exec())

from PyQt5 import QtCore, QtGui, QtWidgets


class BlurLabel(QtWidgets.QWidget):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.setAttribute(QtCore.Qt.WA_StyledBackground)
        widget = QtWidgets.QWidget()
        widget.setStyleSheet("""QWidget{ background:#fff; color:#000;}""")
        blur_effect = QtWidgets.QGraphicsBlurEffect(blurRadius=2)
        widget.setGraphicsEffect(blur_effect)

        self._label = QtWidgets.QLabel(
            text=text, alignment=QtCore.Qt.AlignCenter, parent=self
        )
        self.label.setStyleSheet(""" background-color : transparent; color : black""")
        self.label.setContentsMargins(10, 0, 10, 0)

        lay = QtWidgets.QVBoxLayout(self)
        lay.addWidget(widget)

    @property
    def label(self):
        return self._label

    def sizeHint(self):
        return self._label.sizeHint()

    def resizeEvent(self, event):
        self._label.resize(self.size())
        self._label.raise_()
        return super().resizeEvent(event)


class ButtonWidget(QtWidgets.QWidget):
    clicked = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.setStyleSheet("""background:#fff;""")

        vlay = QtWidgets.QVBoxLayout(self)

        group = QtWidgets.QButtonGroup(self)
        group.buttonClicked[int].connect(self.clicked)

        for i in range(3):
            radiobutton = QtWidgets.QRadioButton(str(i))
            radiobutton.setStyleSheet("""background:#000; color:#fff;""")
            group.addButton(radiobutton, i)
            vlay.addWidget(radiobutton)


class LabelWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.setStyleSheet("""background:#fff;""")

        vlay = QtWidgets.QVBoxLayout(self)

        label = QtWidgets.QLabel("text, text, text, text")
        label.setStyleSheet("""background:#000; color:#fff;""")
        vlay.addWidget(label)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        container = QtWidgets.QWidget()
        container.setStyleSheet("""QWidget{ background:#000;}""")

        hlay_menus = QtWidgets.QHBoxLayout()
        hlay_menus.setContentsMargins(0, 6, 0, 6)

        self.menus = []

        for i in range(3):
            menu = BlurLabel("menu-{}".format(i))
            hlay_menus.addWidget(menu)
            self.menus.append(menu)

        self.button_widget = ButtonWidget()
        self.button_widget.clicked.connect(self.onClicked)
        self.label_widget = LabelWidget()

        lay = QtWidgets.QHBoxLayout(container)
        lay.addLayout(hlay_menus)
        lay.addWidget(self.button_widget)
        lay.addWidget(self.label_widget)
        container.setFixedSize(container.sizeHint())

        hlay = QtWidgets.QHBoxLayout()
        hlay.addStretch(0)
        hlay.addWidget(container)
        hlay.addStretch(0)

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        vlay = QtWidgets.QVBoxLayout(central_widget)
        vlay.addStretch(0)
        vlay.addLayout(hlay)
        vlay.addStretch(0)

        self.last_id = -1

    @QtCore.pyqtSlot(int)
    def onClicked(self, id_):
        menu = self.menus[id_]
        if not hasattr(menu, "animation"):
            animation = QtCore.QPropertyAnimation(menu, b"pos", duration=1000)
            animation.setStartValue(menu.pos())
            animation.setEndValue(
                QtCore.QPoint(self.label_widget.pos().x() + 5, menu.pos().y())
            )
            animation.start()
            menu.animation = animation

        if self.last_id != -1:
            last_menu = self.menus[self.last_id]
            last_menu.animation.setDirection(QtCore.QAbstractAnimation.Backward)
            last_menu.animation.start()
            last_menu.raise_()
        menu.animation.setDirection(QtCore.QAbstractAnimation.Forward)
        menu.animation.start()
        menu.raise_()
        self.button_widget.raise_()
        self.last_id = id_


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    w = MainWindow()
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())