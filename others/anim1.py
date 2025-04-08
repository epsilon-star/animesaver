from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPainter, QLinearGradient, QColor, QFont, QPainterPath

import os
import sys

def comp(value,min,max):
    output = value
    if value > min and value < max: output = value
    elif value > max: output = max
    elif value < min: output = min
    return output

class ShinyLabel(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setFixedSize(parent.width(),parent.height())
        self.setFont(QFont("Arial", 40, QFont.Bold))
        self.gradient_position = -0.1  # Start position of the shine effect

        # Timer to update the shine position
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_shine)
        self.timer.start(30)  # Adjust for speed

    def update_shine(self):
        self.gradient_position += 0.02  # Adjust for speed
        if self.gradient_position > 1.2:  # Reset position for infinite loop
            self.gradient_position = -0.1

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw text
        rect = self.rect()
        gradient = QLinearGradient(rect.left(), 0, rect.right(), 0)
        gradient.setColorAt(
            comp(max(self.gradient_position - 0.1, 0),0,1), QColor("#a0a0a0"))
        gradient.setColorAt(comp(self.gradient_position,0,1), QColor("#ffffff"))
        gradient.setColorAt(
            comp(max(self.gradient_position + 0.1, 0),0,1), QColor("#a0a0a0"))
        painter.setPen(Qt.NoPen)
        painter.setBrush(gradient)

        # Clip text for the gradient
        path = QPainterPath()
        path.addText(rect.center(), self.font(), self.text())
        painter.drawPath(path)

        painter.end()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Anime Saver Loading")
        self.setGeometry(200, 200, 800, 400)

        # Add shiny label
        self.label = ShinyLabel("ANIME SAVER", self)
        self.setCentralWidget(self.label)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
