import pygame, sys, math, time, os

from windowClass import *
from eventClass import *


pygame.init()



def main():


	print("\n-------------------------")
	print("-------------------------\n")

	monitor_size = pygame.display.Info()

	Wscreen = round((monitor_size.current_w * 80) / 100)
	Hscreen = round((monitor_size.current_h * 80) / 100)


	print(Wscreen, Hscreen)

	myScreen = WindowManager()
	myEvents = EventManager()

	myEvents.setWindowReference(Wscreen, Hscreen)
	myScreen.setWindow(Wscreen, Hscreen)
	myScreen.setTitle("Navegacion Visual")

	clock = pygame.time.Clock()

	buttons_pos_x = [(Wscreen * 35) / 100, (Wscreen * 45) / 100, (Wscreen * 55) /100, (Wscreen * 65) /100]
	buttons_pos_y = [10,10,10,10]


	while True:


		myEvents.setEventSource(pygame.mouse.get_pos())

		myScreen.setMousePos(pygame.mouse.get_pos())
	

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
	

			if event.type == MOUSEBUTTONDOWN and event.button == 1:

				if myScreen.MouseInsideDrawSection():
					
					
					myScreen.setVirtualRobotRotation()
					myEvents.setRobotPath()


				else:

					clicked_button = myEvents.getPressedButton(buttons_pos_x, buttons_pos_y)

					if clicked_button == 0:
						main()

					elif clicked_button == 1:
						myEvents.runStats()



		myScreen.drawBackground()
		myScreen.drawButtons(buttons_pos_x, buttons_pos_y)


		if len(myEvents.line_posX) == 0:

			if myScreen.MouseInsideDrawSection():

				myScreen.draw(myScreen.Imgs.img_robot, myEvents.eventSource[0] - 45, myEvents.eventSource[1] - 45)

		
		else:
			
			myScreen.drawRobotPath()


		pygame.display.update()	
		clock.tick(100)


if __name__ == "__main__":
	main()