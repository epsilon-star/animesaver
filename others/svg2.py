from PySide6 import *
from PySide6.QtGui import *
from PySide6.QtSvg import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *

class ClickableSvgWidget(QSvgWidget):
    def __init__(self, svg_file, on_click=None, parent=None):
        super().__init__(parent)
        self.on_click = on_click
        self.load(svg_file)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            if self.on_click: self.on_click()
        super().mousePressEvent(event)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Clickable SVG Example")

        # Set layout
        layout = QVBoxLayout(self)

        # Label to display a message
        self.message_label = QLabel("Click the SVG below!")
        layout.addWidget(self.message_label)

        # Create the clickable SVG widget
        # svg_widget = ClickableSvgWidget("icons/close.svg", on_click=self.svg_clicked)
        # svg_widget.setFixedSize(200, 200)  # Set size of the SVG widget
        scene = QWidget()
        svg_renderer = QSvgRenderer("icons/close.svg")
        svg_widget = QGraphicsSvgItem()
        layout.addWidget(scene)

        self.setLayout(layout)

    def svg_clicked(self):
        # This function is called when the SVG is clicked
        self.message_label.setText("SVG was clicked!")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
