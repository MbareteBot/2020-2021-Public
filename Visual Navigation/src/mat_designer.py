from ui_main import *

class matDesignerWidget(Ui_MainWindow):

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
