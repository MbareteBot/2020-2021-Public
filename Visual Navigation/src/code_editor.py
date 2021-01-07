from PyQt5 import QtCore, QtGui, QtWidgets


class CodeEditorWindow(QtWidgets.QMainWindow):
    def __init__(self):
        self.setGeometry(0, 0, 100, 100)
        self.show()
        print("NEW")
