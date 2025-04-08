# QT ========================================
from PySide6.QtGui import QPainter,QPainterPath,QLinearGradient,QColor
from PySide6.QtCore import Qt,QTimer,QPoint
from PySide6.QtWidgets import QLabel
# Shadow.Tools ==============================
from tools.comp import comp
# Widget.Class ==============================
class QAnimateTitle(QLabel):
    def __init__(self,text,parent=None):
        super().__init__(text,parent=parent)

        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("font-family: Kontanter; font-size: 100px; background-color: rgba(0,0,0,0.0)")

        self.nailPos = -0.1
        self.nailWidth = 0.1
        self.nailSpeed = 0.005

        self.nailColor = "#fff"
        self.nailColors = [
            # "#ffc400",
            "#ffffff",
            "#6dccff",
            # "#1c33ff",
            # "#3cff00",
            "#ff9e62",
            "#bd72ff",
        ]
        self.nailCIndex = 0
        self.textColor = "#a0a0a0"

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_shine)
        self.timer.start(16)

    def update_shine(self):
        self.nailPos += self.nailSpeed  # Adjust for speed
        if self.nailPos > 1.1:  # Reset position for infinite loop
            self.nailCIndex +=1
            if self.nailCIndex == len(self.nailColors): self.nailCIndex = 0
            self.nailPos = -0.1
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        rect = self.rect()
        gradient = QLinearGradient(rect.left(), rect.top(), rect.right(), rect.bottom())
        gradient.setColorAt(comp(max(self.nailPos - self.nailWidth, 0),0,1), QColor(self.textColor))
        gradient.setColorAt(comp(self.nailPos,0,1), QColor(self.nailColors[self.nailCIndex]))
        gradient.setColorAt(comp(max(self.nailPos + self.nailWidth, 0),0,1), QColor(self.textColor))
        gradient_pen = QLinearGradient(rect.left(), rect.top(), rect.right(), rect.bottom())
        gradient_pen.setColorAt(comp(max(self.nailPos - self.nailWidth, 0),0,1), QColor(self.textColor))
        gradient_pen.setColorAt(comp(self.nailPos,0,1), QColor(self.nailColor))
        gradient_pen.setColorAt(comp(max(self.nailPos + self.nailWidth, 0),0,1), QColor(self.textColor))

        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(gradient)
        # painter.setBrush(QColor(self.textColor))

        path = QPainterPath()
        textWidth = self.fontMetrics().boundingRect(self.text()).width()
        textHeight = self.fontMetrics().boundingRect(self.text()).height()
        path.addText(QPoint(self.width()//2 - (textWidth)//2,self.height()//2 + textHeight//2), self.font(), self.text())
        painter.drawPath(path)

        painter.end()