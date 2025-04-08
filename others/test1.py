from PySide6 import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
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

        # Progress Bar Placeholder
        self.progress_bar = ProgressBar()

        # Bottom Icon Placeholder
        self.bottom_icon = BottomIcon()

        # Add Widgets
        main_layout.addWidget(self.title_label)
        main_layout.addWidget(self.subtitle_label)
        main_layout.addSpacing(50)
        main_layout.addWidget(self.progress_bar)
        main_layout.addSpacing(50)
        main_layout.addWidget(self.bottom_icon)

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

# Progress Bar Class (Placeholder)
class ProgressBar(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300, 20)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(Qt.white)
        painter.drawRect(0, 0, self.width(), self.height())
        painter.setBrush(Qt.black)
        painter.drawRect(2, 2, self.width() - 4, self.height() - 4)

# Bottom Icon Class
class BottomIcon(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(100, 100)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(Qt.white)
        painter.drawPolygon(
            [
                QPoint(0, 0),
                QPoint(50, 50),
                QPoint(0, 50),
            ]
        )

# Application Execution
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
