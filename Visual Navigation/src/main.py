import resources_rc
from ui_main import *
from mat_designer import *
from menu_bar import *
from timer import *

import os
import pickle


class App(menuBar, matDesignerWidget, timerWidget, Ui_MainWindow):

    def __init__(self):

        self.clicksPositions = []
        self.squareClicksPositions = []
        self.globalMX = 0
        self.globalMY = 0
        self.rectsColor = QtGui.QColor.fromRgb(40, 40, 40)
        self.linesColor = QtGui.QColor.fromRgb(80, 80, 80)

        self.lastPressedBtn = ""

        self.rects = []
        self.graphicsElements = []


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = App()
    ui.setupUI(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
