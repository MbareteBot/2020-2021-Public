from screen_manager import *
import sys

pygame.init()
screen = ScreenManager()

screen.setWindow(800,500)
screen.setTitle("Program")


def Buttons(positions, text):

	btn = Button(position=positions, dimensions = (150,30), bg_color = (100,100,100), caption=text)

	screen.draw(btn)







def main():


	clock = pygame.time.Clock()
	
	'''def __init__(self, 
					position, 
					dimensions = None, 
					skin_path = None,
					bg_color = (200,200,200),
					caption = "cta"):'''

	btn1 = Button(position = (10,10), dimensions = (150,30), bg_color = (100,100,100), caption="Click")



	running = True
	while running:

		for event in pygame.event.get():


			if event.type == pygame.QUIT:

				running = False
				sys.exit()



		
		screen.setBg(color=(150,150,150))
		

		#Buttons((50,50),"Submit")
		btn = Button(position=(50,50), dimensions = (100,30), bg_color = (100,100,100), caption="click")

		screen.draw(btn)



		screen.update()


		clock.tick(60)




main()

