from screen_manager import *
import sys

pygame.init()
screen = ScreenManager()

screen.setWindow(800,500)
screen.setTitle("Program")


def Buttons():

	btn = Button(position=(50,50), dimensions = (150,30), bg_color = (100,100,100), caption="Click Aqui")
	
	if btn.hover():
		btn.bg_color = (80,80,80)
	else:
		btn.bg_color = (100,100,100)


	if btn.clicked():
		btn.surface.width = 149
		btn.surface.height = 29


	screen.draw(btn)










def main():


	clock = pygame.time.Clock()
	
	'''def __init__(self, 
					position, 
					dimensions = None, 
					skin_path = None,
					bg_color = (200,200,200),
					caption = "cta"):'''




	running = True
	while running:

		for event in pygame.event.get():


			if event.type == pygame.QUIT:

				running = False
				sys.exit()



		
		screen.setBg(color=(150,150,150))
		

		#Buttons((50,50),"Submit")

		Buttons()


		screen.update()


		clock.tick(60)




main()

