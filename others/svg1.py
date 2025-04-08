from PySide6 import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *

# class ClickableSvgWidget(QSvgWidget):
#     def __init__(self, svg_file, on_click=None, parent=None):
#         super().__init__(parent)
#         self.on_click = on_click
#         self.load(svg_file)

#     def mousePressEvent(self, event):
#         if event.button() == Qt.MouseButton.LeftButton: 
#             if self.on_click: self.on_click()
#         super().mousePressEvent(event)

# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("SVG Example")
        
#         # Create a QVBoxLayout
#         layout = QVBoxLayout(self)

#         # Load SVG using QSvgWidget
#         svg_widget = ClickableSvgWidget("icons/windows.svg",parent=self,on_click=lambda : print("SVG CLICKED"))
#         svg_widget.setFixedSize(20, 20)  # Set widget size (scales the SVG to fit)
#         # layout.addWidget(svg_widget)

#         # Example QLabel with an SVG icon
#         label = QLabel("This is a label with an SVG icon:")
#         label.setPixmap(svg_widget.grab())  # Grab rendered SVG as pixmap for QLabel
#         layout.addWidget(label)

#         self.setLayout(layout)

# if __name__ == "__main__":
#     app = QApplication([])
#     window = MainWindow()
#     window.show()
#     app.exec()

from PySide6.QtCore import *
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap, QPainter
from PySide6.QtSvg import QSvgRenderer

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom SVG Example")

        layout = QVBoxLayout(self)

        # SVG Renderer
        svg_renderer = QSvgRenderer("icons/close.svg")

        # Create a QPixmap to render the SVG into
        pixmap = QPixmap(20, 20)  # Set the size of the rendered SVG
        pixmap.fill(Qt.transparent)  # Make background transparent

        # Use QPainter to apply transformations
        painter = QPainter(pixmap)

        # Scale the SVG
        painter.scale(1, 1)  # Scale by 1.5x

        # Apply rotation
        painter.rotate(0)  # Rotate 45 degrees

        # Apply color transformation
        painter.setPen(Qt.red)  # Set stroke color (if SVG uses strokes)
        painter.setBrush(Qt.green)  # Set fill color (if SVG uses fills)

        # Render the SVG
        svg_renderer.render(painter)
        painter.end()

        # Use the rendered QPixmap in a QLabel
        label = QLabel()
        label.setPixmap(pixmap)
        layout.addWidget(label)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
