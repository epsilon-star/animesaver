import sys

from PySide6 import QtCore, QtGui, QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    scene = QtWidgets.QGraphicsScene(QtCore.QRectF(0, 0, 200, 100))
    view = QtWidgets.QGraphicsView(
        scene, alignment=QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter
    )
    view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    view.setBackgroundBrush(QtGui.QColor("Blue")
    )
    view.setWindowTitle("Qt")

    line1 = scene.addLine(0, 0, 200, 100)
    line2 = scene.addLine(0, 100, 200, 0)
    pen = QtGui.QPen()
    pen.setDashPattern((4, 4))
    pen.setColor(QtGui.QColor("red"))
    line2.setPen(pen)

    rect = scene.addRect(QtCore.QRectF(QtCore.QPointF(50, 25), QtCore.QPointF(150, 75)))
    rect.setBrush(QtGui.QColor("blue"))

    view.resize(200, 100)
    view.show()

    sys.exit(app.exec_())