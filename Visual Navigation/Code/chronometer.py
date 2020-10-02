import pygame, time
from pygame.locals import MOUSEBUTTONDOWN
from main import screenDrawer,eventCheck
from imagesCreator import img_buttons_chrono
pygame.init()

Wscreen = 1047
Hscreen = 633

screen = pygame.display.set_mode((Wscreen, Hscreen))
pygame.display.set_caption("Cronometro")


myScreen = screenDrawer(screen)
myEvent = eventCheck(screen)

buttons_pos_x = [(Wscreen * 40) / 100, (Wscreen * 55) / 100, (Wscreen * 10)/100]
buttons_pos_y = [(Hscreen * 60) / 100, (Hscreen * 60) / 100, (Hscreen * 10)/100]


class Time():

	def __init__(self):

		self.minutes = 0
		self.seconds = 0
		self.minutes_text = ""
		self.seconds_text = ""
		self.time_text = ""

	def resetTimer(self):

		self.minutes = 0
		self.seconds = 0
		self.minutes_text = ""
		self.seconds_text = ""

	def runChronometer(self):

		current_seconds = round(time.time() - start) % 60
		current_minute = round(time.time() - start) // 60

		if current_seconds < 10:
			
			self.seconds_text = "0" + str(current_seconds) 

		else:
			self.seconds_text = str(current_seconds) 


		self.minutes_text = str(current_minute)

		if current_minute < 10:

			self.minutes_text = "0" + str(current_minute)

			


		myScreen.drawText(self.minutes_text + ":" + self.seconds_text , 150, "digital7", (0,0,0),Wscreen/2,Hscreen/3)	




	def runTimer(self, times):
			

		current_seconds = times - round(time.time() - start)

		myScreen.drawText(str(current_seconds) , 150, "digital7", (0,0,0),Wscreen/2,Hscreen/3)				



Time = Time()

start = time.time()


while True:
	

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

		if event.type == MOUSEBUTTONDOWN and event.button == 1:
			clicked_button = myEvent.buttonEvent(buttons_pos_x, buttons_pos_y)
			print(clicked_button)

			if clicked_button == 0:

				InPause = True

				while InPause:

					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()	

						if event.type == MOUSEBUTTONDOWN and event.button == 1:
							clicked_button = myEvent.buttonEvent(buttons_pos_x, buttons_pos_y)
							print(clicked_button)


			elif clicked_button == 1:
				Timer.resetTimer()





	screen.fill((255,255,255))
	#Timer.runTimer()






	myScreen.drawButtons(buttons_pos_x,buttons_pos_y, img_buttons_chrono)
	Time.runTimer(250)

	pygame.display.update()





