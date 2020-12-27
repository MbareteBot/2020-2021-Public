from ui_main import *
import os, pickle

class APP(Ui_MainWindow):
		

	def __init__(self):
        # CREATING BUTTONS FUNCTIONALIY

		self.clicksPositions = []
		self.squareClicksPositions = []
		self.globalMX = 0
		self.globalMY = 0
		self.rectsColor = QtGui.QColor.fromRgb(40,40,40)
		self.linesColor = QtGui.QColor.fromRgb(80,80,80)

		self.lastPressedBtn = ""

		self.rects = []


    # ACITVATE THE SPECIFIC PAINT EVENT FOR THE MAIN FRAME
	def activateRectDrawing(self, event):
   		self.lastPressedBtn = "SQUARE"

	def activateLineDrawing(self, event):
	    self.lastPressedBtn = "LINE"


    # SETS THE PAINTER OBJECT BASED ON A COLOR -> IMPORTANT -> THIS IS USE TO DRAW ON THE FRAME
	def setPainter(self, color):
	    self.painter = QtGui.QPainter()
	    self.painter.begin(self.Frame_mat_replay)
	    self.pen = QtGui.QPen(color, 7, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.MiterJoin)

	    self.painter.setPen(self.pen)



	# PART OF THE DRAG AND DRAW FUNCTIONALIY FOR DRAWING RECTS
	def mouseReleaseEvent(self, event):

	    if self.lastPressedBtn == "SQUARE":
	        if len(self.squareClicksPositions) > 0:
	            self.rects.append([self.squareClicksPositions[-1][0], self.squareClicksPositions[-1][1], self.globalMX - self.squareClicksPositions[-1][0], self.globalMY - self.squareClicksPositions[-1][1]])



	# THIS IS THE PAINT EVENT ASSOCIATED TO THE MAIN FRAME -> IT'S BASED ON THE lastPressedBtn VARIABLE
	def paintEvent(self, event):

	    if self.lastPressedBtn == "SQUARE":
	        self.Frame_mat_replay.paintEvent = self.rectDrawing
	        self.rectDrawing(self.Frame_mat_replay)

	    elif self.lastPressedBtn == "LINE":
	        self.Frame_mat_replay.paintEvent = self.lineDrawing
	        self.lineDrawing(self.Frame_mat_replay)



	# DRAW BOTH LINES AND RECTS, THIS IS USED TO KEEP DRAWING OLDER SHAPES WHEN NEW SHAPES ARE BEING CREATED
	# THIS MUST BE DONE ANY TIME YOU CHANGE THE PAINT EVENT OBJECT FOR THE MAIN FRAME, OTHERWISE ONLY ALL PAST SHAPES WILL BE DELETED
	# ALL "DRAWINGS" ARE BASED ON AN ARRAY THAT STORES THE COORDENATES FOR THAT SHAPE
	def drawRectsAndLines(self):

	    if len(self.rects) > 0:

	        self.setPainter(self.rectsColor)
	        for rect in range(len(self.rects)):
	            self.painter.drawRect(self.rects[rect][0],self.rects[rect][1],self.rects[rect][2],self.rects[rect][3])

	        self.painter.end()


	    if len(self.clicksPositions) > 1:

	        self.setPainter(self.linesColor)
	        for click in range(len(self.clicksPositions)-1):
	            self.painter.drawLine(self.clicksPositions[click][0],self.clicksPositions[click][1],self.clicksPositions[click+1][0],self.clicksPositions[click+1][1])
	        self.painter.end()


	# SET A BUTTON COLOR WHEN IT'S CLICKED
	def setButtonsActiveStates(self):

	    if self.lastPressedBtn == "SQUARE":
	        self.Btn_square.setStyleSheet("background-color: rgb(70,70,70);\n"
	                                      "image: url(:/img/img/dotted-square.png);")
	        self.Btn_square.setEnabled(False)

	        self.Btn_straightLine.setEnabled(True)
	        self.Btn_straightLine.setStyleSheet("background-color: rgb(57,57,57);\n"
	                                            "image: url(:/img/img/pencil.png);")

	        rectQColor = self.rectsColor.getRgb() 
	        rectRgbColor = "rgb" + str((rectQColor[0], rectQColor[1], rectQColor[2])) 
	        self.Btn_colorPick.setStyleSheet("QPushButton {\n"
	                                           f"background-color: {rectRgbColor};\n"
	                                          "image: url(:/img/img/drop-silhouette.png);}")
	 

	    if self.lastPressedBtn == "LINE":
	        self.Btn_straightLine.setStyleSheet("background-color: rgb(70,70,70);\n"
	                                      "image: url(:/img/img/pencil.png);")
	        self.Btn_straightLine.setEnabled(False)

	        self.Btn_square.setEnabled(True)
	        self.Btn_square.setStyleSheet("background-color: rgb(57,57,57);\n"
	                                      "image: url(:/img/img/dotted-square.png);")

	        lineQColor = self.linesColor.getRgb() 
	        lineRgbColor = "rgb" + str((lineQColor[0], lineQColor[1], lineQColor[2])) 
	        self.Btn_colorPick.setStyleSheet("QPushButton {\n"
	                                           f"background-color: {lineRgbColor};\n"
	                                          "image: url(:/img/img/drop-silhouette.png);}")


	# ANIMATES THE "DRAG AND DROP" ANIMATION WHEN DRAWIN A RECT - JUST THAT :)
	def rectDrawing(self, event):


	    # DRAW RECTANGLE WHEN DRAGING
	    self.setButtonsActiveStates()
	    self.drawRectsAndLines()
	    self.setPainter(self.rectsColor)


	    # DRAG ANIMATION WHEN DRAWING RECT
	    if len(self.squareClicksPositions) > 0:
	        self.painter.drawRect(self.squareClicksPositions[-1][0], self.squareClicksPositions[-1][1], self.globalMX - self.squareClicksPositions[-1][0], self.globalMY - self.squareClicksPositions[-1][1])
	    

	    self.painter.end()

	    self.Frame_mat_replay.update()

	    # THIS ALLOWS THE MAIN FRAME TO CHANGE BETWEEN PAINTS EVENTS (RECTDRAWING OR LINEDRAWING)
	    self.Frame_mat_replay.paintEvent = self.paintEvent


	# DRAW LINES
	def lineDrawing(self, event):

	    self.setButtonsActiveStates()
	    self.drawRectsAndLines()
	    self.setPainter(self.linesColor)

	    if len(self.clicksPositions) > 0:
	        self.pen.setWidth(15)
	        self.painter.setPen(self.pen)
	        self.painter.drawPoint(self.clicksPositions[0][0], self.clicksPositions[0][1])
	        self.pen.setWidth(10)
	        self.painter.setPen(self.pen)

	    if len(self.clicksPositions) > 1:
	        for click in range(len(self.clicksPositions)-1):
	            self.painter.drawLine(self.clicksPositions[click][0],self.clicksPositions[click][1],self.clicksPositions[click+1][0],self.clicksPositions[click+1][1])

	    self.painter.end()
	    self.Frame_mat_replay.update()
	    self.Frame_mat_replay.paintEvent = self.paintEvent


	def colorPicker(self):
	    color = QtWidgets.QColorDialog.getColor()


	    if self.lastPressedBtn == "SQUARE":
	        self.rectsColor = color

	    elif self.lastPressedBtn == "LINE":
	        self.linesColor = color



	# UPDATES THE MOUSE POSITIONS VARIABLE
	def mouseMoveEvent(self, event):
	    self.globalMX = event.x()
	    self.globalMY = event.y()


	# WHENEVER THE FRAME GETS CLICKED, ADD THE CLICK (X,Y) POSITION TO THE RESPECTIVE ARRAY, BASED ON THE PAINT EVENT
	def mousePressEvent(self, event):

	    if self.lastPressedBtn == "SQUARE":

	        if len(self.squareClicksPositions) > 0:
	            self.squareClicksPositions.pop()
	        self.squareClicksPositions.append([event.x(), event.y()])

	    elif self.lastPressedBtn == "LINE":
	        self.clicksPositions.append([event.x(), event.y()])
	    
	    self.Frame_mat_replay.update()



	# DELETE THE LAST SHAPE 
	def goBack(self):

	    if self.lastPressedBtn == "SQUARE":

	        if len(self.squareClicksPositions) > 0:
	            self.squareClicksPositions.pop()

	        if len(self.rects) > 0:
	            self.rects.pop()
	            self.Frame_mat_replay.update()

	    if self.lastPressedBtn == "LINE":

	        if len(self.clicksPositions) > 0:
	            self.clicksPositions.pop()
	            self.Frame_mat_replay.update()




	# ASK FOR THE DIRECTORY AND SAVE THE CURRENT PATH (ONLY LINES ARE TAKING INTO ACCOUNG WHEN DEFINIG A "PATH") 
	# ALL LINES ARE CONSIDERED AS THE PATH
	def savePath(self):

	    realRobotCoordenates = []

	    winWidth, winHeight = MainWindow.width(), MainWindow.height()

	    for line in self.clicksPositions:
	        realRobotCoordenates.append([round(200/(MainWindow.width()/line[0])), round(130/(MainWindow.height()/(MainWindow.height()-line[1])))])

	    path = QtWidgets.QFileDialog.getSaveFileName(MainWindow, "Select Directory", os.getcwd(),"Mbarete files (*.mbarete)")

	    try:
	        with open(path[0], "wb") as file:

	            pickle.dump(self.clicksPositions, file)
	            pickle.dump(realRobotCoordenates, file)

	            print("\n---------------------------------")
	            print("Successfully saved binary file")
	    except:
	        print("Fail to save binary file")


	# OPEN AN EXISTING PATH (*.mbarete) AND DRAW THAT PATH ON THE MAIN FRAME
	def openExistingPath(self):

	    path = QtWidgets.QFileDialog.getOpenFileName(MainWindow, "Select File", os.getcwd(),"Mbarete files (*.mbarete)")
	    path_data = []

	    try:
	    	with open(path[0], "rb") as f:
	    		for _ in range(2):
	    			path_data.append(pickle.load(f))

	    	self.clicksPositions = path_data[0]
	    except: 
	    	print("Fail to open file")

	    self.lastPressedBtn = "LINE"
	    self.lineDrawing(self.Frame_mat_replay)


	# TAKE A SCREENSHOT
	def saveCapture(self):

	    path = QtWidgets.QFileDialog.getSaveFileName(MainWindow, "Select Directory", os.getcwd(),"Image files (*.png)")
	    try:
	        screen = QtWidgets.QApplication.primaryScreen()
	        screenshot = screen.grabWindow(self.stackedWidget.currentWidget().winId())
	        screenshot.save(path[0], 'png')
	    except:
	        print("Fail to save capture")


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

	# TIMER FUNCTIONALITY
	def playTimer(self):

	    if self.pressedBtn == "PLAY": self.pressedBtn = "PAUSE"
	    else: self.pressedBtn = "PLAY" 

	    if self.pressedBtn == "PAUSE":
	        self.timer.stop()
	        self.Btn_startTimer.setStyleSheet("image: url(:/img/img/flecha-correcta.png);")
	    elif self.pressedBtn == "PLAY":
	        self.timer.start(10) 
	        self.Btn_startTimer.setStyleSheet("image: url(:/img/img/pausa.png);")
	    
	    self.showTimer()

	# SHOW TIMER ON TIMER LABEL
	def showTimer(self):

		if self.pressedBtn == "PLAY":
			self.curr_time = self.curr_time.addMSecs(10)
			self.TimerNumber.display(self.curr_time.toString("mm:ss"))

	# STOP AND RESET TIMER
	def stopTimer(self):
		self.curr_time = QtCore.QTime(00,00,00)
		self.TimerNumber.display(self.curr_time.toString("mm:ss"))
		self.playTimer()


import resources_rc
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = APP()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())