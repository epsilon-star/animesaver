from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont, QPainter, QPen
import sys

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

        # Animated Progress Bar
        self.animated_progress_bar = AnimatedProgressBar()

        # Add Widgets
        main_layout.addWidget(self.title_label)
        main_layout.addWidget(self.subtitle_label)
        main_layout.addWidget(self.animated_progress_bar)

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

# Animated Progress Bar Class
class AnimatedProgressBar(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 20)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(16)  # ~60 FPS
        self.progress = 0

    def update_progress(self):
        self.progress += 2
        if self.progress > self.width():
            self.progress = 0
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw background
        pen = QPen(Qt.white, 1)
        painter.setPen(pen)
        painter.setBrush(Qt.black)
        painter.drawRect(0, 0, self.width(), self.height())

        # Draw progress
        painter.setBrush(Qt.white)
        painter.drawRect(0, 0, self.progress, self.height())

# Application Execution
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
