import pygame, sys, math, time, os

from event_manager import *
from window_manager import *


pygame.init()



def main():


	print("\n-------------------------")
	print("-------------------------\n")

	Wscreen = round(1024)
	Hscreen = round(600)


	print(Wscreen, Hscreen)

	window = WindowManager()
	eventListeners = EventManager()

	eventListeners.setWindowReference(Wscreen, Hscreen)
	window.setWindow(Wscreen, Hscreen)
	window.setTitle("Navegacion Visual")

	clock = pygame.time.Clock()

	buttons_pos_x = [(Wscreen * 35) / 100, (Wscreen * 45) / 100, (Wscreen * 55) /100, (Wscreen * 65) /100]
	buttons_pos_y = [10,10,10,10]


	while True:


		eventListeners.setEventSource(pygame.mouse.get_pos())

		window.setMousePos(pygame.mouse.get_pos())
	

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
	

			if event.type == MOUSEBUTTONDOWN and event.button == 1:

				if window.MouseInsideDrawSection():
					
					
					window.setVirtualRobotRotation()
					eventListeners.setRobotPath()


				else:

					clicked_button = eventListeners.getPressedButton(buttons_pos_x, buttons_pos_y)

					if clicked_button == 0:
						main()

					elif clicked_button == 1:
						eventListeners.runStats(window.surface)



		window.drawBackground()
		window.drawButtons(buttons_pos_x, buttons_pos_y)


		if len(eventListeners.line_posX) == 0:

			if window.MouseInsideDrawSection():

				window.draw(window.Imgs.img_robot, eventListeners.eventSource[0] - 45, eventListeners.eventSource[1] - 45)

		
		else:
			
			window.drawRobotPath()


		pygame.display.update()	
		


if __name__ == "__main__":
	main()