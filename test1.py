from PySide6 import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *

app = QApplication([])  

# Create a main window  
window = QWidget()  
layout = QVBoxLayout()  

# Create a QLabel  
label = QLabel("This is a blurred background")  
label.setStyleSheet("background-color: rgba(255, 255, 255, 0.1);")  # Set a semi-transparent background  
label.setAlignment(Qt.AlignCenter)

# Create a blur effect  
blur_effect = QGraphicsBlurEffect()
blur_effect.setBlurRadius(30)  # Specify the blur radius  
label.setPixmap(QPixmap("images/backs.png"))
# Set the blur effect to the label  
label.setGraphicsEffect(blur_effect)  

# Add the label to the layout and set the layout on the window  
layout.addWidget(label)  
window.setLayout(layout)  
window.show()  

app.exec()