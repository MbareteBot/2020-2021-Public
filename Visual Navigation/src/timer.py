from ui_main import * 

class timerWidget(Ui_MainWindow):
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