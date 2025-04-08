from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt, QTimer, QPointF
from PySide6.QtGui import QFont, QPainter, QPixmap, QPen
import sys
import math

# Main Window Class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Anime Saver")
        self.setFixedSize(800, 600)
        self.setStyleSheet("background-color: black;")

        # Central Widget
        self.central_widget = CentralWidget()
        self.setCentralWidget(self.central_widget)

# Central Widget Class
class CentralWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Layouts
        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignCenter)

        # Title Label
        self.title_label = TitleLabel("ANIME SAVER")
        self.subtitle_label = SubtitleLabel("SHADOW TEAM")

        # Animated Shape
        self.animated_shape = AnimatedShape()

        # Add Widgets
        main_layout.addWidget(self.title_label)
        main_layout.addWidget(self.subtitle_label)
        main_layout.addWidget(self.animated_shape)

# Title Label Class
class TitleLabel(QLabel):
    def __init__(self, text):
        super().__init__(text)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("color: white;")
        self.setFont(QFont("Arial", 30, QFont.Bold))

# Subtitle Label Class
class SubtitleLabel(QLabel):
    def __init__(self, text):
        super().__init__(text)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("color: white;")
        self.setFont(QFont("Arial", 15, QFont.Bold))

# Animated Shape Class
class AnimatedShape(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 200)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_position)
        self.timer.start(8)  # ~60 FPS
        self.x = 0
        self.y = self.height() // 2
        self.angle = 0

    def update_position(self):
        self.x += 5
        self.angle += 0.1
        self.y = self.height() // 2 + int(50 * math.sin(self.angle))

        if self.x > self.width():
            self.x = 0

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        pen = QPen(Qt.white, 3)
        painter.setPen(pen)
        painter.setBrush(Qt.white)

        painter.drawEllipse(QPointF(self.x, self.y), 10, 10)

# Application Execution
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
