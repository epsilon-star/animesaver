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

from pages.firstloading import FirstLoading
# from pages.login import LoginPage

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
        # self.central_widget = LoginPage(self)
        self.central_widget = FirstLoading(self)
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