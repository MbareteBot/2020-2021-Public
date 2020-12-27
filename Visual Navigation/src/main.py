from ui_main import *
from mat_designer import *
from menu_bar import *
from timer import *

import os, pickle

class APP(menuBar, matDesignerWidget, timerWidget, Ui_MainWindow):
		
	def __init__(self):

		self.clicksPositions = []
		self.squareClicksPositions = []
		self.globalMX = 0
		self.globalMY = 0
		self.rectsColor = QtGui.QColor.fromRgb(40,40,40)
		self.linesColor = QtGui.QColor.fromRgb(80,80,80)

		self.lastPressedBtn = ""

		self.rects = []


	# TOOGLE MENU EFFECT 
	def toggleMenu(self):

	    width = self.LeftBar.width()
	    maxExtend = 180
	    standard = 60

	    if width == 60:
	        widthExtended = maxExtend
	    else:
	        widthExtended = standard

	    # ANIMATION
	    self.animation = QtCore.QPropertyAnimation(self.LeftBar, b"minimumWidth")
	    self.animation.setDuration(400)
	    self.animation.setStartValue(width)
	    self.animation.setEndValue(widthExtended)
	    self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
	    self.animation.start()




import resources_rc
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = APP()
    ui.setupUI(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


